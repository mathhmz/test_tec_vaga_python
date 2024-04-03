SELECT 
    (SELECT name FROM products WHERE id = p.id) AS product_name,
    (SELECT name FROM providers WHERE id = p.id_providers) AS provider_name
FROM products p
WHERE id_categories = 6;