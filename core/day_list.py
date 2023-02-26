from datetime import datetime


class DayList:
    def __init__(self, offset=0):
        """Initialize self.month to the one of execution time"""
        self.month: int = self.get_now().month
        self.offset = offset

    def get_monthly_day_list(self, current=True, other=None):
        """
        datetime.date(2010, 6, 16).isocalendar()[1]
        """
        if not current:
            self.month = other

        return datetime.date(2010, 6, 16).isocalendar()[1]

    def get_now(self):
        return datetime.now()
    

    def select_month(self) -> tuple:
        """Return the year and the month we want the calendar for.
        We consider that if the request is made 13 days before or after the month starts, so the calendar has to be created for that specific month.
        At code level, it means that in case of an early request (before the month is already started) has to become the calendar fo the next coming month"""
        now = self.get_now()

        if now.day > 15:
            # Consider december case!!
            selected_month = now.month + 1 

        return (
            now.year, 
            now.month if now.day < 16 else now.month + 1)
    