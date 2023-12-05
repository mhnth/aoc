from collections import defaultdict

with open('input.txt', 'r') as lines:
  ans = 0
  
  for game in lines:
    ok = True
    id_, game = game.split(':')
    V = defaultdict(int)
    for set in game.split(';'):
      for turn in set.split(','):
        n, color = turn.split()
        n = int(n)
        V[color] = max(V[color], n)
    score = 1
    for v in V.values():
      score *= v
    ans += score
        
print(ans)