SELECT name
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM legal_person lp
    WHERE lp.id_customers = c.id
);