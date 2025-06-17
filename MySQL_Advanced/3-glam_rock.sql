-- Lists all bands with "Glam rock" as their main style, ranked by their longevity
-- Coalesce - if not null, return the split year, if not, band is still current
SELECT
    band_name, IFNULL(split, 2025) - formed AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC
