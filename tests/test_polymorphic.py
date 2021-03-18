import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from polymorphic_type import *

class TestMyType(unittest.TestCase):
    def test_basic(self):
        mytype=MyType("constante",["Int"])
        response=str(mytype)
        self.assertEqual('Int',response)

    def test_constante(self):
        init=PolymorphicType()
        response=init.assign_type(["1","Int"])
        self.assertEqual(response,0)

    def test_variable(self):
        init=PolymorphicType()
        response=init.assign_type(["1","a"])
        self.assertEqual(response,0)

    def test_funcion(self):
        init=PolymorphicType()
        response=init.assign_type(["eq","a","->","Bool"])
        self.assertEqual(response,0)

    def test_parentizado(self):
        init=PolymorphicType()
        response=init.assign_type(["eq","(","a","->","a",")","->","Bool"])
        self.assertEqual(response,0)

    def test_parentizado2(self):
        init=PolymorphicType()
        response=init.assign_type(["eq","(","(","a","->","Bool",")","->","Int",")","->","Bool"])
        self.assertEqual(response,0)

    def test_parentizado3(self):
        init=PolymorphicType()
        response=init.assign_type(["eq","(","(","a","->","Bool",")","->","Int",")","->","(","a","->","Bool",")"])
        self.assertEqual(response,0)

    def test_without_parentizado(self):
        init=PolymorphicType()
        response=init.assign_type(["eq","a","->","Bool","->","Int","->","a","->","Bool"])
        self.assertEqual(response,0)

    # def test_print(self):
    #     init=PolymorphicType()
    #     response=init.assign_type(["1","Int"])
    #     response=init.assign_type(["eq","a","->","Bool","->","Int"])
    #     response=init.assign_type(["eq","a","->","a","->","Bool"])
    #     response=init.print_type(["eq","1"])
    #     self.assertEqual(response,"['funcion', [['constante', ['Int']], ['funcion', [['constante', ['Int']], ['constante', ['Bool']]]]]]")



class TestMemory(unittest.TestCase):
    def test_basic(self):
        my_memory=Memory()
        response=str(my_memory)
        self.assertEqual('[]',response)

    def test_basic_2(self):
        my_memory=Memory()
        mytype=MyType("constante",["Int"])
        my_memory.add("1",mytype)
        response=str(my_memory)
        self.assertEqual('[["1", ["constante", ["Int"]]]]',response)



if __name__ == "__main__":
    unittest.main()