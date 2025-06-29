"""
Memory class: encapsulates a bytearray with load/store utilities.
TODO : implement load_word, store_word methods.
"""
class Memory:
	def __init__(self, size=1024):
		self.mem = bytearray(size) 

	def load(self, address):
		return (self.mem[address] | (self.mem[address+1] << 8)| (self.mem[address+2]<<16) | (self.mem[address+3]<<24))

	def store(self, address, value):
		self.mem[address] = value & 0xFF
		self.mem[address + 1] = (value >> 8) & 0xFF
		self.mem[address + 2] = (value >> 16) & 0xFF
		self.mem[address + 3] = (value >> 24) & 0xFF

	def load_word(self, address):
		return self.load(address)

	def store_word(self, address, value):
		self.store(address, value)

	def load_binary(self, path):
		with open(path, 'rb') as f:
			address = 0
			byte = f.read(1)
			while byte:
				self.mem[address] = byte[0]
				address += 1
				byte = f.read(1)
