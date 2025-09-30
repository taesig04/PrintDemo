
name = "Alice"
age = 25
score = 95.5

print("Hello, Python!")

print("Name:", name, "Age", age, "score", score)

print(f"My name is {name}, I am {age} years old, score:{score}")

print("My name is {}, I am {} years old, score: {}".format(name, age, score))
print("Score with 2 decimals: {:.2f}".format(score))
print("This is line 1\nThis is line 2")

print("Hello", end=" ")
print("World!")

print("2025", "09", "23", sep="-")

data = {"name": name, "age": age, "score": score}
print("Data", data)
print(f"Next year age: {age + 1}")
print(f"Score (rounded): {round(score)}")

print(f"""
Student Info:
- Name : {name}
- Age : {age}
- Score: {score:.2f}
""")