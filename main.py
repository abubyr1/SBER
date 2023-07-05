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

    """
    Запросы для SQL
    task1
SELECT 
    @date := CURDATE() AS random_date
UNION
SELECT 
    @date := DATE_ADD(@date, INTERVAL FLOOR(RAND() *(7-2) ) + 2 DAY) AS random_date
FROM information_schema.tables
LIMIT 100;
    task2
SELECT
    employee.id AS id,
    name,
    COUNT(sales.id) AS sales_c,
    SUM(sales.id) AS sales_s,
    RANK() OVER (ORDER BY COUNT(sales.id) DESC) AS sales_rank_c,
    RANK() OVER (ORDER BY SUM(sales.id) DESC) AS sales_rank_s
FROM employee LEFT JOIN sales
    ON employee.id = sales.employee_id
GROUP BY employee.id
ORDER BY sales_c DESC, sales_s DESC;
    task3
    WITH cte AS (
    SELECT 
        tdate AS dt_from,
        LEAD(tdate, 1, '3000-01-01') OVER (PARTITION BY acc ORDER BY tdate) AS dt_to,
        amount,
        SUM(amount) OVER (PARTITION BY acc ORDER BY tdate) AS balance,
        acc
    FROM transfers
)

SELECT 
    acc,
    dt_from,
    dt_to,
    balance
FROM cte
ORDER BY acc, dt_from;




    """
