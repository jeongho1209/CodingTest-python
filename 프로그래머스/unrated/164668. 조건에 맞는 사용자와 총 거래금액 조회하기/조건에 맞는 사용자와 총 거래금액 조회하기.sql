-- 코드를 입력하세요
SELECT 
U.USER_ID USER_ID,
U.NICKNAME NICKNAME,
SUM(B.PRICE) TOTAL_SALES
FROM USED_GOODS_USER AS U 
INNER JOIN USED_GOODS_BOARD AS B
ON B.WRITER_ID = U.USER_ID
WHERE B.STATUS = 'DONE'
GROUP BY U.USER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES;