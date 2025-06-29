from cpu.cpu import CPU
from memory.memory import Memory
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 -m cpu_simulator.main <binary_file>")
        return

    binary_file = sys.argv[1]

    # Load binary data into memory
    with open(binary_file, 'rb') as f:
        data = f.read()

    mem = Memory(data)  # ✅ Pass data to Memory
    cpu = CPU(mem)      # ✅ Pass memory to CPU

    cpu.run()

if __name__ == "__main__":
    main()
