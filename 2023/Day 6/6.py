## hardcoded my inputs since short
races = [
  (49, 298),
  (78, 1185),
  (79, 1066),
  (80, 1181)
]
answer = 1

for race in races:
  wins = 0
  for speed in range(race[0]):
    time = race[0] - speed
    distance = time * speed
    if distance > race[1]:
      wins += 1
  answer *= wins

print(answer)