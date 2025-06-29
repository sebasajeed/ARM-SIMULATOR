# memory/memory.py

class Memory:
    def __init__(self, size):
        self.data = bytearray(size)

    def load(self, data: bytes, start_address: int = 0):
        self.data[start_address:start_address + len(data)] = data

    def read_byte(self, address: int) -> int:
        return self.data[address]

    def write_byte(self, address: int, value: int):
        self.data[address] = value & 0xFF

    def read_word(self, address: int) -> int:
        """Reads a 32-bit word from memory starting at the given address (little-endian)."""
        return (
            self.data[address]
            | (self.data[address + 1] << 8)
            | (self.data[address + 2] << 16)
            | (self.data[address + 3] << 24)
        )

    def write_word(self, address: int, value: int):
        """Writes a 32-bit word to memory at the given address (little-endian)."""
        self.data[address] = value & 0xFF
        self.data[address + 1] = (value >> 8) & 0xFF
        self.data[address + 2] = (value >> 16) & 0xFF
        self.data[address + 3] = (value >> 24) & 0xFF
