with open("test_thumb.bin", "wb") as f:
    # Format: little endian 16-bit
    # MOVS R0, #1 => 0x2001
    f.write(bytes.fromhex("0120"))
    # ADDS R1, R0, #2 => 0x3102
    f.write(bytes.fromhex("0231"))
    # SUBS R2, R1, #1 => 0x3A01
    f.write(bytes.fromhex("013A"))
    # MOVS R3, #4 => 0x2304
    f.write(bytes.fromhex("0423"))
    # ADDS R4, R3 => 0x1C1C
    f.write(bytes.fromhex("1C1C"))
    # SUBS R5, R2 => 0x1A15
    f.write(bytes.fromhex("151A"))
    # ADDS R6, R5 => 0x1C2E
    f.write(bytes.fromhex("2E1C"))
    # SUBS R7, R6 => 0x1A3F
    f.write(bytes.fromhex("3F1A"))
    # MOVS R4, #8 => 0x2408
    f.write(bytes.fromhex("0824"))
    # MOVS R5, #16 => 0x2510
    f.write(bytes.fromhex("1025"))
    # MOVS R6, #32 => 0x2632
    f.write(bytes.fromhex("3226"))
    # ADD R0, R4 => 0x1800
    f.write(bytes.fromhex("0018"))
    # ADD R1, R5 => 0x1909
    f.write(bytes.fromhex("0919"))
    # SUB R2, R6 => 0x1A12
    f.write(bytes.fromhex("121A"))
    # ADD R3, R0 => 0x1818
    f.write(bytes.fromhex("1818"))
