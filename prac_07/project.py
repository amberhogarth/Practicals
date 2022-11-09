
from datetime import datetime


class Project:

    def __init__(self, name, start_date, priority=0, cost_estimate=0.0, completion=0):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __repr__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, " \
               f"completion: {self.completion}%"

    def is_complete(self):
        return self.completion == 100
