/* Very close to getting this first time and its a hard. The trick here is the need for a sub-query as we can't just LIMIT 3.
    1. We want to use a sub-query when:
        You know HOW to search for a value using a select but DO NOT KNOW the exact value in the database.
    2. Here we use a sub-query to find salaries where they have less than 3 other salaries that are distinctly greater. 
        This returns the first, second, and third highest entry salaries without LIMIT X as we sometimes need to return X+1, X+2, X+N rows.
*/
SELECT DISTINCT Department.Name as Department, e1.Name as Employee, e1.Salary 
FROM Employee e1
JOIN Department ON e1.DepartmentId = Department.Id 
WHERE 3 > (
    SELECT COUNT(DISTINCT(e2.Salary)) FROM Employee e2 WHERE e2.Salary > e1.Salary and e1.DepartmentId = e2.DepartmentId);
)