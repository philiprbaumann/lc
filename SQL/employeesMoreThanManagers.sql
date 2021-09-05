/* There's a few ways to do this. Either with a join or with multiple AS definitions. */

/* Multiple AS approach: 
Advantages Of Subquery:

    Complex query can be broken down into a series of logical steps.
    Subquery is easy to read, understand and maintain.
    It allow to use the results of another query in the outer query.

Disadvantages of Subquery:

    Execution is slower than JOIN.
    We cannot modify a table and select from the same table within a subquery in the same SQL statement.
*/ 
SELECT 
    a.Name AS Employee
FROM
    Employee as a,
    Employee as b
WHERE
    a.ManagerID = b.Id AND a.Salary > b.Salary;

/* JOIN approach: 
Advantage of a JOIN

    Execution and retrieval time faster than subqueries.

Disadvantages Of JOIN:

    Database server has to do more work when it comes to a lot of joins in a query => more time consuming to retrieve data
    Developer can be confused to choose the appropriate type among many types of joins.
*/

SELECT emp.Name as Employee from Employee emp JOIN Employee man where emp.ManagerID=man.Id and emp.Salary > man.Salary;


/* The join query is faster. */ 