SELECT
    question_id AS survey_log
FROM
    surveylog
GROUP BY
    question_id
ORDER BY
    -- Calculate the answer rate directly using conditional aggregation
    SUM(CASE WHEN action = 'answer' THEN 1 ELSE 0 END) / SUM(CASE WHEN action = 'show' THEN 1 ELSE 0 END) DESC,
    question_id ASC
LIMIT 1;