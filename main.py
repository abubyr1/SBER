from task1 import good_num
from task2 import build_atm
from task3 import get_max_number

if __name__ == "__main__":
    string = input("Введите строку: ")
    good_num(string)
    atm_num = int(input('Введите число n:'))
    add_atm = int(input('Введите число k: '))
    distances = [int(input()) for i in range(atm_num)]
    print(build_atm(atm_num, add_atm, distances))
    input_lst = input().split()
    print(get_max_number(input_lst))
