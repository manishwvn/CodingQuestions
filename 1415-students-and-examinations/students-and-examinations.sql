WITH 
students_with_subj AS (
SELECT DISTINCT s.student_id,
       s.student_name,
       Subjects.subject_name 
FROM Students AS s
CROSS JOIN Subjects)


SELECT s.student_id,
       s.student_name,
       s.subject_name,
       COUNT(e.subject_name) AS attended_exams
FROM students_with_subj AS s
LEFT JOIN Examinations AS e ON e.student_id = s.student_id
                           AND e.subject_name = s.subject_name
GROUP BY s.student_id, s.student_name, s.subject_name
ORDER BY s.student_id, s.subject_name