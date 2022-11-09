"""CP1404/CP5632 Practical - Guitars!"""


class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name="", year=0, cost=0.0):
        """Initialise Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get age of guitar."""
        age = 2022 - self.year
        return age

    def is_vintage(self):
        """Check if guitar is vintage (age >= 50)."""
        return self.get_age() >= 50
