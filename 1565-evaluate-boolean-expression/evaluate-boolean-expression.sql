SELECT
    E.LEFT_OPERAND AS 'left_operand',
    E.OPERATOR AS 'operator',
    E.RIGHT_OPERAND AS 'right_operand',
    (
        CASE
            WHEN E.OPERATOR = '<' AND V1.VALUE < V2.VALUE THEN 'true'
            WHEN E.OPERATOR = '=' AND V1.VALUE = V2.VALUE THEN 'true'
            WHEN E.OPERATOR = '>' AND V1.VALUE > V2.VALUE THEN 'true'
            ELSE 'false'
        END
    ) AS 'value'
FROM
    EXPRESSIONS E
JOIN
    VARIABLES V1
ON 
    E.LEFT_OPERAND = V1.NAME
JOIN
    VARIABLES V2
ON
    E.RIGHT_OPERAND = V2.NAME;
