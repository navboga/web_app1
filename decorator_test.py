from functools import wraps

lst= [1,15,39,88,14,7,33]
lst1= [3,15,8,20,60,13]

def dec_func(func):
    idx = 1
    @wraps(func)
    def cnt(*args, **kwargs):
        result_external_func=func(*args,**kwargs)
        if result_external_func in lst:
            return func(*args,**kwargs)
        return 'Числа нет в списке'
    return cnt


def dec_print(func):
    @wraps(func)
    def new_func(*args,**kwargs):
        print('Мы писали мы писали наши пальчики устали')
        return func(*args,**kwargs)
    return new_func


@dec_func
#@dec_print
def calc_func(x,y):
    sm = x + y
    return sm


print(calc_func(15,0))

def sum_lst(*args):
    sm=0
    for i in args:
        sm+=int(i)
    return sm

print(sum_lst(1, 15, 39, 88, 14, 7, 33, 3, 15, 8, 20, 60, 13))