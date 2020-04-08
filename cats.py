class Cat:
    def __int__(self, name, age):
        self.name = name
        self.age = age

max = Cat('smokey', 10)
tom = Cat('tom', 11)
bella = Cat('bella', 12)


def get_oldest_age(*args):
    return max(args)



print(f"The oldest cat is  {get_oldest_age(max.age,tom.age,bella.age)} years old")
