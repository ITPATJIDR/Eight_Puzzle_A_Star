import random
import copy

def win(puzzle, goal):
  return goal == puzzle

def find(puzzle,t):
    for i in range(len(puzzle)):
      for j in range(len(puzzle[i])):
        if t == puzzle[i][j]:
          return i,j

def fScore(init, puzzle,goal):
  count = 0
  for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
      if puzzle[i][j] == 0:
        continue
      if puzzle[i][j] != init[i][j]:
        count += 1  
      k,l = find(goal,puzzle[i][j])
      count += abs(k-i) + abs(l-j)
  return count 

def genOp(puzzle):
  ops = []
  i,j = find(puzzle,0)
  for p in [(-1,0),(+1,0),(0,-1),(0,+1)]:
    if not ((i+p[0] > 2) or (i+p[0] < 0) or (j+p[1] > 2) or (j+p[1] < 0)):
      ops.append([i+p[0],j+p[1]])
  return ops

def swap0(puzzles,pos):
  puzzle = copy.deepcopy(puzzles)
  i,j = find(puzzle,0)
  puzzle[i][j] = puzzle[pos[0]][pos[1]]
  puzzle[pos[0]][pos[1]] = 0
  return puzzle

def shuffle(puzzle, times):

  for i in range(times):
    o = genOp(puzzle)
    k = random.randint(0,len(o)-1)
    puzzle = swap0(puzzle,o[k])
  return puzzle
  
def solve(puzzles, goal):
  lastList = []
  puzzle = copy.deepcopy(puzzles)
  last = find(puzzle,0)
  while not win(puzzle,goal):
    ops = genOp(puzzle)
    ops = [ops[i] for i in range(len(ops)) if list(ops[i]) != list(last)]
    less = swap0(puzzle, ops[0])
    for i,v in enumerate(ops):
      if fScore(puzzles, swap0(puzzle, v),goal) < fScore(puzzles, less,goal):
        less = swap0(puzzle, v)
    last = find(puzzle,0)
    puzzle = less
    lastList.append(puzzle)
  return lastList


goal = [[1,2,3],
        [8,0,4],
        [7,6,5]]

pb =  shuffle(goal,20)
print("Target-----")
for i in goal:
  print(i)
print("-----------")
print("initial----")
for i in pb:
  print(i)
print("-----------\n\n")
lastList = solve(pb, goal)

for i in lastList[0]:
  print(i)
for i in lastList[1:]:
  print("    |")
  print("    V")
  for j in i:
    print(j)
 