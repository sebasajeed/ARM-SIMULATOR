"""
execute(instr, operands, registers, memory)
TODO: flesh out each case. ayla
"""

class Executor:
    def execute(self, instr, operands, registers, memory=None):
        rd = operands.get('rd')
        rn = operands.get('rn')
        operand2 = operands.get('operand2')

        if instr == 'ADD':
            registers[rd] = registers[rn] + operand2
        elif instr == 'SUB':
            registers[rd] = registers[rn] - operand2
        elif instr == 'ORR':
            registers[rd] = registers[rn] | operand2
        elif instr == 'MOV':
            registers[rd] = operand2
        elif instr == 'LDR':
            addr = registers[rn] + operand2
            registers[rd] = memory.load(addr)
        elif instr == 'STR':
            addr = registers[rn] + operand2
            memory.store(addr, registers[rd])
        else:
            print(f"Unknown instruction: {instr}")