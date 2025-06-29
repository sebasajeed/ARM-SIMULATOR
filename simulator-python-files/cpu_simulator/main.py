import sys
from memory.memory import Memory
from cpu.cpu import CPU

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 -m cpu_simulator.main <binary_file>")
        return

    binary_file = sys.argv[1]
    mem = Memory()
    mem.load_binary(binary_file)

    cpu = CPU(mem)
    cpu.run()

if __name__ == '__main__':
    main()
