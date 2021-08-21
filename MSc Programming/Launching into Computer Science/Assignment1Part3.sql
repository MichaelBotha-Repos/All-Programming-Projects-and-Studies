mysql;                                                                     -- Execute MySQL program 
USE COMPANY1;                                                              -- Select database 

-- Question 1
SELECT ENAME AS Employee_Name, DNAME AS Department, SAL AS Salary FROM EMP -- Select the required attributes to display
JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO                                      -- Join/link the EMP and DEPT table to access DNAME
WHERE SAL BETWEEN 1000 AND 2000                                            -- Filter salary range 
ORDER BY SAL;                                                              -- Displaying the salary in ascending order

--Question2 
SELECT COUNT(SAL) AS Department_30_Receving_Salary,                        -- Counting all those who receive a salary and aliasing column
COUNT(COMM) AS Department_30_Receving_Commission                           -- Counting all those who receive a commission and aliasing column
FROM EMP                                                                   -- Specifying source table
WHERE DEPTNO=30;                                                           -- Filtering according to department number 30 

-- Question 3 
SELECT ENAME as Employees_From_Dallas, SAL as Salary                       -- Select the columns to display from the specified table
FROM EMP                                                                   -- Select source table 
JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO                                      -- Join tables to filter on LOC
WHERE LOC = 'DALLAS'                                                       -- Condition to match, 20 represents Dallas location
ORDER BY ENAME;                                                            -- Order alphabetically according to Employee Name

-- Question 4 
SELECT DNAME AS Departments_with_No_Employees                              -- Selecting column to display with understandable alias
FROM DEPT                                                                  -- Specify source table 
LEFT OUTER JOIN EMP ON EMP.DEPTNO = DEPT.DEPTNO                            -- join with outer join to maintain NULL values 
WHERE EMPNO IS NULL;                                                       -- Filter according to non-existant employee numbers

--Question 5
SELECT DEPTNO, AVG(SAL) AS Average_Salary                                  -- Display Department Number and Average of Salaries
FROM EMP                                                                   -- The information source is Employees table 
GROUP BY DEPTNO;                                                           -- Display multiple averages in single table 