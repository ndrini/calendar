from yaml import safe_load

class text_creator():
    def __init__(self, 
                 month, 
                 week_day,
                 week_number,
                 ):
        self.month = month
        self.week_day = week_day
        self.week_number = week_number

    def export_as_text(self):
        this_month = data["months"][self.month - 1]
        month_day = 1
        this_week = self.week_number
        week_day_number = data['week_days'].index(self.week_day)
        print("# Week by week on {}".
            format(this_month) )
        # check if the week already started 
        if week_day_number != 0:
            this_week += 1
        for _ in range(5):   # for 4 or 5 weeks in a month
            for _ in range(7):
                if week_day_number % 7  == 0:
                    print("\n__Settimana {}: {} 2021__".format(
                        this_week,
                        this_month)
                        )    
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
    
with open(r'constants.yaml') as data_file:
    data = safe_load(data_file)

#              month, week_day, week_number,
c = text_creator(4, "giovedì", 14)
c.export_as_text()