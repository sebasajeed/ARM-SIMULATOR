# isa/decoder.py

from isa.arm_instructions import decode_arm_instruction
from isa.thumb_instructions import decode_thumb_instruction

def is_thumb_instruction(word):
    # Check if the word represents a 16-bit Thumb instruction
    return word & 0xFFFF == word

def is_arm_instruction(word):
    # Check if the word represents a 32-bit ARM instruction
    return (word >> 28) & 0xF != 0xF  # Not unconditional encoding

def decode(word, pc):
    if is_thumb_instruction(word):
        return decode_thumb_instruction(word, pc)
    elif is_arm_instruction(word):
        return decode_arm_instruction(word, pc)
    else:
        return {
            "mnemonic": "UNKNOWN",
            "operands": [],
            "type": "INVALID"
        }
