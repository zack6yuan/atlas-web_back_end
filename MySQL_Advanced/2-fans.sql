-- Ranks country origin of bands ordered by the number of fans (non-unique)
CREATE TABLE IF NOT EXISTS number_fans (
    origin VARCHAR(255) PRIMARY KEY,
    nb_fans INT NOT NULL
)