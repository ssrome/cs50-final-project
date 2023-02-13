from datetime import date


class InjectYear:
    @staticmethod
    def inject_year():
        today = date.today()
        year_now = today.strftime("%Y")
        return f'2022 - {year_now}'
