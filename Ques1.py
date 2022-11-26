#question number-1
import re
num=input("Enter the contact number:")
pat=re.compile("(0|91)?[-\s]?[6-9][0-9]{9}")
if pat.match(num):
    print("It is a valid number!")
else:
    print("It is not a valid number")