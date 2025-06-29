# isa/arm_instructions.py

def decode_arm_instruction(instruction):
    cond = (instruction >> 28) & 0xF
    opcode = (instruction >> 21) & 0xF
    i_bit = (instruction >> 25) & 0x1
    mnemonic = "UNKNOWN"
    operands = []
    inst_type = "UNKNOWN"

    if (instruction & 0x0C000000) == 0x00000000:  # Data Processing
        rn = (instruction >> 16) & 0xF
        rd = (instruction >> 12) & 0xF
        operand2 = instruction & 0xFFF

        if i_bit:
            operand2_str = f"#{operand2}"
        else:
            rm = instruction & 0xF
            operand2_str = f"R{rm}"

        if opcode == 0b1101:
            mnemonic = "MOV"
            operands = [f"R{rd}", operand2_str]
        elif opcode == 0b0100:
            mnemonic = "ADD"
            operands = [f"R{rd}", f"R{rn}", operand2_str]
        elif opcode == 0b0010:
            mnemonic = "SUB"
            operands = [f"R{rd}", f"R{rn}", operand2_str]
        elif opcode == 0b1010:
            mnemonic = "CMP"
            operands = [f"R{rn}", operand2_str]

        inst_type = "DP"

    elif (instruction & 0x0C000000) == 0x04000000:  # LDR/STR
        l_bit = (instruction >> 20) & 1
        rn = (instruction >> 16) & 0xF
        rd = (instruction >> 12) & 0xF
        offset = instruction & 0xFFF

        mnemonic = "LDR" if l_bit else "STR"
        operands = [f"R{rd}", f"[R{rn}, #{offset}]"]
        inst_type = "MEM"

    elif (instruction & 0x0E000000) == 0x0A000000:  # B, BL
        link = (instruction >> 24) & 1
        offset = instruction & 0xFFFFFF
        offset = offset << 2
        if offset & (1 << 25):  # sign extend
            offset |= ~((1 << 26) - 1)
        target = offset

        mnemonic = "BL" if link else "B"
        operands = [f"{target}"]
        inst_type = "BR"

    return {
        "mnemonic": mnemonic,
        "operands": operands,
        "type": inst_type
    }
