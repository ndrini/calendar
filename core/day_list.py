from datetime import datetime



    




class DayList:
    def __init__(self):
        """Initialize self.month to the one of execution time"""
        self.month: int = self.get_now().month

    def get_monthly_day_list(self, current=True, other=None):
        """
        datetime.date(2010, 6, 16).isocalendar()[1]

        """
        if not current:
            self.month = other

        return datetime.date(2010, 6, 16).isocalendar()[1]

    def get_now(self):
        return datetime.now()