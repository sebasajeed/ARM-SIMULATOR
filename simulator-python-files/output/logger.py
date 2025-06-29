# output/logger.py

def log_instruction(pc, word, instr):
    ops = ", ".join(str(o) for o in instr['operands'])
    print(f"PC={pc:08X} 0x{word:08X}  {instr['mnemonic']} {ops}")

def log_registers(regs):
    regs.dump()

def debug(msg):
    print(f"[DEBUG] {msg}")

def error(msg):
    print(f"[ERROR] {msg}")
