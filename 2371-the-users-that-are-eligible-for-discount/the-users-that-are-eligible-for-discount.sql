CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
        select
            distinct user_id
        from
            purchases
        where
            amount >= minAmount
        and
            time_stamp >= startDate
        and
            time_stamp <= endDate
        order by
            user_id;
END