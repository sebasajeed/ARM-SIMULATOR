# isa/thumb_instructions.py

def decode_thumb_instruction(instruction):
    # Basic NOP decoder as a fallback placeholder
    if instruction == 0x46C0:  # NOP (MOV R8, R8)
        return {
            "mnemonic": "NOP",
            "operands": [],
            "type": "MISC"
        }

    # Can add more Thumb decoding here
    return {
        "mnemonic": "INVALID FORMAT",
        "operands": [],
        "type": "UNKNOWN"
    }
