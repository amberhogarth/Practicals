"""CP1404 Prac 9 - Silver Service Taxi Test"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test a SilverServiceTaxi."""
    silver_taxi_1 = SilverServiceTaxi("1", 100, 2)
    silver_taxi_1.drive(18)
    print(silver_taxi_1.get_fare())
    print(silver_taxi_1)


main()
