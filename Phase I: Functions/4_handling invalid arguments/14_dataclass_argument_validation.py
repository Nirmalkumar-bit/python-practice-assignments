# Task: Create a dataclass UserInput and validate fields in __post_init__.
# Fields:
# - username: str, must be 3-20 chars, alnum or underscore only
# - age: int, must be between 13 and 120 inclusive (bool not allowed)
# - email: str, must contain exactly one "@" and at least one "." after the "@"
# Invalid handling:
# - Raise TypeError("username must be a str"), TypeError("age must be an int"), TypeError("email must be a str")
# - Raise ValueError("invalid username"), ValueError("invalid age"), ValueError("invalid email")
# Expected outcome:
# - UserInput("alice_1", 30, "a@b.com") constructs successfully
# - UserInput("a!", 30, "a@b.com") raises ValueError("invalid username")
# - UserInput("alice", True, "a@b.com") raises TypeError("age must be an int")
from dataclasses import dataclass


@dataclass
class UserInput:
    username: str
    age: int
    email: str

    def __post_init__(self):
        # -----------------------
        # Type validation
        # -----------------------
        if not isinstance(self.username, str):
            raise TypeError("username must be a str")

        if type(self.age) is not int:   # blocks bool
            raise TypeError("age must be an int")

        if not isinstance(self.email, str):
            raise TypeError("email must be a str")

        # -----------------------
        # Username validation
        # -----------------------
        if not (3 <= len(self.username) <= 20):
            raise ValueError("invalid username")

        if not all(c.isalnum() or c == "_" for c in self.username):
            raise ValueError("invalid username")

        # -----------------------
        # Age validation
        # -----------------------
        if not (13 <= self.age <= 120):
            raise ValueError("invalid age")

        # -----------------------
        # Email validation
        # -----------------------
        if self.email.count("@") != 1:
            raise ValueError("invalid email")

        local, domain = self.email.split("@")

        if local == "":
            raise ValueError("invalid email")

        if "." not in domain:
            raise ValueError("invalid email")

        if domain.startswith(".") or domain.endswith("."):
            raise ValueError("invalid email")

        name_part, ext_part = domain.rsplit(".", 1)
        if name_part == "" or ext_part == "":
            raise ValueError("invalid email")


# -------------------------------------------------
# This part runs only if you execute the file
# -------------------------------------------------
if __name__ == "__main__":
    u = UserInput("alice_1", 30, "a@b.com")
    print(u)
