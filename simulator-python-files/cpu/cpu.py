# cpu/cpu.py

from cpu.alu import ALU
from cpu.register_file import RegisterFile
from cpu.condition_flags import ConditionFlags
from isa.decoder import decode
from output.logger import debug, error, info

class CPU:
    def __init__(self, memory):
        self.memory = memory  # ✅ Memory object, not data
        self.registers = RegisterFile()
        self.flags = ConditionFlags()
        self.alu = ALU(self.registers, self.flags)
        self.running = True
        self.thumb_mode = False  # Add Thumb mode flag

    def fetch(self):
        pc = self.registers.get_pc()
        try:
            if self.thumb_mode:
                # Fetch 16-bit Thumb instruction
                instruction = self.memory.read_byte(pc) | (self.memory.read_byte(pc + 1) << 8)
                debug(f"fetch(): PC = {pc}, Thumb instruction = {instruction:04x}")
                self.registers.set_pc(pc + 2)  # Thumb instructions are 2 bytes
            else:
                # Fetch 32-bit ARM instruction
                instruction = self.memory.read_word(pc)
                debug(f"fetch(): PC = {pc}, ARM instruction = {instruction:08x}")
                self.registers.set_pc(pc + 4)  # ARM instructions are 4 bytes
        except IndexError:
            error(f"Memory read out of bounds at address {pc}")
            self.running = False
            return 0, pc  # Return dummy instruction to avoid crash
        return instruction, pc

    def decode_execute(self, instruction, pc):
        if self.thumb_mode:
            # Force Thumb decoding
            from isa.thumb_instructions import decode_thumb_instruction
            decoded = decode_thumb_instruction(instruction, pc)
        else:
            # Force ARM decoding
            from isa.arm_instructions import decode_arm_instruction
            decoded = decode_arm_instruction(instruction, pc)
            
        debug(f"decode(): Decoded instruction: {decoded}")
        if decoded is None:
            error("decode(): Could not decode instruction")
            self.running = False
            return

        # Execute (only data-processing for now)
        if decoded['type'] == 'DP':
            self.execute_dp(decoded)

    def execute_dp(self, instr):
        mnemonic = instr['mnemonic']
        operands = instr['operands']

        if mnemonic == 'MOV':
            rd = int(operands[0][1:])
            if operands[1].startswith('#'):
                value = int(operands[1][1:])
            else:
                value = self.registers.read(int(operands[1][1:]))
            self.registers.write(rd, value)

        elif mnemonic in ['ADD', 'SUB', 'ADC', 'SBC']:
            rd = int(operands[0][1:])
            
            # Handle different operand patterns
            if len(operands) == 2:  # ADD Rd, Rm (2-operand form)
                rn_val = self.registers.read(rd)  # Use Rd as source
                if operands[1].startswith('#'):
                    op2_val = int(operands[1][1:])
                else:
                    op2_val = self.registers.read(int(operands[1][1:]))
            else:  # ADD Rd, Rn, Op2 (3-operand form)
                if operands[1].startswith('#'):
                    rn_val = int(operands[1][1:])
                else:
                    rn_val = self.registers.read(int(operands[1][1:]))
                
                if operands[2].startswith('#'):
                    op2_val = int(operands[2][1:])
                else:
                    op2_val = self.registers.read(int(operands[2][1:]))

            if mnemonic == 'ADD':
                result = (rn_val + op2_val) & 0xFFFFFFFF
            elif mnemonic == 'SUB':
                result = (rn_val - op2_val) & 0xFFFFFFFF
            elif mnemonic == 'ADC':
                result = (rn_val + op2_val + (1 if self.flags.C else 0)) & 0xFFFFFFFF
            elif mnemonic == 'SBC':
                result = (rn_val - op2_val - (0 if self.flags.C else 1)) & 0xFFFFFFFF

            self.registers.write(rd, result)
            
            # Update flags for Thumb instructions (they typically update flags)
            if self.thumb_mode:
                self.flags.Z = 1 if result == 0 else 0
                self.flags.N = 1 if (result & 0x80000000) != 0 else 0

        elif mnemonic in ['AND', 'EOR', 'ORR', 'BIC']:
            rd = int(operands[0][1:])
            rn_val = self.registers.read(rd)  # Use Rd as source for Thumb
            
            if operands[1].startswith('#'):
                op2_val = int(operands[1][1:])
            else:
                op2_val = self.registers.read(int(operands[1][1:]))

            if mnemonic == 'AND':
                result = rn_val & op2_val
            elif mnemonic == 'EOR':
                result = rn_val ^ op2_val
            elif mnemonic == 'ORR':
                result = rn_val | op2_val
            elif mnemonic == 'BIC':
                result = rn_val & (~op2_val)

            self.registers.write(rd, result & 0xFFFFFFFF)
            
            # Update flags for Thumb instructions
            if self.thumb_mode:
                self.flags.Z = 1 if result == 0 else 0
                self.flags.N = 1 if (result & 0x80000000) != 0 else 0

        elif mnemonic in ['CMP', 'CMN', 'TST']:
            rd = int(operands[0][1:])
            rn_val = self.registers.read(rd)
            
            if operands[1].startswith('#'):
                op2_val = int(operands[1][1:])
            else:
                op2_val = self.registers.read(int(operands[1][1:]))

            if mnemonic == 'CMP':
                result = (rn_val - op2_val) & 0xFFFFFFFF
            elif mnemonic == 'CMN':
                result = (rn_val + op2_val) & 0xFFFFFFFF
            elif mnemonic == 'TST':
                result = rn_val & op2_val

            # Update flags
            self.flags.Z = 1 if result == 0 else 0
            self.flags.N = 1 if (result & 0x80000000) != 0 else 0

        elif mnemonic in ['LSL', 'LSR', 'ASR', 'ROR']:
            rd = int(operands[0][1:])
            rm_val = self.registers.read(int(operands[1][1:]))
            
            if len(operands) > 2 and operands[2].startswith('#'):
                shift_amount = int(operands[2][1:])
            else:
                shift_amount = 1  # Default shift

            if mnemonic == 'LSL':
                result = (rm_val << shift_amount) & 0xFFFFFFFF
            elif mnemonic == 'LSR':
                result = rm_val >> shift_amount
            elif mnemonic == 'ASR':
                if rm_val & 0x80000000:  # Negative number
                    result = (rm_val >> shift_amount) | (0xFFFFFFFF << (32 - shift_amount))
                else:
                    result = rm_val >> shift_amount
            elif mnemonic == 'ROR':
                result = ((rm_val >> shift_amount) | (rm_val << (32 - shift_amount))) & 0xFFFFFFFF

            self.registers.write(rd, result)
            
            # Update flags for Thumb instructions
            if self.thumb_mode:
                self.flags.Z = 1 if result == 0 else 0
                self.flags.N = 1 if (result & 0x80000000) != 0 else 0

        elif mnemonic == 'NEG':
            rd = int(operands[0][1:])
            rm_val = self.registers.read(int(operands[1][1:]))
            result = (-rm_val) & 0xFFFFFFFF
            self.registers.write(rd, result)
            
            # Update flags
            if self.thumb_mode:
                self.flags.Z = 1 if result == 0 else 0
                self.flags.N = 1 if (result & 0x80000000) != 0 else 0

        elif mnemonic == 'MUL':
            rd = int(operands[0][1:])
            rm_val = self.registers.read(int(operands[1][1:]))
            rn_val = self.registers.read(rd)  # Thumb MUL uses Rd as source too
            result = (rn_val * rm_val) & 0xFFFFFFFF
            self.registers.write(rd, result)
            
            # Update flags
            if self.thumb_mode:
                self.flags.Z = 1 if result == 0 else 0
                self.flags.N = 1 if (result & 0x80000000) != 0 else 0

        elif mnemonic == 'MVN':
            rd = int(operands[0][1:])
            rm_val = self.registers.read(int(operands[1][1:]))
            result = (~rm_val) & 0xFFFFFFFF
            self.registers.write(rd, result)
            
            # Update flags for Thumb instructions
            if self.thumb_mode:
                self.flags.Z = 1 if result == 0 else 0
                self.flags.N = 1 if (result & 0x80000000) != 0 else 0

    def run(self):
        instruction_count = 0
        max_instructions = 1000  # Prevent infinite loops
        
        while self.running and instruction_count < max_instructions:
            try:
                instr, pc = self.fetch()
                self.decode_execute(instr, pc)
                instruction_count += 1
                
                # Stop if we reach end of program (all zeros or invalid instructions)
                if instr == 0:
                    print(f"[INFO] Hit NOP/end of program at PC {pc}")
                    break
                    
            except Exception as e:
                error(str(e))
                self.running = False

        print(f"\n==== Execution Complete ====")
        print(f"Instructions executed: {instruction_count}")
        print("\n==== Final Register State ====")
        print(self.registers)
