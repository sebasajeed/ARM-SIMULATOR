# test/test_memory.py

import unittest
from memory.memory import Memory

class TestMemory(unittest.TestCase):
    def test_byte(self):
        m = Memory(64)
        m.write_byte(10, 0xAB)
        self.assertEqual(m.read_byte(10), 0xAB)

    def test_word(self):
        m = Memory(64)
        m.write_word(4, 0x12345678)
        self.assertEqual(m.read_word(4), 0x12345678)
        
    def test_memory_initialization(self):
        m = Memory(32)
        # Test that memory is initialized to zeros
        self.assertEqual(m.read_byte(0), 0)
        self.assertEqual(m.read_word(0), 0)

if __name__ == "__main__":
    unittest.main()
