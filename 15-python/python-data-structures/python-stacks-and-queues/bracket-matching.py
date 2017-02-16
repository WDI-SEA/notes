def test_brackets(ss):
  opening = "([{"
  closing = ")]}"
  stack = []
  for letter in ss:
    # put all opening characters on the stack to wait to be matched.
    if letter in opening:
      stack.append(letter)
    if letter in closing:
      # grab the first thing off the stack and make sure it matches.
      first = stack.pop()
      if first == "[" and not letter == "]":
        return False
      if first == "(" and not letter == ")":
        return False
      if first == "{" and not letter == "}":
        return False

  # if there's anything left in the stack that means
  # something was left waiting to be matched.
  if len(stack) > 0:
    return False

  return True


print(test_brackets('abc(123)'))
print(test_brackets('a[bc(123)]'))
print(test_brackets('a{b}{c(1[2]3)}'))
print(test_brackets('()'))
print(test_brackets('abc123yay'))

print(test_brackets('abc(123'))
print(test_brackets('a[bc(12]3)'))
print(test_brackets('a{b}{c(1}[2]3)'))
