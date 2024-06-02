-- task two, best band ever!
-- sql script that ranks country origins of bands
SELECT DISTINCT origin, SUM(fans) as nb_fans from metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
