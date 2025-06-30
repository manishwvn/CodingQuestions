WITH res_cte AS (
SELECT 
    *,
    id - row_number() OVER (ORDER BY visit_date) level
FROM
    Stadium
WHERE people >= 100)
,final_cte AS (
SELECT 
    id,
    visit_date,
    people,
    level,
    COUNT(*) OVER (PARTITION BY level) consec_count
    FROM res_cte
)

SELECT id, visit_date, people FROM final_cte 
WHERE consec_count > 2 ORDER BY visit_date;

