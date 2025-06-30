# test/test_memory.py

import unittest
from memory.memory import Memory

class TestMemory(unittest.TestCase):
    def test_byte(self):
        m = Memory(64)
        m.store_byte(10, 0xAB)
        self.assertEqual(m.load_byte(10), 0xAB)

    def test_word(self):
        m = Memory(64)
        m.store_word(4, 0x12345678)
        self.assertEqual(m.load_word(4), 0x12345678)

if __name__ == "__main__":
    unittest.main()
