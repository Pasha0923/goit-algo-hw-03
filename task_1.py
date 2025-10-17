#  1. Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

from datetime import datetime
my_date = "2026-10-10"
def get_days_from_today(date):
    try:
        datetime_object = datetime.strptime(date,"%Y-%m-%d").date()
        today = datetime.today().date()  
        difference = (today - datetime_object).days
        print(difference)
        return difference 
    except ValueError:
        print("❌ Неправильный формат дати! Використовуйте формат 'YYYY-MM-DD', наприклад '2024-09-09'")
    except TypeError:
        print("❌Очікується строка 'YYYY-MM-DD', а не об'єкт дати! ")

get_days_from_today("2024.09.09") # неправильний формат дати
get_days_from_today(datetime(2024,1,1)) # непраавильний тип даних
get_days_from_today("2024-09-09") # 403
get_days_from_today(my_date) # -358