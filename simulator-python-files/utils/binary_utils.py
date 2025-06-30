# utils/binary_utils.py

def extract_bits(val, start, end):
    mask = (1 << (end - start + 1)) - 1
    return (val >> start) & mask

def sign_extend(val, bits):
    sign = 1 << (bits - 1)
    return (val & (sign - 1)) - (val & sign)
