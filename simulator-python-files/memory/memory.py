# memory/memory.py

class Memory:
    def __init__(self, data: bytes):
        self.data = bytearray(data)

    def load(self, address: int, size: int = 4) -> int:
        """Load `size` bytes starting from `address` and return as an int (little-endian)."""
        if address + size > len(self.data):
            raise IndexError(f"Memory read out of bounds at address {address}")
        return int.from_bytes(self.data[address:address + size], byteorder='little')

    def load_word(self, address: int) -> int:
        """Load a 4-byte word from memory."""
        return self.load(address, size=4)

    def load_halfword(self, address: int) -> int:
        """Load a 2-byte halfword from memory."""
        return self.load(address, size=2)

    def store(self, address: int, value: int, size: int = 4):
        """Store `value` as `size` bytes at `address` (little-endian)."""
        if address + size > len(self.data):
            raise IndexError(f"Memory write out of bounds at address {address}")
        self.data[address:address + size] = value.to_bytes(size, byteorder='little')

    def store_word(self, address: int, value: int):
        """Store a 4-byte word into memory."""
        self.store(address, value, size=4)

    def store_halfword(self, address: int, value: int):
        """Store a 2-byte halfword into memory."""
        self.store(address, value, size=2)

    def size(self):
        """Return the size of memory in bytes."""
        return len(self.data)

    def __len__(self):
        return len(self.data)
