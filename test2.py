class Person:

    def __init__(self, name, surname, emailid, year_of_birth):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth

    def age(self, current_year):
        return curent_year - self.year_of_birth


maziya = Person("maziya", "tabassum", "maziya@gmail.com", 1998)
print(maziya.name)
print(maziya.age(2022))