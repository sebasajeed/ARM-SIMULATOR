# isa/decoder.py

def is_thumb(instruction):
    # Placeholder for identifying Thumb
    return False  # For now, assume ARM only

def decode_instruction(raw_word):
    if raw_word == 0:
        return {'mnemonic': 'NOP', 'operands': [], 'cond': 'AL'}
    else:
        return {'mnemonic': 'MOV', 'operands': [0, raw_word], 'cond': 'AL'}
