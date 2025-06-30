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

    def fetch(self):
        pc = self.registers.get_pc()
        try:
            instruction = self.memory.read_word(pc)
        except IndexError:
            error(f"Memory read out of bounds at address {pc}")
            self.running = False
            return 0, pc  # Return dummy instruction to avoid crash
        debug(f"fetch(): PC = {pc}, instruction = {instruction:08x}")
        self.registers.set_pc(pc + 4)
        return instruction, pc

    def decode_execute(self, instruction, pc):
        decoded = decode(instruction, pc)
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

        elif mnemonic in ['ADD', 'SUB', 'ADC']:
            rd = int(operands[0][1:])
            rn = int(operands[1][1:])
            op2 = operands[2]

            if op2.startswith('#'):
                value2 = int(op2[1:])
            else:
                value2 = self.registers.read(int(op2[1:]))

            value1 = self.registers.read(rn)
            if mnemonic == 'ADD':
                result = value1 + value2
            elif mnemonic == 'SUB':
                result = value1 - value2
            elif mnemonic == 'ADC':
                result = value1 + value2 + (1 if self.flags.C else 0)

            self.registers.write(rd, result)

    def run(self):
        while self.running:
            try:
                instr, pc = self.fetch()
                self.decode_execute(instr, pc)
            except Exception as e:
                error(str(e))
                self.running = False

        print("\n==== Final Register State ====")
        print(self.registers)
