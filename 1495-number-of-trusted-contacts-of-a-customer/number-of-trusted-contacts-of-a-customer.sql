# Write your MySQL query statement below
SELECT 
    i.invoice_id, 
    c.customer_name, 
    i.price, 
    COUNT(co.contact_name) contacts_cnt,
    COUNT(c2.email) trusted_contacts_cnt
FROM Invoices i
JOIN Customers c ON i.user_id = c.customer_id
LEFT JOIN Contacts co ON c.customer_id = co.user_id
LEFT JOIN Customers c2 ON co.contact_email = c2.email
GROUP BY 1
ORDER BY 1