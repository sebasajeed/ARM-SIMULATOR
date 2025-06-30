# cpu/condition_flags.py

class ConditionFlags:
    def __init__(self):
        self.N = 0  # Negative flag
        self.Z = 0  # Zero flag
        self.C = 0  # Carry flag
        self.V = 0  # Overflow flag

    def __str__(self):
        return (
            "CPSR:\n"
            f"N = {self.N}\n"
            f"Z = {self.Z}\n"
            f"C = {self.C}\n"
            f"V = {self.V}"
        )

    def check_condition(self, cond):
        cond = cond.upper()
        if cond == 'EQ':      # Equal
            return self.Z == 1
        elif cond == 'NE':    # Not equal
            return self.Z == 0
        elif cond in ('CS', 'HS'):  # Carry set / unsigned higher or same
            return self.C == 1
        elif cond in ('CC', 'LO'):  # Carry clear / unsigned lower
            return self.C == 0
        elif cond == 'MI':    # Minus / negative
            return self.N == 1
        elif cond == 'PL':    # Plus / positive or zero
            return self.N == 0
        elif cond == 'VS':    # Overflow
            return self.V == 1
        elif cond == 'VC':    # No overflow
            return self.V == 0
        elif cond == 'HI':    # Unsigned higher
            return self.C == 1 and self.Z == 0
        elif cond == 'LS':    # Unsigned lower or same
            return self.C == 0 or self.Z == 1
        elif cond == 'GE':    # Signed greater than or equal
            return self.N == self.V
        elif cond == 'LT':    # Signed less than
            return self.N != self.V
        elif cond == 'GT':    # Signed greater than
            return self.Z == 0 and self.N == self.V
        elif cond == 'LE':    # Signed less than or equal
            return self.Z == 1 or self.N != self.V
        elif cond == 'AL':    # Always
            return True
        else:
            print(f"[DEBUG] Unknown condition: {cond}")
            return False
