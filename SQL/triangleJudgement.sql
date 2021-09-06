/* The hard part here wasn't actually writing the SQL statement here, but rather making sure that x,y,z 
    variables for measuring a triangle are in the proper order.
    */
SELECT 
    x,
    y,
    z,
    (CASE 
        WHEN x+y > z AND x <= z AND y <= z THEN 'Yes' 
        WHEN x+z > y AND x <= y AND z <= y THEN 'Yes'
        WHEN y+z > x AND y <= x AND z <= x THEN 'Yes'
        ELSE 'No' 
     END) AS triangle
 FROM triangle;
