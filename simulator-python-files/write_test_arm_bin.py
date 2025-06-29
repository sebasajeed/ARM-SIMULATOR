with open("test_arm.bin", "wb") as f:
    # MOV R0, #1 => E3A00001
    f.write(bytes.fromhex("0100A0E3"))
    # ADD R1, R0, R0 => E0801000
    f.write(bytes.fromhex("001080E0"))
    # SUB R2, R1, R1 => E0412001
    f.write(bytes.fromhex("012041E0"))
    # MOV R3, R2 => E1A03002
    f.write(bytes.fromhex("0230A0E1"))
    # ADD R4, R2, R3 => E0824003
    f.write(bytes.fromhex("034082E0"))
    # SUB R5, R4, R0 => E0445000
    f.write(bytes.fromhex("005044E0"))
    # MOV R6, R5 => E1A06005
    f.write(bytes.fromhex("0560A0E1"))
    # ADD R7, R6, R6 => E0867006
    f.write(bytes.fromhex("067086E0"))
    # SUB R8, R7, R1 => E0478001
    f.write(bytes.fromhex("018047E0"))
    # MOV R9, R8 => E1A09008
    f.write(bytes.fromhex("0890A0E1"))
    # ADD R10, R9, R9 => E089A009
    f.write(bytes.fromhex("0990A9E0"))
    # SUB R11, R10, R0 => E05B000A
    f.write(bytes.fromhex("0A005BE0"))
    # MOV R12, R11 => E1A0C00B
    f.write(bytes.fromhex("0BC0A0E1"))
    # ADD R0, R12, R1 => E08C0001
    f.write(bytes.fromhex("01008CE0"))
    # SUB R1, R0, R2 => E0401002
    f.write(bytes.fromhex("021040E0"))
