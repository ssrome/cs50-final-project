from datetime import date


class InjectYear:
    def __call__(self):
        current_year = date.today().strftime("%Y")
        return f'2022 - {current_year}'
