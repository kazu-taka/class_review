class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age < 20:
            return 1000

        if 20 <= self.age < 65:
            return 1500

        if 65 <= self.age:
            return 1200


# B-1
# ken = Customer(first_name="Ken", family_name="Tanaka")
# print(ken.full_name())
#
# tom = Customer(first_name="Tom", family_name="Ford")
# print(tom.full_name())

# B-2
# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# print(ken.age)  # 15 という値を返す
#
# tom = Customer(first_name="Tom", family_name="Ford", age=57)
# print(tom.age)  # 57 という値を返す
#
# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# print(ieyasu.age)  # 73 という値を返す

# B-3
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.entry_fee())  # 1000 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.entry_fee())  # 1500 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.entry_fee())  # 1200 という値を返す
