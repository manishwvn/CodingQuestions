-- select distinct
--    abs((select max(salary) from salaries where department = 'Engineering') - 
--     (select max(salary) from salaries where department = 'Marketing'))
--     as salary_difference
-- from
--     salaries;

select
    abs(
    max(case
        when
            department = 'Engineering' then salary else 0 end) - 
    max(case
        when
            department = 'Marketing' then salary else 0 end)) as            
    salary_difference
from
    salaries;
    