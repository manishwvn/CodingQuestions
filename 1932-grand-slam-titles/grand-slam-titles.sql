select p_id as player_id, player_name, sum(wins) as  grand_slams_count from 

(select wimbledon as p_id,count(*) as wins from Championships
group by 1

union all 

select Fr_open as p_id,count(*) as wins from Championships
group by 1

union all

select US_open as p_id,count(*) as wins from Championships
group by 1

union all

select Au_open as p_id,count(*) as wins from Championships
group by 1
) AS X 
inner join Players Y  on X.p_id = Y.player_id
group by 1,2