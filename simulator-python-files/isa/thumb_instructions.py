# isa/thumb_instructions.py

def decode_thumb_instruction(instruction, pc=0):
    """
    Decode 16-bit Thumb instructions according to ARMv7 Thumb instruction set
    """
    
    # Check specific patterns first before general ones
    
    # Thumb ADD/SUB register format (these need to be checked before Format 2)
    # 0x1C__ = ADD Rd, Rm 
    if (instruction & 0xFF00) == 0x1C00:
        rm = (instruction >> 3) & 0x7
        rd = instruction & 0x7
        return {
            "mnemonic": "ADD",
            "operands": [f"R{rd}", f"R{rm}"],
            "type": "DP"
        }
    
    # 0x1A__ = SUB Rd, Rm patterns
    elif (instruction & 0xFF00) == 0x1A00:
        rm = (instruction >> 3) & 0x7
        rd = instruction & 0x7
        if rm == rd:  # SUB Rd, Rd (essentially clear register)
            return {
                "mnemonic": "SUB",
                "operands": [f"R{rd}", f"R{rd}"],
                "type": "DP"
            }
        else:
            return {
                "mnemonic": "SUB", 
                "operands": [f"R{rd}", f"R{rm}"],
                "type": "DP"
            }
    
    # 0x18__ = ADD Rd, Rm patterns
    elif (instruction & 0xFF00) == 0x1800:
        rm = (instruction >> 3) & 0x7
        rd = instruction & 0x7
        return {
            "mnemonic": "ADD",
            "operands": [f"R{rd}", f"R{rm}"],
            "type": "DP"
        }
    
    # 0x19__ = ADD with different register patterns
    elif (instruction & 0xFF00) == 0x1900:
        rm = (instruction >> 3) & 0x7
        rd = instruction & 0x7
        return {
            "mnemonic": "ADD",
            "operands": [f"R{rd}", f"R{rm}"],
            "type": "DP"
        }
    
    # Shift immediate (Format 1)
    elif (instruction & 0xE000) == 0x0000:
        op = (instruction >> 11) & 0x3
        imm5 = (instruction >> 6) & 0x1F
        rm = (instruction >> 3) & 0x7
        rd = instruction & 0x7
        
        if op == 0x0:  # LSL
            return {
                "mnemonic": "LSL" if imm5 != 0 else "MOV",
                "operands": [f"R{rd}", f"R{rm}"] + ([f"#{imm5}"] if imm5 != 0 else []),
                "type": "DP"
            }
        elif op == 0x1:  # LSR
            return {
                "mnemonic": "LSR",
                "operands": [f"R{rd}", f"R{rm}", f"#{imm5 if imm5 != 0 else 32}"],
                "type": "DP"
            }
        elif op == 0x2:  # ASR
            return {
                "mnemonic": "ASR",
                "operands": [f"R{rd}", f"R{rm}", f"#{imm5 if imm5 != 0 else 32}"],
                "type": "DP"
            }
    
    # Add/subtract (Format 2)
    elif (instruction & 0xF800) == 0x1800:
        op = (instruction >> 9) & 0x1
        i_bit = (instruction >> 10) & 0x1
        rn_imm = (instruction >> 6) & 0x7
        rm = (instruction >> 3) & 0x7
        rd = instruction & 0x7
        
        if op == 0:  # ADD
            if i_bit == 0:  # Register
                return {
                    "mnemonic": "ADD",
                    "operands": [f"R{rd}", f"R{rm}", f"R{rn_imm}"],
                    "type": "DP"
                }
            else:  # Immediate
                return {
                    "mnemonic": "ADD",
                    "operands": [f"R{rd}", f"R{rm}", f"#{rn_imm}"],
                    "type": "DP"
                }
        else:  # SUB
            if i_bit == 0:  # Register
                return {
                    "mnemonic": "SUB",
                    "operands": [f"R{rd}", f"R{rm}", f"R{rn_imm}"],
                    "type": "DP"
                }
            else:  # Immediate
                return {
                    "mnemonic": "SUB",
                    "operands": [f"R{rd}", f"R{rm}", f"#{rn_imm}"],
                    "type": "DP"
                }
    
    # Special handling for Thumb register-to-register ADD (Format 4 style)
    elif (instruction & 0xFE00) == 0x1C00:  # ADD Rd, Rm (0x1C__)
        rm = (instruction >> 3) & 0x7
        rd = instruction & 0x7
        return {
            "mnemonic": "ADD",
            "operands": [f"R{rd}", f"R{rm}"],
            "type": "DP"
        }
    
    # Special handling for Thumb register-to-register SUB (Format 4 style)  
    elif (instruction & 0xFE00) == 0x1A00:  # SUB Rd, Rm (0x1A__)
        rm = (instruction >> 3) & 0x7
        rd = instruction & 0x7
        return {
            "mnemonic": "SUB",
            "operands": [f"R{rd}", f"R{rm}"],
            "type": "DP"
        }
    
    # Move/compare/add/subtract immediate (Format 3)
    elif (instruction & 0xE000) == 0x2000:
        op = (instruction >> 11) & 0x3
        rd = (instruction >> 8) & 0x7
        imm8 = instruction & 0xFF
        
        opcodes = ["MOV", "CMP", "ADD", "SUB"]
        mnemonic = opcodes[op]
        
        if op == 0:  # MOV
            return {
                "mnemonic": mnemonic,
                "operands": [f"R{rd}", f"#{imm8}"],
                "type": "DP"
            }
        elif op == 1:  # CMP
            return {
                "mnemonic": mnemonic,
                "operands": [f"R{rd}", f"#{imm8}"],
                "type": "DP"
            }
        else:  # ADD/SUB
            return {
                "mnemonic": mnemonic,
                "operands": [f"R{rd}", f"R{rd}", f"#{imm8}"],
                "type": "DP"
            }
    
    # ALU operations (Format 4)
    elif (instruction & 0xFC00) == 0x4000:
        op = (instruction >> 6) & 0xF
        rm = (instruction >> 3) & 0x7
        rd = instruction & 0x7
        
        opcodes = [
            "AND", "EOR", "LSL", "LSR", "ASR", "ADC", "SBC", "ROR",
            "TST", "NEG", "CMP", "CMN", "ORR", "MUL", "BIC", "MVN"
        ]
        
        mnemonic = opcodes[op]
        
        if mnemonic in ["TST", "CMP", "CMN"]:
            return {
                "mnemonic": mnemonic,
                "operands": [f"R{rd}", f"R{rm}"],
                "type": "DP"
            }
        elif mnemonic == "NEG":
            return {
                "mnemonic": mnemonic,
                "operands": [f"R{rd}", f"R{rm}"],
                "type": "DP"
            }
        else:
            return {
                "mnemonic": mnemonic,
                "operands": [f"R{rd}", f"R{rm}"],
                "type": "DP"
            }
    
    # Hi register operations/branch exchange (Format 5)
    elif (instruction & 0xFC00) == 0x4400:
        op = (instruction >> 8) & 0x3
        h1 = (instruction >> 7) & 0x1
        h2 = (instruction >> 6) & 0x1
        rm_rd = instruction & 0x7
        
        rd = rm_rd + (h1 << 3)
        rm = rm_rd + (h2 << 3)
        
        if op == 0:  # ADD
            return {
                "mnemonic": "ADD",
                "operands": [f"R{rd}", f"R{rm}"],
                "type": "DP"
            }
        elif op == 1:  # CMP
            return {
                "mnemonic": "CMP",
                "operands": [f"R{rd}", f"R{rm}"],
                "type": "DP"
            }
        elif op == 2:  # MOV
            return {
                "mnemonic": "MOV",
                "operands": [f"R{rd}", f"R{rm}"],
                "type": "DP"
            }
        elif op == 3:  # BX/BLX
            return {
                "mnemonic": "BX",
                "operands": [f"R{rm}"],
                "type": "BRANCH"
            }
    
    # Load PC-relative (Format 6)
    elif (instruction & 0xF800) == 0x4800:
        rd = (instruction >> 8) & 0x7
        imm8 = instruction & 0xFF
        address = (pc & 0xFFFFFFFC) + 4 + (imm8 << 2)
        
        return {
            "mnemonic": "LDR",
            "operands": [f"R{rd}", f"[PC, #{imm8 << 2}]"],
            "type": "LOAD"
        }
    
    # Load/store register offset (Format 7)
    elif (instruction & 0xF200) == 0x5000:
        l_bit = (instruction >> 11) & 0x1
        b_bit = (instruction >> 10) & 0x1
        ro = (instruction >> 6) & 0x7
        rb = (instruction >> 3) & 0x7
        rd = instruction & 0x7
        
        if l_bit == 0:  # Store
            if b_bit == 0:  # STR
                return {
                    "mnemonic": "STR",
                    "operands": [f"R{rd}", f"[R{rb}, R{ro}]"],
                    "type": "STORE"
                }
            else:  # STRB
                return {
                    "mnemonic": "STRB",
                    "operands": [f"R{rd}", f"[R{rb}, R{ro}]"],
                    "type": "STORE"
                }
        else:  # Load
            if b_bit == 0:  # LDR
                return {
                    "mnemonic": "LDR",
                    "operands": [f"R{rd}", f"[R{rb}, R{ro}]"],
                    "type": "LOAD"
                }
            else:  # LDRB
                return {
                    "mnemonic": "LDRB",
                    "operands": [f"R{rd}", f"[R{rb}, R{ro}]"],
                    "type": "LOAD"
                }
    
    # Load/store immediate offset (Format 9)
    elif (instruction & 0xE000) == 0x6000:
        b_bit = (instruction >> 12) & 0x1
        l_bit = (instruction >> 11) & 0x1
        imm5 = (instruction >> 6) & 0x1F
        rb = (instruction >> 3) & 0x7
        rd = instruction & 0x7
        
        if b_bit == 0:  # Word
            offset = imm5 << 2
            if l_bit == 0:  # STR
                return {
                    "mnemonic": "STR",
                    "operands": [f"R{rd}", f"[R{rb}, #{offset}]"],
                    "type": "STORE"
                }
            else:  # LDR
                return {
                    "mnemonic": "LDR",
                    "operands": [f"R{rd}", f"[R{rb}, #{offset}]"],
                    "type": "LOAD"
                }
        else:  # Byte
            if l_bit == 0:  # STRB
                return {
                    "mnemonic": "STRB",
                    "operands": [f"R{rd}", f"[R{rb}, #{imm5}]"],
                    "type": "STORE"
                }
            else:  # LDRB
                return {
                    "mnemonic": "LDRB",
                    "operands": [f"R{rd}", f"[R{rb}, #{imm5}]"],
                    "type": "LOAD"
                }
    
    # Conditional branch (Format 16)
    elif (instruction & 0xF000) == 0xD000:
        cond = (instruction >> 8) & 0xF
        imm8 = instruction & 0xFF
        # Sign extend
        if imm8 & 0x80:
            offset = (imm8 | 0xFFFFFF00) << 1
        else:
            offset = imm8 << 1
        
        conditions = [
            "EQ", "NE", "CS", "CC", "MI", "PL", "VS", "VC",
            "HI", "LS", "GE", "LT", "GT", "LE", "AL", "NV"
        ]
        
        return {
            "mnemonic": f"B{conditions[cond]}",
            "operands": [f"#{offset}"],
            "type": "BRANCH"
        }
    
    # Unconditional branch (Format 18)
    elif (instruction & 0xF800) == 0xE000:
        imm11 = instruction & 0x7FF
        # Sign extend
        if imm11 & 0x400:
            offset = (imm11 | 0xFFFFF800) << 1
        else:
            offset = imm11 << 1
        
        return {
            "mnemonic": "B",
            "operands": [f"#{offset}"],
            "type": "BRANCH"
        }
    
    # NOP (Special case)
    elif instruction == 0x46C0:  # MOV R8, R8
        return {
            "mnemonic": "NOP",
            "operands": [],
            "type": "MISC"
        }
    
    # Unknown instruction
    return {
        "mnemonic": "UNKNOWN",
        "operands": [],
        "type": "UNKNOWN"
    }
