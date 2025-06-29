# isa/arm_instructions.py

from isa.instruction_set import Instruction

class MOV(Instruction):
    def execute(self, registers, memory, alu):
        dest, imm = self.operands
        registers.set(dest, imm)

class ADD(Instruction):
    def execute(self, registers, memory, alu):
        rd, rn, op2 = self.operands
        val = alu.add(registers.get(rn), op2)
        registers.set(rd, val)

class SUB(Instruction):
    def execute(self, registers, memory, alu):
        rd, rn, op2 = self.operands
        val = alu.sub(registers.get(rn), op2)
        registers.set(rd, val)

class CMP(Instruction):
    def execute(self, registers, memory, alu):
        rn, op2 = self.operands
        alu.cmp(registers.get(rn), op2)
