# Write your MySQL query statement below
select e.name name,b.bonus bonus
from Employee e left join Bonus b
on e.empID=b.empID 
where b.bonus<1000 or b.bonus is null;