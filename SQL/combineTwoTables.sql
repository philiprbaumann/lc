/*Learned a few things here:
    - LEFT JOIN: all rows that match as well as rows that don't, left table with NULL values in non-matching columns
    - RIGHT JOIN: all rows that match as well as rows that don't right table with NULL values in non-matching columns
    - INNER JOIN: only rows that match
    - FULL JOIN: combination of LEFT JOIN and RIGHT JOIN, all rows that match as well as rows that don't in both tables
        with NULL values in non-matching columns 
*/

SELECT Person.FirstName, Person.LastName, Address.City, Address.State
FROM Person LEFT JOIN Address ON Person.PersonId = Address.PersonId;