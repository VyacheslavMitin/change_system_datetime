# Модуль смены времени в системе

import pyautogui
import win32api
from datetime import datetime


def input_datetime():
    """Функция запроса ДАТЫ и ВРЕМЕНИ"""
    input_year = pyautogui.prompt(text="ГОД - формат '2022'", title='Ввод года', default='2022')
    input_month = pyautogui.prompt(text="МЕСЯЦ - формат '12'", title='Ввод месяца', default='')
    input_date = pyautogui.prompt(text="ДЕНЬ - формат '29'", title='Ввод дня', default='1')
    input_hour = pyautogui.prompt(text="ЧАС - формат '11'", title='Ввод часа', default='08')
    input_minute = pyautogui.prompt(text="МИНУТЫ - формат '59'", title='Ввод минут', default='00')

    time_tuple = (
            int(input_year),  # ГОД
            int(input_month),  # МЕСЯЦ
            int(input_date),  # ДЕНЬ
            int(input_hour)-4,  # ЧАС (-4)
            int(input_minute),  # МИНУТЫ
            0,  # СЕКУНДЫ
            0,  # МИЛИСЕКУНДЫ
                  )

    return time_tuple


def win_set_time(time_tuple=input_datetime()):
    """Функция смены ДАТЫ и ВРЕМЕНИ"""
    day_of_week = datetime(*time_tuple).isocalendar()[2]
    t = time_tuple[:2] + (day_of_week,) + time_tuple[2:]
    win32api.SetSystemTime(*t)


if __name__ == '__main__':
    win_set_time()
