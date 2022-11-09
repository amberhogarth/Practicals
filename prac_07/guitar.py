""""""


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        return f"{self.name}, made in {self.year}, ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year

