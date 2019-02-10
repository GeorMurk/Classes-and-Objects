#!/usr/bin/python

#!Creating Classes and Objects

class Employee:

    def __init__(self, name, department, position, is_on_leave):
        self.name = name
        self.department = department
        self.position = position
        self.is_on_leave = is_on_leave

#!Creating an object this data should be on a different file

from "python file" import Employee

employee1 = Employee("Nick", "Engineering", "Senior_Engineer", False)
employee2 = Employee("Ivy", "Human Resource", "Customer Service", True)


print(employee1)
print(employee2)


#!Go ahead and test it out!!!
