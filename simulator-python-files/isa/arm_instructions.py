# isa/arm_instructions.py

def decode_arm_instruction(word, pc):
    cond = (word >> 28) & 0xF
    i_bit = (word >> 25) & 0x1
    opcode = (word >> 21) & 0xF
    s_bit = (word >> 20) & 0x1
    rn = (word >> 16) & 0xF
    rd = (word >> 12) & 0xF
    operand2 = word & 0xFFF

    # ARM opcode lookup
    opcode_map = {
        0x0: 'AND',
        0x1: 'EOR',
        0x2: 'SUB',
        0x3: 'RSB',
        0x4: 'ADD',
        0x5: 'ADC',
        0x6: 'SBC',
        0x7: 'RSC',
        0x8: 'TST',
        0x9: 'TEQ',
        0xA: 'CMP',
        0xB: 'CMN',
        0xC: 'ORR',
        0xD: 'MOV',
        0xE: 'BIC',
        0xF: 'MVN',
    }

    mnemonic = opcode_map.get(opcode, 'UNKNOWN')

    def format_operand2(op2):
        if i_bit:
            imm = op2 & 0xFF
            rotate = ((op2 >> 8) & 0xF) * 2
            if rotate:
                imm = (imm >> rotate) | ((imm << (32 - rotate)) & 0xFFFFFFFF)
            return f"#{imm}"
        else:
            rm = op2 & 0xF
            return f"R{rm}"

    # Special formats for testing instructions (no destination register)
    if mnemonic in ('TST', 'TEQ', 'CMP', 'CMN'):
        operands = [f"R{rn}", format_operand2(operand2)]
    elif mnemonic == 'MOV':
        operands = [f"R{rd}", format_operand2(operand2)]
    elif mnemonic == 'MVN':
        operands = [f"R{rd}", format_operand2(operand2)]
    else:
        operands = [f"R{rd}", f"R{rn}", format_operand2(operand2)]

    return {
        'mnemonic': mnemonic,
        'operands': operands,
        'type': 'DP'
    }
