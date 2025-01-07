select
    i.invoice_id,
    c1.customer_name,
    i.price,
    count(c2.contact_name) as contacts_cnt,
    count(c3.customer_name) as trusted_contacts_cnt
from
    invoices i
left join
    customers c1
on
    i.user_id = c1.customer_id
left join
    contacts c2
on
    i.user_id = c2.user_id
left join
    customers c3
on
    c2.contact_name = c3.customer_name
    and
    c2.contact_email = c3.email
group by
    1,2,3
order by
    1;

