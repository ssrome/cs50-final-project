from datetime import date


class InjectYear():
    def inject_year(self):
        today = date.today()
        year_now = today.strftime("%Y")
        print(year_now)
        # return dict(year="2022 - {}".format(year_now))
        return f'2022 - {year_now}'

