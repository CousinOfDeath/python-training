import datetime


class Person:
    def __init__(self, first_name, last_name, year):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def age(self):
        """Use datetime module"""
        return datetime.date.today().year - self.year

    def __str__(self):
        return f"{self.full_name()} is {self.age()} years old"


class Employee(Person):
    def __init__(self, first_name, last_name, year, company_name, social_security_number):
        super().__init__(first_name, last_name, year)
        self.company_name = company_name
        self.social_security_number = social_security_number

    def __str__(self):
        return f"{super().__str__()}, {self.company_name}, {self.social_security_number}"


p = Person("Cousin", "Death", 1982)
e = Employee("Second", "Cousin", 1999, "D´vil", "010199-1234")

print(p)
print(e)