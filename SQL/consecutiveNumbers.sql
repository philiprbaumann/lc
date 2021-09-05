/* This way works but its not performance friendly. */

SELECT DISTINCT
    Num AS `ConsecutiveNums` 
FROM 
    `Logs` lg1 
WHERE 3 = (SELECT COUNT(Id) FROM `Logs` lg2 WHERE Id IN (lg1.Id, lg1.Id+1, lg1.Id+2) and lg2.Num=lg1.Num )

/* This one is more performance friendly. Instead of performing a count, we perform the same (probably cached) query two more times. */

SELECT DISTINCT
    Num AS `ConsecutiveNums` 
FROM 
    `Logs` lg1 
WHERE (lg1.Id+1, Num) IN (SELECT Id, Num from Logs) AND (lg1.Id+2, Num) in (SELECT Id, Num from Logs);