
### Average program using if/elif/else

gradeOne = float( input("Enter grade one: "))
gradeTwo = float( input("Enter grade two: "))
gradeThree = float( input("Enter grade three: "))
gradeFour = float( input("Enter grade four: "))

average = (gradeOne + gradeTwo + gradeThree + gradeFour) / 4

if average >= 90:
    letterGrade = "A"
elif average < 90 and average >= 80:
    letterGrade = "B"
elif average < 80 and average >= 75:
    letterGrade = "C"
elif average < 75 and average >= 70:
    letterGrade = "D"
else:
    letterGrade = "F"

print("Your average is", average)
print("You have a(n)", letterGrade)