

from abc import ABC, abstractmethod

class Employee(ABC):
    def doJob(self):
        pass

class Manager(Employee):
    def doJob(self):
        print("Managers Job.....")

class Developer(Employee):

    def doJob(self):
        print("Coding Job...." )

def BankFun(emps):           # polymorphism
    print("Bank Job Strated......".center(60,"-"))
    for emp in emps:
        emp.doJob()
    print("Bank job Completed.....".center(60, "-"))
    print("-" * 60)

mike = Manager()
david = Developer()

BankFun([mike, david])

