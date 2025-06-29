# isa/decoder.py

from isa.arm_instructions import decode_arm_instruction
from isa.thumb_instructions import decode_thumb_instruction  # ✅ FIXED import

def decode(instruction):
    # ARM/Thumb mode detection can be more advanced, but for now assume 32-bit ARM
    if (instruction & 0xFFFF0000) == 0:  # crude check for Thumb 16-bit
        return decode_thumb_instruction(instruction & 0xFFFF)
    else:
        return decode_arm_instruction(instruction)
