"""CP1404/CP5632 Practical - Programming language class."""


class ProgrammingLanguage:
    """Represent a Programming Language."""
    def __init__(self, field="", typing="", reflection=bool, year=0):
        """Initialise a Programming Language instance."""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return whether typing is dynamic or not."""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        """Return string."""
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
