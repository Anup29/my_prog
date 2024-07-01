class School:
    sch_name = "ABCS"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_val(self):
        return f"Name: {self.name}, Age: {self.age}"

    def set_name(self, name):
        self.name = name

    @classmethod
    def class_method(cls, data_str):
        name, age = data_str.split("-")
        return cls(name, age)

    @staticmethod
    def static_method():
        print("This is static method")

    def __add__(self, other):
        con_name = self.name + other.name
        tot_age = self.age + int(other.age)
        return School(con_name,tot_age)

    def __str__(self,other):
        return f"{self.name+other.name} {self.age+other.age}"

ob = School("WER", 20)
ob2 = School("REW", 40)

print(ob.get_val())
ob.set_name("RRR")
print(ob.get_val())
print(ob.static_method())

ob1 = School.class_method("TTT-30")
print(ob1.__dict__)
print(ob1.get_val())
ob3 = ob + ob1
print(ob3.get_val())
print(ob+ob2)