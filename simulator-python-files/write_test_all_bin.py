with open("test_all.bin", "wb") as f:
    # 5 ARM instructions
    f.write(bytes.fromhex("0100A0E3"))  # MOV R0, #1
    f.write(bytes.fromhex("001080E0"))  # ADD R1, R0, R0
    f.write(bytes.fromhex("012041E0"))  # SUB R2, R1, R1
    f.write(bytes.fromhex("0230A0E1"))  # MOV R3, R2
    f.write(bytes.fromhex("034082E0"))  # ADD R4, R2, R3

    # 10 Thumb instructions (little endian)
    f.write(bytes.fromhex("0120"))  # MOVS R0, #1
    f.write(bytes.fromhex("0231"))  # ADDS R1, #2
    f.write(bytes.fromhex("013A"))  # SUBS R2, #1
    f.write(bytes.fromhex("0423"))  # MOVS R3, #4
    f.write(bytes.fromhex("1C1C"))  # ADD R4, R3
    f.write(bytes.fromhex("151A"))  # SUB R5, R2
    f.write(bytes.fromhex("2E1C"))  # ADD R6, R5
    f.write(bytes.fromhex("3F1A"))  # SUB R7, R6
    f.write(bytes.fromhex("0824"))  # MOVS R4, #8
    f.write(bytes.fromhex("1025"))  # MOVS R5, #16
