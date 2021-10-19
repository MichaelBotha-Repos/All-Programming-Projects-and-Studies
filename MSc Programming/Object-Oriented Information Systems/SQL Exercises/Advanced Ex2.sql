-- Find the maximum, minimum and average driver’s salary.
select max(bdsalary) as MaxSalary , min(bdsalary) as MinSalary, avg(bdsalary) as AvgSalary
from BusDriver;

-- Count the number of drivers who are working for Middlesex Transport at the moment. 
-- Change the column heading in the result to make it ‘friendly’.
select count(*) as friendly
from BusDriver;

-- (Use a subquery to answer this question) Find route information (route number and description)
--  for all routes which connect to the Holloway Depot.
select rno, rdescript 
from Route
where dno = (select dno
             from Depot
             where dname = 'Holloway');
    
-- Now try question 3 with a JOIN.
select rno, rdescript
from Route
join on Route.dno = Depot.dno;

--  List bus details for any bus which has not been assigned to a depot.
select *
from Bus
where dno is NULL;

-- List each depot name and the average salary for drivers working at the depot.
select dname as DepotName, avg(bdsalary) as AvgDriverSal
from BusDriver
join Depot on BusDriver.dno = Depot.dno
group by DepotName;

-- List each depot by name and count the number of bus drivers who are assigned to each,
-- for depots with more than one driver.
select dname, count(bdno)
from BusDriver
join Depot on BusDriver.dno = Depot.dno
group by dname
having count(bdno) > 1;