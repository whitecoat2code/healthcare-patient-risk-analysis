-- View all patients
SELECT * FROM patients;

-- Identify high risk patients
SELECT *
FROM patients
WHERE age > 50 AND bp > 140;

-- Outcome distribution
SELECT outcome, COUNT(*) AS count
FROM patients
GROUP BY outcome;

-- Top 5 highest BP patients
SELECT *
FROM patients
ORDER BY bp DESC
LIMIT 5;

-- High risk outcome analysis
SELECT outcome, COUNT(*) AS count
FROM patients
WHERE age > 50 AND bp > 140
GROUP BY outcome;