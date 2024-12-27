with same_locs as(
    select
        concat(lat,',',lon) as loc
    from
        insurance
    group by lat, lon
    having count(pid) > 1
),

inv_2015 as(
    select
        distinct
            t1.pid,
            t1.tiv_2015,
            t1.tiv_2016
    from
        insurance t1
    left join
        insurance t2
    on
        t1.tiv_2015 = t2.tiv_2015
    where
        t1.pid <> t2.pid
    and
        concat(t1.lat,',',t1.lon) not in (select loc from same_locs)
)

select round(sum(tiv_2016), 2) as tiv_2016 from inv_2015;