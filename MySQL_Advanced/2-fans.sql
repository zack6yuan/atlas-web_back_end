-- Ranks country origin of bands ordered by the number of fans (non-unique)
SELECT origin, nb_fans
FROM metal_bands
ORDER BY nb_fans DESC