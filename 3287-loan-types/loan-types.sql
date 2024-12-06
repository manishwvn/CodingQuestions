-- select
--     distinct user_id
-- from
--     loans
-- where
--     loan_type in ('Mortgage', 'Refinance')
-- group by
--     user_id
-- having
--     sum(loan_type = 'Mortgage') > 0 and sum(loan_type = 'Refinance') > 0;

select
    distinct l1.user_id
from
    loans l1
join
    loans l2
on
    l1.user_id = l2.user_id
where
    l1.loan_type = 'Refinance' and l2.loan_type = 'Mortgage'
order by 1;
