CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
        select
            distinct user_id
        from
            purchases
        where
            amount >= minAmount
        and
            time_stamp >= cast(startDate as datetime)
        and
            time_stamp <= cast(endDate as datetime)
        order by
            user_id;
END