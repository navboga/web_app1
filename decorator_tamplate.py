"""Декократор удобно положить в отдельный файл и потом импортировать его в основной код
декоратор принимает на вход функцию и возвращает функцию
"""
from functools import wraps

def some_decorator_name(func): # func- декорируемая функция
    @wraps(func)
    def some_name_func(*args, **kwargs):
        # 1.Код выполняющийся до декорируемой функции
        # 2.Вызов декомруемой функции и возврат полученных от нее результатов
        return func(*args, **kwargs)
        #3. код выполнения вместо декорируемой функции
    return some_name_func # возвращаем функцию


# пример



def calc_decorator(func):
    wraps(func)
    def response(*args,**kwargs):
        L = list('dshgj')
        if len(L) > 3: #проверяем уловие, если длина списка больше 3х то выполняем декорированную функцию func в данном случае(summa и multi)
            return func(*args,**kwargs)
        return 'Длина меньше 3х'
    return response # возвращаем результат функци проверки заложенной в def response -либо выполняется func либо возвращается текст 'Длина меньше 3х'


@calc_decorator
def summa(x:int, y:int):
    return x + y
@calc_decorator
def multi(x: int, y: int):
    return x * y

print(summa(3,5))
print(multi(3,5))
