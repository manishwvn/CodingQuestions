SELECT
    S.STOCK_NAME as 'stock_name',
    SUM(CASE WHEN OPERATION = 'SELL' THEN PRICE
        ELSE 0
        END) - 
        SUM(CASE WHEN OPERATION = 'BUY' THEN PRICE
            ELSE 0
            END) AS 'capital_gain_loss'
FROM 
    STOCKS AS S
# JOIN
#     STOCKS B
# ON
#     A.STOCK_NAME = B.STOCK_NAME
#     AND
#     A.OPERATION_DAY <> B.OPERATION_DAY
# WHERE 
#     A.OPERATION <> B.OPERATION
# GROUP BY
#     A.STOCK_NAME;

GROUP BY
    S.STOCK_NAME;
    