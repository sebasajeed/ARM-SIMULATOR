# cpu/alu.py

class ALU:
    def __init__(self, registers):
        self.regs = registers

    def add(self, op1, op2):
        result = (op1 + op2) & 0xFFFFFFFF
        self._update_flags(result)
        return result

    def sub(self, op1, op2):
        result = (op1 - op2) & 0xFFFFFFFF
        self._update_flags(result)
        return result

    def and_op(self, op1, op2):
        result = op1 & op2
        self._update_flags(result)
        return result

    def orr_op(self, op1, op2):
        result = op1 | op2
        self._update_flags(result)
        return result

    def cmp(self, op1, op2):
        result = (op1 - op2) & 0xFFFFFFFF
        self._update_flags(result)

    def _update_flags(self, result):
        self.regs.set_flag('Z', int(result == 0))
        self.regs.set_flag('N', int((result >> 31) & 1))
