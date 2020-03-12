"""/
меняем функцию view_log что бы она читала данные в список списков
при этом данные в списке должны быть экранированы escape
(оригинал
def view_log():
    #with open('log_request.txt') as log:
    with open('vsearch.log') as log:
        log_data=log.readlines()
    return escape(''.join(log_data))
)

"""
# Штатно удаление не существ элем из словаря вызывает исключение,
# если не прописан default ,что возвращать- в данном случае прописал None,
#  что бы избежать исключения
# some_dict = {'apple':'green', 'limon':'yellow'}
# print(some_dict)
# some_dict.pop('limon')
# print(some_dict)
# some_dict.pop('limon',None)

import mysql.connector

def view_log():
    log_data=[]
    with open('vsearch.log') as log:
        for lines in log:
            log_data.append([])
            for item in lines.split('|'):
                log_data[-1].append((item))
        return ((log_data))


some_list=view_log()
#print(some_list)

for i in range (len(some_list)):
    for j in range (len(some_list[i])):
        print(some_list[i][j])
