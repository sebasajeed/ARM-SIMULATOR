# test/test_decoder.py

import unittest
from isa.decoder import decode_instruction

class TestDecoder(unittest.TestCase):
    def test_nop(self):
        instr = decode_instruction(0)
        self.assertEqual(instr['mnemonic'], 'NOP')

    def test_mov_stub(self):
        instr = decode_instruction(0xFF)
        self.assertEqual(instr['mnemonic'], 'MOV')

if __name__ == "__main__":
    unittest.main()
