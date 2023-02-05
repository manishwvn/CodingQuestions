# with CTE as (
#     select student, 
# case 
#     when id%2 = 0 then id-1
#     when id%2 = 1 and id != (select count(*) from seat) then id+1
#     else id end 
# 	as id
    
#     from seat
# )

# select id,  student
# from CTE
# order by id


select
    case 
    when id%2 = 0 then id-1
    when id%2 = 1 and id != (select count(*) from seat) then id+1
    else id end 
	as id,
    
    student

from    
    seat
order by id;
    