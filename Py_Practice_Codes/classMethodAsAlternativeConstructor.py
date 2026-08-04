class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_str):
        """Parse 'YYYY-MM-DD' to create a Date object."""
        year, month, day = map(int, date_str.split('-'))
        return cls(year, month, day)

    def __repr__(self):
        return f"Date({self.year}, {self.month}, {self.day})"

def demo_alternative_constructor():
    d = Date.from_string("2026-07-15")
    print("Date from string:", d)

demo_alternative_constructor()