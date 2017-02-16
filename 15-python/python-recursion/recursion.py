def sum(n):
  if n <= 0:
    return 0
  else:
    return n + sum(n - 1)

def is_palindrome(ss):
  if len(ss) < 2:
    return True
  if ss[0] != ss[-1]:
    return False
  return is_palindrome(ss[1:-1])


def reverse(ss):
  if len(ss) == 0:
    return ""
  return ss[-1] + reverse(ss[:-1])

def fib(n):
  if n < 0:
    return 0
  if n == 1 or n == 2:
    return 1
  else:
    return fib(n - 1) + fib(n - 2)


def pretty_print(dictionary, indent="  "):
  # iterate through every key in the dictionary
  for key in dictionary:
    # get the value associated with the key
    val = dictionary[key]
    # check the type of the key to see if it's another dict
    if isinstance(val, dict):
      print(f"{indent}{key}:")
      pretty_print(dictionary[key], indent + indent)
    else:
      # it's the val isn't a dict then just print out they key and val
      print(f"{indent}{key}: {val}")

print(sum(3), "should be", 6)
print(sum(4), "should be", 10)
print()

print(is_palindrome(""), "should be", True)
print(is_palindrome("a"), "should be", True)
print(is_palindrome("aa"), "should be", True)
print(is_palindrome("tacocat"), "should be", True)
print(is_palindrome("lionoil"), "should be", True)
print(is_palindrome("firetruck"), "should be", False)
print()

print(reverse("cat"), "should be", "tac")
print(reverse(reverse("abcdefghijk")), "should be", "abcdefghijk")
print()

print(fib(0), "should be", 0)
print(fib(1), "should be", 1)
print(fib(2), "should be", 1)
print(fib(3), "should be", 2)
print(fib(4), "should be", 3)
print(fib(5), "should be", 5)
print(fib(6), "should be", 8)
print(fib(7), "should be", 13)
print()

d0 = {"foo": 42, "bar": "car"}
d1 = {"foo": 42, "bar": {"baz": "ace"}}
d2 = {"foo": 42, "bar": {"baz": "ace", "deep": {"val": 3333}}, "another": 90}
pretty_print(d0)
print()
pretty_print(d1)
print()
pretty_print(d2)
print()
