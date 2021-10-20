show databases;
use Bus_Depots;
show tables;
select * from BusDriver;

-- List all drivers (number and name) who have a salary of less than 1800.
select bdno as DriverNumber, bdname as DriverName  
from BusDriver 
where bdsalary < 1800;

-- List all bus drivers (number and name) whose name begins with J.
select bdno as DriverNumber, bdname as DriverName  
from BusDriver 
where bdname like 'J%';

-- List all bus drivers details for those drivers who have a salary between 2000 and 4000
select bdno as DriverNumber, bdname as DriverName  
from BusDriver 
where bdsalary between 2000 and 4000;

-- List all buses (registration number and model) of type 2 which are not based at depot 101.
select regno, model
from Bus
where (tno = 2) and (dno != 101);

-- List buses (all details )which are either Volvo model s or Mercedes models.
select * 
from Bus 
where (model like 'Volvo%') or (model like 'Mercedes%');

-- List all depot numbers in the bus table. Now eliminate all duplicates.
select distinct dno
from Bus;

-- List all cleaners (number and name) with the name and address of their depot, 
-- but only for those cleaners located at a depot.
select cno, cname, dname, daddress
from Cleaner c 
join Depot d on c.dno = d.dno;

-- List bus drivers (number and name) and the bus types (description)
-- for which each bus driver has had training
select BusDriver.bdno, BusDriver.bdname, join1.tdescript
from BusDriver 
join (select BusType.tdescript, Training.tno, Training.bdno 
      from BusType 
      join Training on BusType.tno = Training.tno
     ) as join1
on BusDriver.bdno = join1.bdno;
      