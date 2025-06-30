# test/test_decoder.py

import unittest
from isa.decoder import decode

class TestDecoder(unittest.TestCase):
    def test_unknown_instruction(self):
        # Test with invalid instruction
        instr = decode(0xFFFFFFFF, 0)
        self.assertEqual(instr['mnemonic'], 'UNKNOWN')
        self.assertEqual(instr['type'], 'INVALID')

    def test_decode_function_exists(self):
        # Test that decode function works with basic input
        instr = decode(0x00000000, 0)
        self.assertIn('mnemonic', instr)
        self.assertIn('operands', instr)

if __name__ == "__main__":
    unittest.main()
