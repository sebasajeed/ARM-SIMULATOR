# isa/addressing_modes.py

def pre_index(base, offset):
    return base + offset

def post_index(base, offset):
    return base

def apply_shift(value, shift_type, shift_amount):
    if shift_type == 'LSL':
        return value << shift_amount & 0xFFFFFFFF
    elif shift_type == 'LSR':
        return value >> shift_amount & 0xFFFFFFFF
    elif shift_type == 'ASR':
        return value >> shift_amount  # Arithmetic is same here for unsigned
    else:
        return value
