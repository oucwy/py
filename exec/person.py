# Author: Wang Yong
# Date: 2024.2.24
# Description: class and constructor in python

# List of people
# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 30},
#     {"name": "Charlie", "age": 35},
# ]

# # Print name and age of each person
# for person in people:
#     print(f"Name: {person['name']}, Age: {person['age']}")


# Python

class Person:
    # Constructor
    def __init__(self, name, salary, rank):
        self.name = name
        self._salary = salary  # salary is private
        self.__rank = rank

    def get_salary(self):
        return self._salary
    
    def get_rank(self):
        return self.__rank
        

# List of people
people = [
    Person("Alice", 2500, 170),
    Person("Bob", 3000, 180),
    Person("王老师", 3500, 175),
]

# Print name and age of each person
for person in people:
    print(f"{person.name}好, 等级{person.get_rank()}, 年终奖{person._salary}元已发，请查收。祝假期愉快[庆祝][庆祝]")