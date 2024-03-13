class ShittyDb:
    def __init__(self):
        self.data = {}

    def create(self, key, val):
        if key in self.data:
            raise Exception("Key already exists")
        self.data[key] = val

    def read(self, key):
        if key not in self.data:
            raise Exception("Key not found")
        self.data[key]

    def update(self, key, val):
        if key not in self.data:
            raise Exception("Key not found")
        self.data[key] = val

    def delete(self, key):
        if key not in self.data:
            raise Exception("Key not found")
        self.data.pop(key)

