import datetime


class DateAndTime:
    # def __init__(self, date):
    #     self.date_time = date

    @staticmethod
    def get_date_time_now():
        return datetime.date.today()

    @staticmethod
    def get_current_year():
        return datetime.date.today().strftime("%Y")

    @staticmethod
    def get_utc_time():
        return datetime.datetime.utcnow()
