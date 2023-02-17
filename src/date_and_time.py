import datetime


class DateAndTime:
    # def __init__(self, date):
    #     self.date_time = date

    @staticmethod
    def get_date_time_now():
        return datetime.date().today()

    @staticmethod
    def get_current_year():
        current_year = datetime.date.today().strftime("%Y")
        return current_year
