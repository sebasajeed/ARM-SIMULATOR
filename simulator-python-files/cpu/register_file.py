# cpu/register_file.py

class RegisterFile:
    def __init__(self):
        self.registers = [0] * 16  # R0 to R15
        self.PC_INDEX = 15

    def get(self, index):
        return self.registers[index]

    def set(self, index, value):
        self.registers[index] = value & 0xFFFFFFFF  # Ensure 32-bit values

    def get_pc(self):
        return self.registers[self.PC_INDEX]

    def set_pc(self, value):
        print(f"[DEBUG] register_file.set_pc(): Setting PC to {value}")
        self.registers[self.PC_INDEX] = value & 0xFFFFFFFF

    def write(self, index, value):
        self.set(index, value)

    def read(self, index):
        return self.get(index)

    def __str__(self):
        output = ""
        for i in range(13):
            output += f"R{i:2}: {self.get(i):08X}\n"
        output += f"SP : {self.get(13):08X}\n"
        output += f"LR : {self.get(14):08X}\n"
        output += f"PC : {self.get_pc():08X}\n"
        return output
