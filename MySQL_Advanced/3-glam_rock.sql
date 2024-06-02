-- task three, old school band
-- sql script that lists all bands with glam rock
SELECT DISTINCT band_name, (IFNULL(SPLIT, 2020)-formed) AS lifespan from metal_bands
WHERE style LIKE 'Glam rock'
ORDER BY lifespan DESC;
