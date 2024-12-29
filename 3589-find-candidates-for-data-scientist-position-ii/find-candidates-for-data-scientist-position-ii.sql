with skillscore as(
    select
        p.project_id,
        c.candidate_id,
        100 + sum(case
            when c.proficiency > p.importance then 10
            when c.proficiency < p.importance then -5
            else 0
        end) as score,
        count(c.skill) as skill_count
    from
        candidates c
    join
        projects p
    on
        c.skill = p.skill
    group by
        1, 2),

scorerank as (
    select
        *,
        dense_rank() over(partition by project_id order by score desc, candidate_id) as rnk
    from
        skillscore
    where
        (project_id, skill_count) in (
            select
                project_id,
                count(skill) as skill_count
            from
                projects
            group by
                project_id
        ))

select
    project_id,
    candidate_id,
    score
from
    scorerank
where
    rnk = 1