input = open('input.txt')

with open('input.txt', 'r') as file:
  ans = 0
  for line in file:
    digits = []
    for c in line:
      if(c.isdigit()): digits.append(c)
    score = int(digits[0] + digits[-1])
    ans += score
    
  print('ans:', ans)
        