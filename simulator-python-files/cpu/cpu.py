from .register_file import RegisterFile
from .pipeline import Pipeline
from .condition_flags import check_condition
from .alu import ALU
from memory.memory import Memory
from output.logger import log_instruction, log_registers
from isa.decoder import decode_instruction

class CPU:
    def __init__(self, memory: Memory):
        self.mem = memory
        self.regs = RegisterFile()
        self.alu = ALU(self.regs)
        self.pipeline = Pipeline()
        self.pc = 0

    def step(self):
        instr_word = self.mem.load_word(self.pc)
        instr = decode_instruction(instr_word)
        log_instruction(self.pc, instr_word, instr)

        mnemonic = instr['mnemonic']
        operands = instr['operands']
        cond = instr['cond']

        print(f"PC={self.pc:08X} INSTR=0x{instr_word:08X} {mnemonic} {operands}")
        print(f"[DEBUG] Condition: {cond} Result: {check_condition(cond, self.regs.cpsr)}")

        if check_condition(cond, self.regs.cpsr):
            if mnemonic == 'NOP':
                pass
            elif mnemonic == 'MOV':
                dest = operands[0]
                value = operands[1]
                self.regs.set(dest, value)
            elif mnemonic == 'ADD':
                rd, rn, imm = operands
                self.regs.set(rd, self.regs.get(rn) + imm)
            elif mnemonic == 'SUB':
                rd, rn, imm = operands
                self.regs.set(rd, self.regs.get(rn) - imm)
            else:
                print(f"[WARNING] Unsupported mnemonic: {mnemonic}")
        else:
            print(f"[DEBUG] Condition {cond} failed; skipping")

        self.pc += instr.get('size', 4)

    def run(self):
        while True:
            instr_word = self.mem.load_word(self.pc)
            if instr_word == 0x00000000:
                break
            self.step()

        print("\nFinal Register State:")
        print("Registers:")
        for i in range(16):
            print(f"R{i} = {self.regs.get(i)}")
        print("CPSR:")
        for flag in ['N', 'Z', 'C', 'V']:
            print(f"{flag} = {self.regs.get_flag(flag)}")
