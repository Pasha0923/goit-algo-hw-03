# 2. Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей
# Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.
# Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

import random

def get_numbers_ticket(min, max, quantity):
    try:
        # перевірка вхідних даних
        if min >= max:
            raise ValueError("❌ мінімальне число має бути менше максимального!")
        if quantity > (max - min + 1):
            raise ValueError("❌кількість чисел переважає максимальний діапазон!")
        if max > 49:
            raise ValueError("❌ максимальне число не може бути більше 49!")
        if min < 1:
            raise ValueError("❌ мінімальне число не може бути менше 1")
    except ValueError as error:
        print(error)
        return [] 
    # створюємо діапазон чисел от min до max включно
    list_numbers = list(range(min, max + 1))
    print(list(list_numbers))
    # вибираємо випадкові числа з цього діапазону
    randoms_list = random.sample(list_numbers, quantity) 
    randoms_list_sorted = sorted(randoms_list) 

    return randoms_list_sorted

lottery_numbers = get_numbers_ticket(1, 49, 6 )
print("Ваші лотерейні числа:", lottery_numbers) # [3, 15, 22, 28, 34, 45] 