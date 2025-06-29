# write_test_bin.py

# This will write 4 real ARM instructions into test.bin:
# MOV R0, #1
# ADD R1, R0, R0
# SUB R2, R1, R1
# NOP (MOV R0, R0)

with open("test.bin", "wb") as f:
    f.write((0xE3A00001).to_bytes(4, byteorder='little'))  # MOV R0, #1
    f.write((0xE0801000).to_bytes(4, byteorder='little'))  # ADD R1, R0, R0
    f.write((0xE0412001).to_bytes(4, byteorder='little'))  # SUB R2, R1, R1
    f.write((0xE1A00000).to_bytes(4, byteorder='little'))  # NOP (MOV R0, R0)
