# memory/memory.py

class Memory:
    def __init__(self, size=1024*1024):
        self.size = size
        self.mem  = bytearray(size)

    def _check(self, addr, length=1):
        if not (0 <= addr < self.size and 0 < addr+length <= self.size):
            raise IndexError(f"Bad memory access @ {addr:#x}")

    def load_byte(self, addr):
        self._check(addr,1)
        return self.mem[addr]

    def store_byte(self, addr, val):
        self._check(addr,1)
        self.mem[addr] = val & 0xFF

    def load_word(self, addr):
        self._check(addr,4)
        return int.from_bytes(self.mem[addr:addr+4], 'little')

    def store_word(self, addr, val):
        self._check(addr,4)
        self.mem[addr:addr+4] = (val & 0xFFFFFFFF).to_bytes(4,'little')

    def load_binary(self, data, start=0):
        end = start + len(data)
        self._check(start,len(data))
        self.mem[start:end] = data

    def dump(self, start=0, end=64):
        print("Memory dump:")
        for addr in range(start, min(end, self.size), 4):
            word = self.load_word(addr)
            print(f"{addr}: {word}")

