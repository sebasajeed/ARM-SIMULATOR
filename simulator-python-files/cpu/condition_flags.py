# cpu/condition_flags.py

def check_condition(cond, cpsr):
    if cond == 'AL':
        return True
    elif cond == 'EQ':
        return cpsr['Z'] == 1
    elif cond == 'NE':
        return cpsr['Z'] == 0
    elif cond == 'LT':
        return cpsr['N'] != cpsr['V']
    elif cond == 'GE':
        return cpsr['N'] == cpsr['V']
    elif cond == 'GT':
        return cpsr['Z'] == 0 and cpsr['N'] == cpsr['V']
    elif cond == 'LE':
        return cpsr['Z'] == 1 or cpsr['N'] != cpsr['V']
    else:
        return False  
