from django.utils import timezone
import calendar


class Day:
    def __init__(self, number, past, month, year):
        self.number = number
        self.past = past
        self.month = month
        self.year = year

    def __str__(self):
        return str(self.number)


class Calendar(calendar.Calendar):
    def __init__(self, year, month):
        super().__init__(firstweekday=2)
        self.year = year
        self.month = month
        self.day_names = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
        self.months = (
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        )

    def get_days(self):
        weeks = self.monthdays2calendar(self.year, self.month)
        days = []
        cnt = 0
        for week in weeks:
            for day, day_of_week in week:
                now = timezone.now()
                month = now.month
                now = now.day
                past = False
                if day <= now and month == self.month:
                    past = True
                new_day = Day(number=day, past=past, month=self.month, year=self.year)
                if cnt == 0 and day_of_week >= 0 and day_of_week <= 5:
                    temp = day_of_week + 1
                    for i in range(temp):
                        days.append(Day(0, False, 0, 0))
                    days.append(new_day)
                    cnt += 1
                else:
                    days.append(new_day)
        return days

    def get_month(self):
        return self.months[self.month - 1]
