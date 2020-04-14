import calendar


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
                if cnt == 0 & day_of_week >= 0 & day_of_week <= 5:
                    temp = day_of_week + 1
                    for i in range(temp):
                        days.append(0)
                    days.append(day)
                else:
                    days.append(day)
                cnt += 1
        return days

    def get_month(self):
        return self.months[self.month - 1]
