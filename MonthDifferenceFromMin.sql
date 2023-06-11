
SELECT CustID, date, timestampdiff(MONTH, MIN(date) OVER (PARTITION BY CustID), date) AS month_gap
FROM MONTHDIFFERENCE