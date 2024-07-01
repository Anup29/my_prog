class UpdateDict(dict):
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError("Key already exists..")
        super().__setitem__(key, value)


x = UpdateDict()
print(x)
x["a"] = 15
print(x)
x["a"] = 16
print(x)