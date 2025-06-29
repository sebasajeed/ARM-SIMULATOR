# cpu/cpu.py

from isa.decoder import decode
from cpu.register_file import RegisterFile
from cpu.condition_flags import ConditionFlags
from cpu.alu import ALU
from memory.memory import Memory
from output.logger import debug, error

class CPU:
    def __init__(self, memory):
        self.register_file = RegisterFile()
        self.flags = ConditionFlags()
        self.alu = ALU(self.register_file, self.flags)
        self.memory = memory if isinstance(memory, Memory) else Memory(memory)

    def fetch(self):
        pc = self.register_file.get_pc()
        instruction = self.memory.load_word(pc)
        debug(f"fetch(): PC = {pc}, instruction = 0x{instruction:08x}")
        self.register_file.set_pc(pc + 4)
        return instruction

    def decode(self, instruction):
        decoded = decode(instruction)
        debug(f"decode(): Decoded instruction: {decoded}")
        return decoded

    def execute_instruction(self, decoded):
        mnemonic = decoded["mnemonic"]
        operands = decoded["operands"]

        if mnemonic == "MOV":
            dest = int(operands[0][1:])
            val = self._parse_operand(operands[1])
            self.register_file.write(dest, val)

        elif mnemonic == "ADD":
            rd = int(operands[0][1:])
            rn = int(operands[1][1:])
            op2 = self._parse_operand(operands[2])
            val = self.register_file.read(rn) + op2
            self.register_file.write(rd, val)

        elif mnemonic == "SUB":
            rd = int(operands[0][1:])
            rn = int(operands[1][1:])
            op2 = self._parse_operand(operands[2])
            val = self.register_file.read(rn) - op2
            self.register_file.write(rd, val)

        elif mnemonic == "LDR":
            rd = int(operands[0][1:])
            addr = self._parse_memory_address(operands[1])
            val = self.memory.load_word(addr)
            self.register_file.write(rd, val)

        elif mnemonic == "STR":
            rd = int(operands[0][1:])
            addr = self._parse_memory_address(operands[1])
            val = self.register_file.read(rd)
            self.memory.store_word(addr, val)

        elif mnemonic == "B":
            target = int(operands[0])
            self.register_file.set_pc(target)

        elif mnemonic == "CMP":
            rn = int(operands[0][1:])
            op2 = self._parse_operand(operands[1])
            result = self.register_file.read(rn) - op2
            self.flags.update_flags(result)

        elif mnemonic == "INVALID FORMAT":
            error("Invalid decoded format")

    def _parse_operand(self, op):
        if op.startswith("#"):
            return int(op[1:])
        elif op.startswith("R"):
            return self.register_file.read(int(op[1:]))
        else:
            raise ValueError(f"Unknown operand format: {op}")

    def _parse_memory_address(self, addr_str):
        # parses format like "[R2, #8]"
        addr_str = addr_str.strip("[]")
        parts = addr_str.split(",")
        base = self.register_file.read(int(parts[0][1:]))
        offset = int(parts[1].strip()[1:]) if len(parts) > 1 else 0
        return base + offset

    def run(self):
        while True:
            try:
                instruction = self.fetch()
                decoded = self.decode(instruction)
                self.execute_instruction(decoded)
            except Exception as e:
                error(str(e))
                break
