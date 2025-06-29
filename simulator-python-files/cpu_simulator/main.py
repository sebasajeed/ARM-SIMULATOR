# cpu_simulator/main.py

from memory.memory import Memory
from cpu.register_file import RegisterFile
from isa.decoder import decode_instruction
import sys

def main(binary_file):
    memory = Memory()
    registers = RegisterFile()

    with open(binary_file, 'rb') as f:
        binary_data = f.read()
        memory.load_binary(binary_data)

    pc = 0
    while pc < len(binary_data):
        instr_word = memory.load_word(pc)
        instr = decode_instruction(instr_word)
        print(f"PC={pc:08X} INSTR=0x{instr_word:08X} {instr['mnemonic']} {instr['operands']}")
        pc += 4  # assuming fixed 32-bit instructions for now

    print("\nFinal Register State:")
    registers.dump()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <binary_file>")
    else:
        main(sys.argv[1])
