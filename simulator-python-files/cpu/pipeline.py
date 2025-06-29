# cpu/pipeline.py

class Pipeline:
    def __init__(self):
        self.IF = None
        self.ID = None
        self.EX = None
        self.MEM = None
        self.WB = None

    def advance(self, new_instr):
        self.WB = self.MEM
        self.MEM = self.EX
        self.EX = self.ID
        self.ID = self.IF
        self.IF = new_instr

    def dump(self):
        print("Pipeline stages:")
        print("  IF  =", self.IF)
        print("  ID  =", self.ID)
        print("  EX  =", self.EX)
        print("  MEM =", self.MEM)
        print("  WB  =", self.WB)

