-- question 1a)
select b.name from employee as b
join (select * from employee ) as a
on b.manager_id = a.id
where a.salary < b.salary;

-- question 1b)
select avg(worker_salary) as average from (
select distinct(b.name) as worker, b.salary as worker_salary  from employee as b
inner join (select * from employee ) as a
on b.manager_id = a.id
where b.name not in (
	select a.name  from employee as b
	inner join (select * from employee ) as a
	on b.manager_id = a.id
)) as c;