select
             
            s.student_id,
            s.student_name,
            sub.subject_name,
            count(e.student_id) as attended_exams
    from
        students s
    cross join
        subjects sub
    
    left join
    examinations e 
    on
        s.student_id = e.student_id
        and
        e.subject_name = sub.subject_name

    group by 1,2,3
    order by 1, 3
