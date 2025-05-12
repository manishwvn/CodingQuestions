class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        def is_leap(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        def days_in_month(month, year):
            if month == 2:
                return 29 if is_leap(year) else 28
            elif month in [1, 3, 5, 7, 8, 10, 12]:
                return 31
            else:
                return 30

        def count_total_days(year, month, day):
            days = 0
            # Add full years
            for y in range(0, year):
                days += 366 if is_leap(y) else 365
            # Add full months in current year
            for m in range(1, month):
                days += days_in_month(m, year)
            # Add days in current month
            days += day
            return days

        # Parse input
        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))

        # Get total days since year 0
        total1 = count_total_days(y1, m1, d1)
        total2 = count_total_days(y2, m2, d2)

        return abs(total1 - total2)