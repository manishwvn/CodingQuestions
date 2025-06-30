WITH CompanyMaxSalaries AS (
  -- Step 1: For each employee, find the maximum salary within their company's partition.
  -- The window function adds this max salary to every row without collapsing them.
  SELECT
    company_id,
    employee_id,
    employee_name,
    salary,
    MAX(salary) OVER (PARTITION BY company_id) AS max_company_salary
  FROM
    Salaries
) -- Step 2: Apply the tax calculation based on the max_company_salary.
SELECT
  company_id,
  employee_id,
  employee_name,
  -- Use a CASE statement to determine the correct tax rate and apply it.
  -- ROUND() gives the nearest integer as requested.
  ROUND(
    CASE
      WHEN max_company_salary < 1000 THEN salary -- 0% tax
      WHEN max_company_salary <= 10000 THEN salary * 0.76 -- 24% tax
      ELSE salary * 0.51 -- 49% tax
    END
  ) AS salary
FROM
  CompanyMaxSalaries;
