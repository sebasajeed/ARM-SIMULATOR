# test/test_cpu.py

import unittest
from memory.memory import Memory
from cpu.register_file import RegisterFile
from cpu.condition_flags import ConditionFlags

class TestRegisters(unittest.TestCase):
    def test_set_get(self):
        r = RegisterFile()
        r.set(1, 0xDEADBEEF)
        self.assertEqual(r.get(1), 0xDEADBEEF & 0xFFFFFFFF)
        
    def test_pc_operations(self):
        r = RegisterFile()
        r.set_pc(0x1000)
        self.assertEqual(r.get_pc(), 0x1000)
        
class TestConditionFlags(unittest.TestCase):
    def test_flags(self):
        flags = ConditionFlags()
        flags.Z = 1
        self.assertEqual(flags.Z, 1)
        self.assertTrue(flags.check_condition('EQ'))
        self.assertFalse(flags.check_condition('NE'))

if __name__ == "__main__":
    unittest.main()
