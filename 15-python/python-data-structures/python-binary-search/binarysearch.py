import math
import unittest

def binary_search(array, value):
  if len(array) == 0:
    return -1
    
  low = 0
  high = len(array) - 1
  while not low > high:
    index = math.floor((low + high) / 2)
    # print(f'low: {low} high: {high} index: {index} {array} {value}')
    if array[index] == value:
      return index
    elif array[index] < value:
      low = index + 1
    elif array[index] > value:
      high = index - 1
      
  # The value wasn't found. Return the last index we were looking at.
  # Turn the last index into a negative number to indicate that it wasn't
  # found. Any index that returns negative means "value was not found." Add
  # +1 to the index before turning it negative to account for index zero.
  # | item found? | last index? | returned_index |
  # | =========== | =========== | ============== |
  # |     no      |     5       |      -6        |
  # |     no      |     1       |      -2        |
  # |     no      |     0       |      -1        |
  # |     yes     |     0       |       0        |
  # |     yes     |     1       |       1        |
  # |     yes     |     5       |       5        |
  # uhh.. it turns out returning the indexes like that is hard.
  # result = -(index + 1)
  # print(f'index: {index} result: {result}')
  # return result
  return -1
  
class BinarySearchTest(unittest.TestCase):
  def setUp(self):
    self.a0 = []
    self.a1 = [6]
    self.a2 = [2, 8]
    self.a3 = [2, 8, 17]
    self.aMany = [2, 8, 14, 34, 74, 87, 99, 120]

  def test_a0_not_there_low(self):
    index = binary_search(self.a0, -50)
    self.assertEqual(index, -1)
  
  def test_a0_not_there_high(self):
    index = binary_search(self.a0, 50)
    self.assertEqual(index, -1)

  def test_a1_exists(self):
    index = binary_search(self.a1, 6)
    self.assertEqual(index, 0)
    
  def test_a1_not_there_low(self):
    index = binary_search(self.a1, 3)
    self.assertEqual(index, -1)
  
  def test_a1_not_there_high(self):
    index = binary_search(self.a1, 10)
    self.assertEqual(index, -1)
    
  def test_amany_not_there(self):
    self.assertEqual(binary_search(self.aMany, -50), -1)
    self.assertEqual(binary_search(self.aMany, 10), -1)
    self.assertEqual(binary_search(self.aMany, 40), -1)
    self.assertEqual(binary_search(self.aMany, 119), -1)
    self.assertEqual(binary_search(self.aMany, 999), -1)
      
  def test_amany_exists(self):
    self.assertEqual(binary_search(self.aMany, 2), 0)
    self.assertEqual(binary_search(self.aMany, 2), 0)
    self.assertEqual(binary_search(self.aMany, 74), 4)
    self.assertEqual(binary_search(self.aMany, 120), len(self.aMany) - 1)

unittest.main()
