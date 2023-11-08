"""
This module demonstrate the use of the if statement
"""

# pylint: disable=invalid-name

#  If statement
X = 4
if X < 1:
    SCORE = "low"
elif X <= 4:
    SCORE = "meduim"
else:
    SCORE = "high"
print("SCORE", SCORE)

# if statement with boolean
x = True
if x:
    print("It worked!")
