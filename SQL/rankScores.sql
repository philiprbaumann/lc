/* Things to note on this question:
    1. DENSE_RANK() groups and ranks, prevents gaps between rankings if there are more than one values with the same rank. (1,1,1,2)
    2. RANK() groups, but keeps gaps so (1,1,1,4)
/* MySQL 8 DENSE_RANK() Approach: */
SELECT Score,
    DENSE_RANK() OVER (ORDER BY SCORE DESC) as Rank
FROM Scores;

/* Older MySQL approach which is more "basic". Pretty straightforward approach.*/
SELECT sc1.Score, (SELECT COUNT(DISTINCT(sc2.Score)) FROM Scores sc2 WHERE sc2.Score >= sc1.Score) as `Rank`
FROM Scores sc1 ORDER BY sc1.Score DESC;