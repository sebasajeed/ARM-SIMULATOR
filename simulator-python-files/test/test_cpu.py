# test/test_cpu.py

import unittest
from memory.memory import Memory
from cpu.register_file import RegisterFile

class TestRegisters(unittest.TestCase):
    def test_set_get(self):
        r = RegisterFile()
        r.set(1, 0xDEADBEEF)
        self.assertEqual(r.get(1), 0xDEADBEEF & 0xFFFFFFFF)
        r.set_flag('Z', 1)
        self.assertEqual(r.get_flag('Z'), 1)

if __name__ == "__main__":
    unittest.main()
