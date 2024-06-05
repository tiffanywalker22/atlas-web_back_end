-- task nine, optimize search and score
-- sql script that creates an index
CREATE INDEX idx_name_first_score ON names (name(1), score);