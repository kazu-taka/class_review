class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age <= 3:
            return 0

        if self.age < 20:
            return 1000

        if 20 <= self.age < 65:
            return 1500

        if 65 <= self.age < 75:
            return 1200

        if 75 <= self.age:
            return 500

    def info(self, delimiter=","):
        return f"{self.full_name()}{delimiter}{self.age}{delimiter}{self.entry_fee()}"


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
# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# print(ken.entry_fee())  # 1000 という値を返す
#
# tom = Customer(first_name="Tom", family_name="Ford", age=57)
# print(tom.entry_fee())  # 1500 という値を返す
#
# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# print(ieyasu.entry_fee())  # 1200 という値を返す

# B-4
# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を返す
#
# tom = Customer(first_name="Tom", family_name="Ford", age=57)
# print(ken.info_csv())  # "Tom Ford,57,1500" という値を返す
#
# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# print(ieyasu.info_csv())  # "Ieyasu Tokugawa,73,1200" という値を返す

# B-5
# mike = Customer(first_name="Mike", family_name="Suzuki", age=3)
# print(mike.entry_fee())

# B-6
# jiro = Customer(first_name="Jiro", family_name="Sasaki", age=75)
# print(jiro.entry_fee())

# B-7
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.info("\t"))  # "Ken Tanaka,15,1000" という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(ken.info("\t"))  # "Tom Ford,57,1500" という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.info("\t"))
