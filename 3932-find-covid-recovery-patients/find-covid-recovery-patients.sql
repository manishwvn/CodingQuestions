WITH FirstPositive AS (
    SELECT
        patient_id,
        MIN(test_date) AS first_pos_date
    FROM
        covid_tests
    WHERE
        result = 'Positive'
    GROUP BY
        patient_id
),
FirstNegativeAfterPositive AS (
    SELECT
        ct.patient_id,
        MIN(ct.test_date) AS first_neg_date
    FROM
        covid_tests ct
    JOIN
        FirstPositive fp ON ct.patient_id = fp.patient_id
    WHERE
        ct.result = 'Negative'
        AND ct.test_date > fp.first_pos_date
    GROUP BY
        ct.patient_id
)
SELECT
    p.patient_id,
    p.patient_name,
    p.age,
    DATEDIFF(fnap.first_neg_date, fp.first_pos_date) AS recovery_time
FROM
    patients p
JOIN
    FirstPositive fp ON p.patient_id = fp.patient_id
JOIN
    FirstNegativeAfterPositive fnap ON p.patient_id = fnap.patient_id
ORDER BY
    recovery_time ASC,
    p.patient_name ASC;