# Python Type Hints - Improved Version

# -------------------------------
# 1. Variable Type Hints
# -------------------------------
marks: int = 300
age: int = 18
name: str = "Umesh"
height: float = 5.8
is_student: bool = True

print(f"{name} -> {type(name)}")
print(f"{age} -> {type(age)}")
print(f"{marks} -> {type(marks)}")
print(f"{height} -> {type(height)}")
print(f"{is_student} -> {type(is_student)}")


# -------------------------------
# 2. Function Type Hints
# -------------------------------
def add(a: int, b: int) -> int:
    return a + b


def greeting(name: str) -> str:
    return f"Hello, {name}!"


print(add(10, 20))
print(greeting("Umesh"))


# -------------------------------
# 3. List & Dict Type Hints (Modern)
# -------------------------------
marks_list: list[int] = [85, 90, 78]
student: dict[str, int] = {"math": 90, "science": 88}

print(marks_list)
print(student)


# -------------------------------
# 4. Optional Type Hint (Modern)
# -------------------------------
def get_username(user: str | None) -> str:
    return user if user else "Guest"


print(get_username(None))
print(get_username("Umesh"))


# -------------------------------
# 5. Type Hint ≠ Type Enforcement
# -------------------------------
n: int = "umesh"   # ⚠️ No runtime error, but static tools will warn
print(n, type(n))
