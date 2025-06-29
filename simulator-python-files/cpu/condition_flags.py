def check_condition(cond, cpsr):
    N = cpsr.get('N', 0)
    Z = cpsr.get('Z', 0)
    C = cpsr.get('C', 0)
    V = cpsr.get('V', 0)

    if cond == 'EQ':
        return Z == 1
    elif cond == 'NE':
        return Z == 0
    elif cond == 'AL':
        return True
    return False  # Default: fail
