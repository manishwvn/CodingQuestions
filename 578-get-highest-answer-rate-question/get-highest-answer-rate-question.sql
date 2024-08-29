WITH AnswerRates AS (
    SELECT
        question_id,
        COALESCE(
            SUM(CASE WHEN action = 'answer' THEN 1 ELSE 0 END)::decimal /
            NULLIF(SUM(CASE WHEN action = 'show' THEN 1 ELSE 0 END), 0),
            0
        ) AS answer_rate
    FROM
        SurveyLog
    GROUP BY
        question_id
)
SELECT
    question_id AS survey_log
FROM
    AnswerRates
ORDER BY
    answer_rate DESC,
    question_id ASC
LIMIT 1;