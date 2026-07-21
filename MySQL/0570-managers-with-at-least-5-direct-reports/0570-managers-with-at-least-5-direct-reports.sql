# Write your MySQL query statement below
select 
case 
    when e1.name is null then  null
    else e1.name
end as name
from employee e1
inner join employee e2
on e1.id=e2.managerId
group by e1.id
having count(*)>=5;