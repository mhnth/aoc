input = open('input.txt')

with open('input.txt', 'r') as file:
  ans = 0
  for line in file:
    digits = []
    for i, c in enumerate(line):
      if c.isdigit():
        digits.append(c)
      for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        if line[i:].startswith(val):
          digits.append(str(d + 1))
      if(c.isdigit()): digits.append(c)
    score = int(digits[0] + digits[-1])
    ans += score
    
  print('ans:', ans)