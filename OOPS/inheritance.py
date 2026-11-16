"""
Inheritance->its the concepts in which one class acquires the properties and methods into another class.
First class is called as -> parent,base,super
Second class called as->child,sub,derived class,inherited class(a child class can re-use the code of the parent class without writing its again
"""

class Parent:
    networth ="10 crore"

    def skill(self):
        print("Teaching skill")

class Child(Parent):
    def job(self, job_title):
        print(f"My job title is {job_title}")

c = Child()
c.skill()
c.job("HR")
print(c.networth)

"""
Types of inheritance->
1.Single inheritance->one parent-one child
2.Multiple inheritance->Different parent class and 1 child class
3.Multi-level inheritance->A child becomes parent class for another class.
4.hierarchial inheritance->Single parent and differnt child.
5.Hybrid inheritance->Combination of two or more types inheritance.
"""

#multiple inheritance.

class A:
    pass
class B:
    pass
class C(A,B): #child class
    pass

c=C()

#Multi-level inheritance
class A:
    pass
class B(A):
    pass
class C(B):
    pass

c= C()

#hierarchial inheritance
class Parent():
    def display(self):
        print("Parent method: ")
class Child1(Parent):
    pass
class Child2(Parent):
    pass

c1=Child1()
c1.display()
c2=Child2()
c2.display()