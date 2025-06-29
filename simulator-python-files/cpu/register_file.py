class RegisterFile:
    def __init__(self):
        self.registers = [0] * 16
        self.cpsr = {'N': 0, 'Z': 0, 'C': 0, 'V': 0}

    def get(self, reg_num):
        return self.registers[reg_num]

    def set(self, reg_num, value):
        print(f"[DEBUG] register_file.set(): Writing {value} to R{reg_num}")
        self.registers[reg_num] = value & 0xFFFFFFFF


    def set_flag(self, flag, value):
        if flag in self.cpsr:
            self.cpsr[flag] = 1 if value else 0

    def get_flag(self, flag):
        return self.cpsr.get(flag, 0)

    def dump(self):
        print("Registers:")
        for i, val in enumerate(self.registers):
            print(f"R{i} = {val}")
        print("CPSR:")
        for flag in self.cpsr:
            print(f"{flag} = {self.cpsr[flag]}")
