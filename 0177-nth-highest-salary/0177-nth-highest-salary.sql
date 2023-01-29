CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT 
        DISTINCT SALARY AS SecondHighestSalary
      FROM
        (SELECT 
            SALARY,
            DENSE_RANK() OVER (ORDER BY SALARY DESC) AS RANK_DESC
         FROM 
            EMPLOYEE) AS E2
      WHERE
        E2.RANK_DESC = N);
END