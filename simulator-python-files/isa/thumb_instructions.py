# isa/thumb_instructions.py

from isa.instruction_set import Instruction

class ThumbNOP(Instruction):
    def execute(self, registers, memory, alu):
        pass  # No operation
