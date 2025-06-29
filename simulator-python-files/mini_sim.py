# mini_sim.py

from dataclasses import dataclass
import sys

# --- Memory ---
class Memory:
    def __init__(self, size=1024):
        self.mem = bytearray(size)
    def load_word(self, addr):
        return int.from_bytes(self.mem[addr:addr+4], 'little')
    def store_binary(self, data):
        self.mem[0:len(data)] = data

# --- Registers ---
class RegisterFile:
    def __init__(self):
        self.regs = [0]*16
    def set(self, r, v):    self.regs[r] = v & 0xFFFFFFFF
    def get(self, r):       return self.regs[r]
    def dump(self):
        for i,v in enumerate(self.regs):
            print(f"R{i:2} = {v}")
        print()

# --- Decoder ---
@dataclass
class Instr:
    mnemonic: str
    operands: tuple
    size: int = 4

def decode(raw):
    if raw == 0:
        return Instr('NOP', ())
    else:
        return Instr('MOV', (0, raw))

# --- CPU ---
class CPU:
    def __init__(self, mem):
        self.mem = mem
        self.regs = RegisterFile()
        self.pc = 0

    def step(self):
        w = self.mem.load_word(self.pc)
        instr = decode(w)
        print(f"PC={self.pc:08X}  {instr.mnemonic} {instr.operands}")
        if instr.mnemonic == 'MOV':
            rd, imm = instr.operands
            print(f"  -> executing MOV: R{rd} = {imm}")
            self.regs.set(rd, imm)
        self.pc += instr.size

    def run(self):
        while self.pc < 8:     # hard-coded for 2 instructions
            self.step()
        print("\nFinal:")
        self.regs.dump()

# --- Main ---
if __name__ == "__main__":
    if len(sys.argv)!=2:
        print("Usage: python mini_sim.py <binary>")
        sys.exit(1)

    data = open(sys.argv[1],'rb').read()
    mem = Memory(256)
    mem.store_binary(data)
    cpu = CPU(mem)
    cpu.run()
