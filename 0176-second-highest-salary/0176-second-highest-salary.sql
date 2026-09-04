# Write your MySQL query statement belowSELE
select max(salary) SecondHighestSalary from Employee where salary<
(select max(salary) from Employee);
