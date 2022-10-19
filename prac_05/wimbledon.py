"""
CP1404 Prac 5 - Amber Hogarth - Wimbledon
Estimate: 40 minutes
Actual: 35 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    records = get_records(FILENAME)
    countries, champion_to_count = process_records(records)
    print("Wimbledon Champions:")
    for name, count in champion_to_count.items():
        print(f"{name} {count}")
    print()
    print("These countries have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))


def get_records(filename):
    """Get records from file and put into a list."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Create set of countries and dictionary of champions."""
    countries = set()
    champion_to_count = {}
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return countries, champion_to_count


main()
