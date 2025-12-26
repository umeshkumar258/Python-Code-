# -------------------------------
# 1. Variable Type Hints
# -------------------------------

age: int = 18
name: str = "Umesh"
height: float = 5.8
is_student: bool = True

print(name, type(name))
print(age, type(age))


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
# 3. List & Dict Type Hints
# -------------------------------

from typing import List, Dict

marks: List[int] = [85, 90, 78]
student: Dict[str, int] = {"math": 90, "science": 88}

print(marks)
print(student)


# -------------------------------
# 4. Optional Type Hint
# -------------------------------

from typing import Optional

def get_username(user: Optional[str]) -> str:
    if user:
        return user
    return "Guest"

print(get_username(None))
print(get_username("Umesh"))


# -------------------------------
# 5. Type Hint ≠ Type Enforcement
# -------------------------------

n: int = "umesh"   # ❌ allowed at runtime, but type checker warns
print(n, type(n))
