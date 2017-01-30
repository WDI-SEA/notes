# run with `python3 linkedlist-test.py`
import unittest
from linkedlist import *

class TestItem(unittest.TestCase):
  def setUp(self):
    self.n0 = ListNode(0)
    self.empty_list = LinkedList()
    
    self.l1 = LinkedList()
    self.l1.insert_in_front(1)
    
    self.l2 = LinkedList()
    self.l2.insert_in_front(2)
    self.l2.insert_in_front(1)
    
    self.l3 = LinkedList()
    self.l3.insert_in_front(3)
    self.l3.insert_in_front(2)
    self.l3.insert_in_front(1)
    
    self.l99 = LinkedList()
    for i in range(99, 0,-1):
      self.l99.insert_in_front(i)
    
  def test_list_node(self):
    self.assertEqual(self.n0.data, 0)
  
  # Empty tests
  def test_empty_list_is_empty(self):
    self.assertEqual(self.empty_list.is_empty(), True)
    self.assertEqual(len(self.empty_list), 0)
    
  def test_not_is_empty(self):
    self.assertEqual(self.l1.is_empty(), False)
    self.assertEqual(len(self.l1), 1)
    
    self.assertEqual(self.l2.is_empty(), False)
    self.assertEqual(len(self.l2), 2)
    
    self.assertEqual(self.l3.is_empty(), False)
    self.assertEqual(len(self.l3), 3)
    
    self.assertEqual(self.l99.is_empty(), False)
    self.assertEqual(len(self.l99), 99)
   
  # __str__ tests
  def test_str_empty_list(self):
    self.assertEqual(str(self.empty_list), "[]")
    self.assertEqual(len(self.empty_list), 0)
    
  def test_str_single_item_list(self):
    self.assertEqual(str(self.l1), "[1]")
    self.assertEqual(len(self.l1), 1)
  
  def test_str_two_item_list(self):
    self.assertEqual(str(self.l2), "[1 -> 2]")
    self.assertEqual(len(self.l2), 2)
  
  def test_str_three_item_list(self):
    self.assertEqual(str(self.l3), "[1 -> 2 -> 3]")
    self.assertEqual(len(self.l3), 3)
    
  def test_str_99_item_list(self):
    self.assertEqual(str(self.l99), "[1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32 -> 33 -> 34 -> 35 -> 36 -> 37 -> 38 -> 39 -> 40 -> 41 -> 42 -> 43 -> 44 -> 45 -> 46 -> 47 -> 48 -> 49 -> 50 -> 51 -> 52 -> 53 -> 54 -> 55 -> 56 -> 57 -> 58 -> 59 -> 60 -> 61 -> 62 -> 63 -> 64 -> 65 -> 66 -> 67 -> 68 -> 69 -> 70 -> 71 -> 72 -> 73 -> 74 -> 75 -> 76 -> 77 -> 78 -> 79 -> 80 -> 81 -> 82 -> 83 -> 84 -> 85 -> 86 -> 87 -> 88 -> 89 -> 90 -> 91 -> 92 -> 93 -> 94 -> 95 -> 96 -> 97 -> 98 -> 99]")
    self.assertEqual(len(self.l99), 99)
    
  def test_insert_in_front(self):
    self.empty_list.insert_in_front(1)
      
    self.l1.insert_in_front(0)
    self.l1.insert_in_front(0)
    self.l1.insert_in_front(0)
    self.l1.insert_in_front(0)
    
    self.assertEqual(str(self.empty_list), '[1]')
    self.assertEqual(str(self.l1), '[0 -> 0 -> 0 -> 0 -> 1]')
    self.assertEqual(len(self.l1), 5)
    
  def test_remove_front(self):
    self.assertFalse(self.empty_list.remove_front())
    self.l1.remove_front()
    self.assertEqual(str(self.l1), '[]')
    self.assertEqual(len(self.l1), 0)
    
    self.l2.remove_front()
    self.assertEqual(str(self.l2), '[2]')
    self.assertEqual(len(self.l2), 1)
    
    self.l3.remove_front()
    self.assertEqual(str(self.l3), '[2 -> 3]')
    self.assertEqual(len(self.l3), 2)
    
  def test_insert_at_end(self):
    self.empty_list.insert_at_end(98)
    self.assertEqual(str(self.empty_list), '[98]')
    self.assertEqual(len(self.empty_list), 1)
    
    self.l1.insert_at_end(98)
    self.assertEqual(str(self.l1), '[1 -> 98]')
    self.assertEqual(len(self.l1), 2)
    
    self.l2.insert_at_end(98)
    self.assertEqual(str(self.l2), '[1 -> 2 -> 98]')
    self.assertEqual(len(self.l2), 3)
    
    self.l3.insert_at_end(98)
    self.assertEqual(str(self.l3), '[1 -> 2 -> 3 -> 98]')
    self.assertEqual(len(self.l3), 4)
    
  def test_remove_last_empty_list(self):
    result = self.empty_list.remove_last()
    self.assertFalse(result)
    self.assertEqual(len(self.empty_list), 0)
    
  def test_remove_last_one_list(self):
    self.l1.remove_last()
    self.assertEqual(str(self.l1), '[]')
    self.assertEqual(len(self.l1), 0)
    
  def test_remove_last_two_list(self):
    self.l2.remove_last()
    self.assertEqual(str(self.l2), '[1]')
    self.assertEqual(len(self.l2), 1)
    
  def test_remove_last_three_list(self):
    self.l3.remove_last()
    self.assertEqual(str(self.l3), '[1 -> 2]')
    self.assertEqual(len(self.l3), 2)
      
  def test_insert_at_index_empty_list_default_param(self):
    self.empty_list.insert_at_index(22)
    self.assertEqual(str(self.empty_list), '[22]')
    self.assertEqual(len(self.empty_list), 1)
    
  def test_insert_at_index_empty_list0(self):
    self.empty_list.insert_at_index(22, 0)
    self.assertEqual(str(self.empty_list), '[22]')
    self.assertEqual(len(self.empty_list), 1)
    
  def test_insert_at_index_size_one_list0(self):
    self.l1.insert_at_index(22, 0)
    self.assertEqual(str(self.l1), '[22 -> 1]')
    self.assertEqual(len(self.l1), 2)
    
  def test_insert_at_index_size_one_list1(self):
    self.l1.insert_at_index(22, 1)
    self.assertEqual(str(self.l1), '[1 -> 22]')
    self.assertEqual(len(self.l1), 2)
    
  def test_insert_at_index_size_three_list0(self):
    self.l3.insert_at_index(22, 0)
    self.assertEqual(str(self.l3), '[22 -> 1 -> 2 -> 3]')
    self.assertEqual(len(self.l3), 4)
    
  def test_insert_at_index_size_three_list1(self):
    self.l3.insert_at_index(22, 1)
    self.assertEqual(str(self.l3), '[1 -> 22 -> 2 -> 3]')
    self.assertEqual(len(self.l3), 4)
    
  def test_insert_at_index_size_three_list2(self):
    self.l3.insert_at_index(22, 2)
    self.assertEqual(str(self.l3), '[1 -> 2 -> 22 -> 3]')
    self.assertEqual(len(self.l3), 4)
    
  def test_insert_at_index_size_three_list3(self):
    self.l3.insert_at_index(22, 3)
    self.assertEqual(str(self.l3), '[1 -> 2 -> 3 -> 22]')
    self.assertEqual(len(self.l3), 4)
    
  # remove at index tests
  def test_remove_at_index_empty_list_default_param(self):
    result = self.empty_list.remove_at_index()
    self.assertFalse(result)
    
  def test_remove_at_index_size_one_list0(self):
    self.l1.remove_at_index(0)
    self.assertEqual(str(self.l1), '[]')
    self.assertEqual(len(self.l1), 0)
    
  def test_remove_at_index_size_three_list0(self):
    self.l3.remove_at_index(0)
    self.assertEqual(str(self.l3), '[2 -> 3]')
    self.assertEqual(len(self.l3), 2)
    
  def test_remove_at_index_size_three_list1(self):
    self.l3.remove_at_index(1)
    self.assertEqual(str(self.l3), '[1 -> 3]')
    self.assertEqual(len(self.l3), 2)
    
  def xtest_remove_at_index_size_three_list2(self):
    self.l3.remove_at_index(2)
    self.assertEqual(str(self.l3), '[1 -> 2]')
    self.assertEqual(len(self.l3), 2)
    
  def test_for_loop(self):
    for (i, node) in enumerate(self.l3):
      self.assertEqual(node.data, i + 1)
    
unittest.main()
