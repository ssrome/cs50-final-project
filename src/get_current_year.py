from datetime import date


class GetCurrentYear:
    @staticmethod
    def __call__():
        current_year = date.today().strftime("%Y")
        return current_year
