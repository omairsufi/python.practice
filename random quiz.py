import random

correct = 0

for _ in range(20):
    a = random.randint(0,20)
    b = random.randint(0,20)
    c = a + b
    print(a, "+", b, "=" )
    r = int(input())

    if r == c:
        print("Correct answer!")
    else:
        print("Try Again...")

    max_correct = 5
    if correct < max_correct:
        correct += 1
        continue
    elif correct >= max_correct:
        break    
print("5 correct answers!!!")