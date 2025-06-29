# write_test_bin.py
with open("test.bin", "wb") as f:
    f.write((1).to_bytes(4, 'little'))  # MOV R0, #1
    f.write((2).to_bytes(4, 'little'))  # ADD R1, R0, #1
    f.write((3).to_bytes(4, 'little'))  # SUB R2, R1, #1
    f.write((0).to_bytes(4, 'little'))  # HALT (NOP)
