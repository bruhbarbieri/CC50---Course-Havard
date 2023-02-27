from cs50 import get_int

scores = []

for i in range(3):
    scores.append(get_int("Scores: "))

def average():
    n = sum(scores) / len(scores)
    return n

print("Average:", average())