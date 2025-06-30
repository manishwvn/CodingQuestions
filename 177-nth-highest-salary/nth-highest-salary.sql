CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select distinct coalesce(salary) from
      (
        select
            *,
            dense_rank() over(order by salary desc) as rnk
        from
            employee
      ) as t
      where
        t.rnk = N

  );
END