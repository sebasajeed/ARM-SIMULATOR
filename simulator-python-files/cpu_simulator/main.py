from cpu.cpu import CPU
from memory.memory import Memory
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 -m cpu_simulator.main <binary_file> [--thumb]")
        return

    binary_file = sys.argv[1]
    thumb_mode = "--thumb" in sys.argv

    # Load binary data into memory
    with open(binary_file, 'rb') as f:
        data = f.read()

    # Create memory with sufficient size and load the binary data
    memory_size = max(len(data) + 1024, 4096)  # Ensure enough space
    mem = Memory(memory_size)
    mem.load(data, 0)  # Load binary data starting at address 0

    cpu = CPU(mem)      # Pass memory to CPU
    
    # Set the appropriate mode
    if thumb_mode:
        cpu.thumb_mode = True
        print("Running in Thumb mode")
    else:
        cpu.thumb_mode = False
        print("Running in ARM mode")
    
    # Initialize PC to 0 (start of program)
    cpu.registers.set_pc(0)

    print(f"Loading binary file: {binary_file}")
    print(f"Binary size: {len(data)} bytes")
    print(f"Memory size: {memory_size} bytes")
    print(f"Initial PC: {cpu.registers.get_pc()}")
    print("Starting CPU execution...\n")

    # Read first few instructions to verify they loaded correctly
    if thumb_mode:
        print("First few Thumb instructions in memory:")
        for i in range(0, min(len(data), 16), 2):
            instr = mem.read_byte(i) | (mem.read_byte(i+1) << 8)
            print(f"Address {i:04x}: {instr:04x}")
    else:
        print("First few ARM instructions in memory:")
        for i in range(0, min(len(data), 16), 4):
            instr = mem.read_word(i)
            print(f"Address {i:04x}: {instr:08x}")
    print()

    cpu.run()

if __name__ == "__main__":
    main()
