select
    round(ifnull(sum(item_count * order_occurrences) / sum(order_occurrences), 0), 2)
    as average_items_per_order
from
    orders;