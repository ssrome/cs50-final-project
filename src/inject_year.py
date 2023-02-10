from datetime import date


class InjectYear():
    def inject_year(self):
        today = date.today()
        year_now = today.strftime("%Y")
        return f'2022 - {year_now}'

