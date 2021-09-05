/* Things to learn from this example:
        1. You can use a `CASE` instead of a `SELECT` to perform a IFNULL sort of query.
            CASE WHEN column1='value' THEN column2 ELSE null END.
        2. We use SUM here to not lose the values after a GROUP BY. Given GROUP BY will choose one volumn value, we can do SUM to make sure
            all of those values are included in the group. 
*/
SELECT 
    id,
    SUM( CASE when month='Jan' then revenue else null end ) as Jan_Revenue,
    SUM( CASE when month='Feb' then revenue else null end ) as Feb_Revenue,
    SUM( CASE when month='Mar' then revenue else null end ) as Mar_Revenue,
    SUM( CASE when month='Apr' then revenue else null end ) as Apr_Revenue, 
    SUM( CASE when month='May' then revenue else null end ) as May_Revenue, 
    SUM( CASE when month='Jun' then revenue else null end ) as Jun_Revenue, 
    SUM( CASE when month='Jul' then revenue else null end ) as Jul_Revenue, 
    SUM( CASE when month='Aug' then revenue else null end ) as Aug_Revenue, 
    SUM( CASE when month='Sep' then revenue else null end ) as Sep_Revenue, 
    SUM( CASE when month='Oct' then revenue else null end ) as Oct_Revenue, 
    SUM( CASE when month='Nov' then revenue else null end ) as Nov_Revenue, 
    SUM( CASE when month='Dec' then revenue else null end ) as Dec_Revenue
FROM
    Department
GROUP BY
    id;