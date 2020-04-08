class Cat:
    def __int__(self, name, age):
        self.name = name
        self.age = age

smokey = Cat('smokey', 10)
tom = Cat('tom', 11)
bella = Cat('bella', 12)


def get_oldest_age(*args):
    return max(args)



print(f"The oldest cat is  {get_oldest_age(smokey.age,tom.age,bella.age)} years old")
