select question_id as survey_log
from (select 
question_id,
sum(case when action = 'answer' then 1 else 0 end) as ans_cnt,
sum(case when action = 'show' then 1 else 0 end) as show_cnt


from Surveylog
group by 1) a

order by  ans_cnt/show_cnt desc, 1
limit 1