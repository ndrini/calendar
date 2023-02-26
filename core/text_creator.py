#!/usr/bin/python
from yaml import safe_load
import os

def read_user_preference() -> dict:
    '''
    Collect user info about the needed month and its peculiarity
    (for instance the week day the month starts with) 	
    '''
    data = set_up_environment()

    lang =  input(
        "Select language code you prefer to use: "
        f"\n(possible {data.keys()})"
        "\nfor instance it: "
        ) or "it"

    data = data[lang]

    print("\n\nPlease, provide some information about the month you want "
          "to create the calendar for.")
    month = input("The number of the month (int) \
    you need: for instance March is 3: ") or "4"

    # TODO read by current date or input 
    year = 2022

    try:
        day_list = ', '.join([ day for day in data['week_days']])
        # day_list = day_list[:-1] + '.'
    except:
        print("not chargeable day_list")


    print(f'Acceptable day input example {day_list}.')
    week_day = input(
        "The week day that starts the month with (string): ").lower() or "giovedì"

    # TODO data validation    
    week_number = input("The week number (int): ") or 14
    return {"month": int(month),
            "week_day": week_day,
            "week_number": int(week_number),
            # "day_parts": day_parts
            'lang': lang,
            }


def set_up_environment() -> dict:
    ''' 
    load the language specific constants and inform the user how to change it	
    '''
    try:
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, r'constants.yaml')
        with open(filename) as data_file:
            data = safe_load(data_file)
            assert type(data) == dict
            lang_list = [i for i in data] 
            print('\nLanguages available are ', lang_list)
            print('\nIf necessary, change the content of constants.yaml')
            return data
    except:
        print('Please provide a valid constants.yaml file.')
        exit()


class TextCreator():
    def __init__(self,
                 month,
                 week_day,
                 week_number,
                 data
                 ):
        ''' data is the language dict,
            while month, week_day and week_number are necessary to identify
            the currently month info '''
        self.month = month
        self.week_day = week_day
        self.week_number = week_number
        self.data = data


    def export_as_text(self):
        ''' 
        create the output
        '''
     
        print(self.data)

        this_month = self.data["months"][self.month - 1]
        month_day = 1
        this_week = self.week_number
        week_day_number = self.data['week_days'].index(self.week_day)
        # day_parts = self.data['day_parts']    

        result = ""
        t1 = "# Week by week on {}".format(this_month)
        result += t1
        print(t1)
        # check if the week already started
        if week_day_number != 0:
            this_week += 1
        for _ in range(5):   # for 4 or 5 weeks in a month
            for _ in range(7):
                if week_day_number % 7 == 0:
                    # insert year    
                    t2 = "\n__Settimana {}: {} 2022__".format(
                        this_week,
                        this_month)
                    result += t2
                    print(t2)

                t3 = "\n  * __{}__ {} {} **' '** \n".format(
                    self.data["week_days"][week_day_number % 7],
                    month_day,
                    this_month,)
                result += t3

                for part in self.data['day_parts']: 
                    result += "    * " + part + "\n" + "      * " +  "\n"

                print(t3)
                # update the values after a day
                month_day += 1
                week_day_number += 1
            # update the values after a week
            this_week += 1
        return result

def main():
    data = set_up_environment()

    pref = read_user_preference()
    c = TextCreator(
        pref["month"],
        pref["week_day"],
        pref["week_number"],
        data[pref['lang']],
    )
    result = c.export_as_text()
    new_file = 'calendar_of_' + str(pref["month"]) + '.txt'
    with open(new_file, 'w') as out_file:
        out_file.write(result)
        print(f'\nResult available as {new_file}')
    print(result)

if __name__ == '__main__':
    main()

