# isa/instruction_set.py

class Instruction:
    def __init__(self, raw, mnemonic, operands, cond='AL'):
        self.raw = raw
        self.mnemonic = mnemonic
        self.operands = operands
        self.cond = cond
	self.size = size

    def execute(self, registers, memory, alu):
        raise NotImplementedError("Execute must be implemented by subclass.")
