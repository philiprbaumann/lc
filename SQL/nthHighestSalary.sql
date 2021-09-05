/*Learned a few things here:
        1. This is very similar to secondHighestSalary.sql so that helps.
        2. Main thing to realize is how methods can be defined in SQL. 
        3. You cannot perform arithmetic within the LIMIT/OFFSET logic so you need to DECLARE a new variable BEFORE the return block. 
            -   DECLARE varname vartype;
                SET varname = VALUE;
                    OR
                DECLARE varname vartype DEFAULT value;
*/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M int DEFAULT N-1;
  RETURN (
      SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET M
  );
END