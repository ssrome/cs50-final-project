from datetime import datetime, date, timezone


class DateAndTime:
    # def __init__(self, date):
    #     self.date_time = date

    @staticmethod
    def get_date_time_now():
        return date.today()

    @staticmethod
    def get_current_year():
        return date.today().strftime("%Y")

    @staticmethod
    def get_utc_time():
        utc_time_now = datetime.now(tz=timezone.utc)
        return utc_time_now.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def convert_to_utc_time(local_now, utc_now, countdown_time):
        if local_now > utc_now:
            utc_offset = local_now - utc_now
            print(utc_offset)
            converted_time = countdown_time - utc_offset
            print(converted_time)
            return datetime.astimezone(converted_time, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

        # date_in_numbers = datetime.fromisoformat(timestamp)
        # return datetime.astimezone(date_in_numbers, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
