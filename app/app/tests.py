"""
sample test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
     """testing the calc module"""
     def test_add_nmbers(self):
          """testing add function"""
          res=calc.add(5,6)
          
          #check if it is equal
          self.assertEqual(res,11)
          
     def test_substract_numbers(self):
          """creating the test for substract functionality TDD"""
          res=calc.substract(16,8)
          
          self.assertEqual(res,8)