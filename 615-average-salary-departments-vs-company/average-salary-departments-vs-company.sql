with cte as (select
    s.employee_id,
    s.amount,
    date_format(s.pay_date, '%Y-%m') as pay_month,
    e.department_id,
    avg(amount) over(partition by date_format(s.pay_date, '%Y-%m')) as company_avg,
    avg(amount) over(partition by e.department_id, date_format(s.pay_date, '%Y-%m')) as department_avg
from
    salary s
left join
    employee e
on
    s.employee_id = e.employee_id)

select
    distinct
    pay_month,
    department_id,
    case 
        when department_avg > company_avg then 'higher'
        when department_avg < company_avg then 'lower'
        else 'same'
    end as comparison
from
    cte;
