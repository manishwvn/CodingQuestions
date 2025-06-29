SELECT 
    ROUND(
        
            COUNT(CASE WHEN order_date = customer_pref_delivery_date THEN delivery_id ELSE NULL END) / 
        COUNT(delivery_id) * 100, 2
    ) AS immediate_percentage
FROM 
    Delivery;