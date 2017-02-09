from collections import deque

def josephus(names, m):
  qq = deque()
  for name in names:
    qq.append(name)

  count = 0
  while len(qq) > 1:
    count += 1
    person = qq.popleft()
    if count % m == 0:
      print(f"{m} {person} is eliminated")
    else:
      print(f"{count % m} {person} is skipped")
      qq.append(person)
  last_person = qq.popleft()
  print(last_person, "is the only one left.")
  return last_person

print(josephus(["James", "John", "Mike", "Josephus"], 1))
print(josephus(["James", "John", "Mike", "Josephus"], 2))
print(josephus(["James", "John", "Mike", "Josephus"], 3))
print(josephus(["Peter", "Paul", "Mary", "Abba", "Prince", "Sting", "Beck"], 58))

