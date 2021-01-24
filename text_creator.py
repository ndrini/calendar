from yaml import safe_load

class text_creator():
    def __init__(self, 
                 month, 
                 # first_month_day,
                 week_day,
                 week_number,
                 ):
        self.month = month
        # self.first_month_day = first_month_day
        self.week_day = week_day
        self.week_number = week_number

    def export_as_text(self):
        this_month = data["months"][self.month - 1]
        month_day = 1
        this_week = self.week_number
        week_day_number = data['week_days'].index(self.week_day)
        print("# Week by week on {}".
            format(this_month) )
        for w in range(5):   # for 4 or 5 weeks in a month
            print("\n__Settimana {}: {} 2021__".format(
            this_week,
            this_month)
            )
            for _ in range(7):
                print("  * * {} {} {} *".format(
                data["week_days"][week_day_number % 7 ],
                month_day, 
                this_month,)
                )
                # update the values after a day
                month_day += 1
                week_day_number += 1 
            # update the values after a week 
            this_week += 1
        
        print ("Array day value: ", data['week_days'].index(self.week_day))


with open(r'constants.yaml') as data_file:
    data = safe_load(data_file)

print (data)
# c = text_creator(2, 1, "mercoledì", 6)
#              month, week_day, week_number,
c = text_creator(3, "lunedì", 10)
c.export_as_text()

