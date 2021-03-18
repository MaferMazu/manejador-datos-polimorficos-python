import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from my_type import *

class TestMyType(unittest.TestCase):
    def test_basic(self):
        mytype=MyType("constante",["Int"])
        response=str(mytype)
        self.assertEqual('Int',str(response))

    def test_constante(self):
        response,error=read_type(["1","Int"])
        self.assertEqual('Int',str(response))

    def test_variable(self):
        response,error=read_type(["1","a"])
        self.assertEqual(str(response),"a")

    def test_funcion(self):
        response,error=read_type(["a","->","Bool"])
        self.assertEqual(str(response),"a -> Bool")

    def test_parentizado(self):
        response,error=read_type(["(","a","->","a",")","->","Bool"])
        self.assertEqual(str(response),"(a -> a) -> Bool")

    def test_parentizado2(self):
        response,error=read_type(["(","(","a","->","Bool",")","->","Int",")","->","Bool"])
        self.assertEqual(str(response),"(a -> (Bool -> Int)) -> Bool")

    def test_parentizado3(self):
        response,error=read_type(["(","(","a","->","Bool",")","->","Int",")","->","(","a","->","Bool",")"])
        self.assertEqual(str(response),"(a -> (Bool -> Int)) -> (a -> Bool)")

    def test_without_parentizado(self):
        response,error=read_type(["a","->","Bool","->","Int","->","a","->","Bool"])
        self.assertEqual(str(response),"a -> (Bool -> (Int -> (a -> Bool)))")


if __name__ == "__main__":
    unittest.main()