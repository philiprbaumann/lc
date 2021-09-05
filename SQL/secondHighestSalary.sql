/*Learned a few things here:
        1. Use "AS" to name information.
        2. Use LIMIT to limit the number of records returned. 
        3. Use OFFSET to move the start point of that LIMIT.
        4. Use DISTINCT (but note performance hit), can swap in "GROUP BY salary"
        5. Because we need to return null if no value exists, we need to use IFNULL. 
            - IFNULL(statement, "DEFAULT VALUE") - returns second value if first expression is NULL 
*/
SELECT
    IFNULL (
        (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET 1),
        NULL
    ) AS SecondHighestSalary;

SELECT
    IFNULL (
        (SELECT salary FROM Employee GROUP BY salary ORDER BY salary DESC LIMIT 1 OFFSET 1),
        NULL
    ) AS SecondHighestSalary;
