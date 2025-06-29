class Memory:
    def __init__(self, size=1024):
        self.data = bytearray(size)

    def load_word(self, address):
        return int.from_bytes(self.data[address:address+4], 'little')

    def store_word(self, address, value):
        self.data[address:address+4] = value.to_bytes(4, 'little')

    def load_binary(self, filepath):
        with open(filepath, 'rb') as f:
            binary = f.read()
            self.data[0:len(binary)] = binary
