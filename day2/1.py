# 12 red cubes, 13 green cubes, and 14 blue

with open('input.txt', 'r') as lines:
  ans = 0
  for game in lines:
    ok = True
    id_, game = game.split(':')
    for set in game.split(';'):
      for turn in set.split(','):
        n, color = turn.split()
        if int(n) > {'red': 12, 'green': 13, 'blue': 14 }.get(color, 0):
          ok = False
    if ok: 
      ans += int(id_.split()[1])
        
print(ans)
    