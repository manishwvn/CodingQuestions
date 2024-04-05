select * from Cinema where 
mod(id, 2) <> 0 and description not like 'boring'
order by rating desc;