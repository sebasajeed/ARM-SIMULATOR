from .register_file import RegisterFile
from .pipeline import Pipeline
from .condition_flags import check_condition
from .alu import ALU
from memory.memory import Memory
from output.logger import log_instruction, log_registers
from isa.decoder import decode_instruction

class CPU:
    def __init__(self, memory: Memory):
        self.mem       = memory
        self.regs      = RegisterFile()
        self.alu       = ALU(self.regs)
        self.pipeline  = Pipeline()
        self.pc        = 0

    def step(self):
    instr_word = self.mem.load_word(self.pc)
    instr = decode_instruction(instr_word)

    mnemonic = instr['mnemonic']
    operands = instr['operands']
    cond = instr['cond']

    print(f"[DEBUG] Decoded: mnemonic={mnemonic}, operands={operands}, cond={cond}")

    if check_condition(cond, self.regs.cpsr):
        print(f"[DEBUG] Condition passed: {cond}")

        if mnemonic == 'MOV':
            print(f"[DEBUG] Entered MOV block")

            rd, imm = operands
            print(f"[DEBUG] Calling set: set({rd}, {imm})")

            self.regs.set(rd, imm)

            print(f"[DEBUG] After set: R{rd} = {self.regs.get(rd)}")

    else:
        print(f"[DEBUG] Condition failed: {cond}")

    self.pc += 4


    def run(self, max_steps=100):
        steps = 0
        while steps < max_steps:
            self.step()
            steps += 1
