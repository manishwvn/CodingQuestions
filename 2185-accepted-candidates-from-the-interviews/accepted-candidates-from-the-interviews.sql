select
    c.candidate_id
from
    candidates c
 join
    rounds r
on
    c.interview_id = r.interview_id
where
    c.years_of_exp >= 2
group by
    c.candidate_id
having
    sum(r.score) > 15;