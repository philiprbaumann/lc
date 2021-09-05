/*  This approach works and functions like the top three salaries query, but its not the most straightforward.
    In these instances its better to use the MAX function to fetch the largest value in a column.
*/

/* Approach 1: Not performance friendly, but works. */ 
SELECT Department.Name as `Department`, Employee.Name as `Employee`, Employee.Salary
FROM Employee 
JOIN Department ON Employee.DepartmentId = Department.Id
WHERE 0 >= (
    SELECT (COUNT(DISTINCT(ep2.Salary))) FROM Employee as ep2 WHERE ep2.Salary > `Employee`.Salary AND ep2.DepartmentId = `Employee`.DepartmentId
);

/* Approach 2: Leverages MAX and is more performance friendly. 
        1. WHERE queries can use sub-queries to limit returned values.
        2. These sub-queries can return multiple columns like DepartmentId and Salary.
        3. That sub-query essentially returns the DepartmentId and MAX(Salary) for all employees 
            after being grouped by DepartmentId. It would be best to start with a query like this
            before attempting to generate the Department Name and Employee Names of these records. 
*/

SELECT 
    Department.Name as `Department`, 
        Employee.Name as `Employee`, 
        Employee.Salary
FROM Employee JOIN Department ON Employee.DepartmentId = Department.Id
WHERE (Employee.DepartmentId, Employee.Salary) IN 
    (SELECT DepartmentId, MAX(Salary) from Employee GROUP BY DepartmentId );
