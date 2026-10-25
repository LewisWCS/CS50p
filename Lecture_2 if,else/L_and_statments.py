score = int(input("Score: "))

if 75 <= score <= 100:
    print("Grade:Distinction")
elif 50 <= score < 75:
    print("Grade:Merit")
elif 20 <= score < 50:
    print("Grade:Pass")
else:
    print("Fail")