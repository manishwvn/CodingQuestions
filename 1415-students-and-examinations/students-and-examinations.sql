with students_with_subj as (
    select
        distinct 
            s.student_id,
            s.student_name,
            sub.subject_name
    from
        students s
    cross join
        subjects sub
)


select
    s.student_id,
    s.student_name,
    s.subject_name,
    COUNT(e.student_id) AS attended_exams
FROM 
    students_with_subj AS s
LEFT JOIN 
    Examinations AS e 
ON 
    e.student_id = s.student_id
    AND 
    e.subject_name = s.subject_name
GROUP BY s.student_id, s.student_name, s.subject_name
ORDER BY s.student_id, s.subject_name
