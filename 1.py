# https://adventofcode.com/2022/day/1

with open('input/1.txt') as f:
  lines = f.readlines()

elves = []
calories = []
for line in lines:
  if line == '\n':
    elves.append(calories)
    calories = []
  else:
    calories.append(int(line[:-1]))

elves.append(calories)

print(max([sum(calories) for calories in elves]))

elves = sorted(elves, key=lambda x: sum(x))
elves_summed = [sum(calories) for calories in elves]
top_3_elves = sum(elves_summed[-3:])
print(top_3_elves)