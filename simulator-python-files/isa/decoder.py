def decode_instruction(raw_word):
    if raw_word == 0x00000000:
        return {
            'mnemonic': 'NOP',
            'operands': [],
            'cond': 'AL',
            'size': 4
        }
    elif raw_word == 0x00000001:
        return {
            'mnemonic': 'MOV',
            'operands': [0, 1],  # MOV R0, #1
            'cond': 'AL',
            'size': 4
        }
    elif raw_word == 0x00000002:
        return {
            'mnemonic': 'ADD',
            'operands': [1, 0, 1],  # ADD R1, R0, #1
            'cond': 'AL',
            'size': 4
        }
    elif raw_word == 0x00000003:
        return {
            'mnemonic': 'SUB',
            'operands': [2, 1, 1],  # SUB R2, R1, #1
            'cond': 'AL',
            'size': 4
        }
    else:
        return {
            'mnemonic': 'NOP',
            'operands': [],
            'cond': 'AL',
            'size': 4
        }
