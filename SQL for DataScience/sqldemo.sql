CREATE DATABASE sqldemo;  #CreateDatabase
USE sqldemo;             #USE DATABASE
select * from medicalcharges;
#Select any specific column from table
select `age` from medicalcharges;
#selct dsitinct or unique values from columns means values that are not repeated but dsitinct
select distinct region from medicalcharges;
#two distinct column at a time
select distinct age,region,sex from medicalcharges;
#select specific value means gender,departmentetc from any column
select * from medicalcharges where region in ('southeast');
select * from medicalcharges where sex in ('male') and region in ('southeast');
# show data withou any specific value gender,department etc in any column
select * from medicalcharges where smoker not in ('yes') and region not in ('southeast');

#seeing data >age 30
select * from medicalcharges where `age` > 30;
select `bmi`,`age` from medicalcharges where `age` >30;
#now average of bmi of those whose age is >30
select avg(`bmi`) from medicalcharges where age>30;

#select any specific value name,department,employee data in any column
select * from medicalcharges where bmi='22.705';
select `age`,`bmi`,`charges` from medicalcharges where charges > 10000;
#access values in a certain range 
select * from medicalcharges where `age` between 20 and 25;

#Sorting 
select * from medicalcharges order by age,bmi; #by default it will be ascending
select * from medicalcharges order by age desc;
select * from medicalcharges order by bmi desc;

#Inserting
#Specify both the column names and the values to be inserted:
#INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
#If you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query. However, make sure the order of the values is in the same order as the columns in the table. Here, the INSERT INTO syntax would be as follows:
#INSERT INTO table_name VALUES (value1, value2, value3, ...);
INSERT INTO medicalcharges (age,sex,bmi,children,smoker,region,charges) Values ('21','male','21','0','yes','southeast','16123.1000');
#checking the inserted value
select * from medicalcharges where bmi='21';
#before making any changes to data set the following
SET SQL_SAFE_UPDATES = 0;
#deleting values
#Delete All Records
#It is possible to delete all rows in a table without deleting the table. This means that the table structure, attributes, and indexes will be intact:
#DELETE FROM table_name;
#Be careful when deleting records in a table! Notice the WHERE clause in the DELETE statement. The WHERE clause specifies which record(s) should be deleted. If you omit the WHERE clause, all records in the table will be deleted!
delete from medicalcharges where charges='16123.34';
#now checking the reults
select * from medicalcharges where bmi='21';

#UPDATE
#The UPDATE statement is used to modify the existing records in a table.
#UPDATE Syntax
#UPDATE table_name
#SET column1 = value1, column2 = value2, ...
#WHERE condition;
#Be careful when updating records. If you omit the WHERE clause, ALL records will be updated!
#updating bmi to 150 of all the ages =30
UPDATE medicalcharges SET   bmi='150' WHERE age=30;
#now checking the result
select `bmi`,`age` from medicalcharges where `age` =30;

#DROP DATABASE 
#The SQL DROP DATABASE statement is used to drop an existing database in SQL schema.
#Syntax
#The basic syntax of DROP DATABASE statement is as follows −
#DROP DATABASE DatabaseName;

#GROUPBY FUNCTION
#The SQL GROUP BY clause is used in collaboration with the SELECT statement to arrange identical data into groups. This GROUP BY clause follows the WHERE clause in a SELECT statement and precedes the ORDER BY clause.
#SELECT column1, column2 FROM table_name WHERE [ conditions ] GROUP BY column1, column2 ORDER BY column1, column2
select * from medicalcharges where age >30 group by age;
select age,bmi,sex from medicalcharges where age >30 group by age,bmi,sex;

#SQL - NULL Values
#The SQL NULL is the term used to represent a missing value. A NULL value in a table is a value in a field that appears to be blank.
#CREATE TABLE CUSTOMERS(
  # ID   INT              NOT NULL,
  ## AGE  INT              NOT NULL,
  # ADDRESS  CHAR (25) ,
   #SALARY   DECIMAL (18, 2),       
   #PRIMARY KEY (ID)
#);
#in this table there is no null values
select * from medicalcharges where age is not null;
select * from medicalcharges where age is  null;

#NOW JOIN TOPIC
#A JOIN clause is used to combine rows from two or more tables, based on a related column between them.
#Different Types of SQL JOINs
#Here are the different types of the JOINs in SQL:
#suppose u have 2 tables customer and orders with same columns customer id
#(INNER) JOIN: Returns records that have matching values in both tables
      #SELECT Orders.OrderID, Customers.CustomerName FROM Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

#LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
    #SELECT Customers.CustomerName, Orders.OrderID FROM Customers LEFT JOIN Orders ON Customers.CustomerID=Orders.CustomerID ORDER BY Customers.CustomerName;

#RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
     # SELECT Orders.OrderID, Employees.LastName, Employees.FirstName FROM Orders RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeIDORDER BY Orders.OrderID;

#FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table
     #SELECT Customers.CustomerName, Orders.OrderID FROM Customers FULL OUTER JOIN Orders ON Customers.CustomerID=Orders.CustomerID ORDER BY Customers.CustomerName;
     
     #UNION(With union we can combile two columns from same table in to one and also from two different dataset
     #The UNION operator is used to combine the result-set of two or more SELECT statements.
     select age from medicalcharges union select bmi from medicalcharges
     #from different datasets
		#SELECT City FROM Customers UNION SELECT City FROM Suppliers ORDER BY City;
        
#INTERVIEW QUESTIONS
#fIND THE FIRST 3  CHARCTHER FROM CHARGES COLUMN MEANS ONLY 3 VAL FROM LEFT WILL BE USED
select left(charges,3as first_three from medicalharges; #firstthree is naming the column as firstthree 

 #Mask a column such that last few charcther are changed to star
    select concat(left(charges,3),"***") as concat_mask from medicalcharges
#Find a third to sixth chaarcther of a column
select substr(charges,3,6) from medicalcharges;
