# cpu/alu.py

class ALU:
    def __init__(self, registers, flags):
        self.registers = registers
        self.flags = flags

    def execute(self, mnemonic, operands):
        if mnemonic == "MOV":
            dest, value = operands
            self.registers.set(dest, value)

        elif mnemonic == "ADD":
            dest, op1, op2 = operands
            result = self.registers.get(op1) + self.registers.get(op2)
            self.registers.set(dest, result)
            self._update_flags(result)

        elif mnemonic == "SUB":
            dest, op1, op2 = operands
            result = self.registers.get(op1) - self.registers.get(op2)
            self.registers.set(dest, result)
            self._update_flags(result)

        elif mnemonic == "NOP":
            pass  # No operation

        else:
            print(f"[ALU] Unsupported instruction: {mnemonic}")

    def _update_flags(self, result):
        self.flags.N = int(result < 0)
        self.flags.Z = int(result == 0)
        # For simplicity, carry and overflow flags are not updated here
