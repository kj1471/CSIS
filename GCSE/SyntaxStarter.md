---
title: Selection Syntax Starter
---
 
# Task One

## What is the error?
Can you find the cause of the syntax error?
```python
# Get the user's name from the user via command line input.
name = input("What is your name: ").upper()

# Test to see if the user is called Kieran
if name is KIERAN:
    print("Hello Kieran")
else:
    print("Wait, you're not called Kieran!")
```

## Is there still an error?
```python
KIERAN = "KIERAN"
# Get the user's name from the user via command line input.
name = input("What is your name: ").upper()

# Test to see if the user is called Kieran
if name is KIERAN:
    print("Hello Kieran")
else:
    print("Wait, you're not called Kieran!")
```

# Task Two
## Incorrect Segment
How many different causes of a syntax error can you find?
```python
# Get the score from the user via command line input.
student_score = int(input("Student's score: ")

# Test to see if the score is a pass, a fail, or 0.
if student_score => 70
    print("That is a pass")
elif student_score > 0
    print("That is a fail")
elif
    print("Did the student even attend?")
```

## What is wrong?
- Closing parenthesis (`)`) missing
- Missing colons (`:`) missing (x3)
- `elif` in place of `else`
- `=>` is invalid, use `>=`  
    Python is a bit picky here, but the `>` or `<` must come first

## Correction
```python
# Get the score from the user via command line input.
student_score = int(input("Student's score: "))

# Test to see if the score is a pass, a fail, or 0.
if student_score >= 70:
    print("That is a pass")
elif student_score > 0:
    print("That is a fail")
else:
    print("Did the student even attend?")
```
 