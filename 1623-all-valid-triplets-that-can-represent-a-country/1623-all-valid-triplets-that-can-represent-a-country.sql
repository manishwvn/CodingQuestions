SELECT DISTINCT
    A.STUDENT_NAME AS 'member_a',
    B.STUDENT_NAME AS 'member_b',
    C.STUDENT_NAME AS 'member_c'
FROM
    SCHOOLA AS A
JOIN
    SCHOOLB AS B
ON
    A.STUDENT_ID <> B.STUDENT_ID
    AND
    A.STUDENT_NAME <> B.STUDENT_NAME
JOIN
    SCHOOLC AS C
ON 
    C.STUDENT_ID <> B.STUDENT_ID
    AND
    B.STUDENT_NAME <> C.STUDENT_NAME
AND
    A.STUDENT_ID <> C.STUDENT_ID 
    AND 
    A.STUDENT_NAME <> C.STUDENT_NAME;
    
