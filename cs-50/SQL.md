# [SQL](https://youtu.be/Eda-NmcE5mQ)


Trying to find some way to use databases to make it easier for our web applications to store and manipulate and use data ultimately.

And the types of databases that we're going to be talking about today, are relational databases. Which you can think of as effectively storing data inside of a table.

Designing these sorts of tables, but we're going to do so using technology called SQL, or S-Q-L. Structured query language, which is a language designed to allow us to very easily interact with databases.

Interact with tables of data that have rows and columns, for instance.



## [create.sql](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/SQL/create.sql)



PostgreSQL

* 以飛機航班當作例子
* syntax of creating a [table](https://www.w3schools.com/sql/sql_create_table.asp)
* [Primary key](https://www.w3schools.com/sql/sql_primarykey.asp)
  * A table can have only one primary key, which may consist of single or multiple fields.
  * And then primary key just means this is the primary way via which I'm going to reference a flight. That every flight is going to have a unique ID. And therefore, if I tell you ID number 28, that will map to one and only one flight.
* VARCHAR
  * text
* [NULL Value](https://www.w3schools.com/sql/sql_null_values.asp)
  * A field with a NULL value is a field with no value.
  * A NULL value is different from a zero value or a field that contains spaces. A field with a NULL value is one that has been left blank during record creation!
* NOT NULL
  * column doesn't necessarily need to have a value, but can have a value if you wanted to.

[Postgres Guide](http://postgresguide.com/setup/install.html)

* 可以下 command 連到線上資料庫
* \d 顯示 table

#### [Constraints](https://www.w3schools.com/sql/sql_constraints.asp)

* [**NOT NULL**](https://www.w3schools.com/sql/sql_notnull.asp) - Ensures that a column cannot have a NULL value
* [**UNIQUE**](https://www.w3schools.com/sql/sql_unique.asp) - Ensures that all values in a column are different
* [**PRIMARY KEY**](https://www.w3schools.com/sql/sql_primarykey.asp) - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
* [**FOREIGN KEY**](https://www.w3schools.com/sql/sql_foreignkey.asp) - Uniquely identifies a row/record in another table
* [**CHECK**](https://www.w3schools.com/sql/sql_check.asp) - Ensures that all values in a column satisfies a specific condition
* [**DEFAULT**](https://www.w3schools.com/sql/sql_default.asp) - Sets a default value for a column when no value is specified
* [**INDEX**](https://www.w3schools.com/sql/sql_create_index.asp) - Used to create and retrieve data from the database very quickly

insert.sql

* Inserting Data into Table
* [官方](https://www.w3schools.com/sql/sql_insert.asp)

how to reading data from a database

* select is a query that is meant for reading from a database. I already have rows in the database, and now I care about accessing those rows.
* [select](https://www.w3schools.com/sql/sql_select.asp)
* [select where](https://www.w3schools.com/sql/sql_where.asp)

psql command

* [安裝](https://medium.freecodecamp.org/how-to-get-started-with-postgresql-9d3bc1dd1b11)
* [heroku](https://www.heroku.com/postgres)

SQL Functions

* SUM
* COUNT
* MIN
* MAX
* AVG

計算有幾列

* 可以搭配 WHERE 使用
* [SQL In](https://www.w3schools.com/sql/sql_in.asp)
* [SQL WHERE](https://www.w3schools.com/sql/sql_where.asp)
* [SQL LIKE](https://www.w3schools.com/sql/sql_like.asp)

```text
SELECT COUNT(*) FROM flights;
```

Update Query

* What if that data needs to be updated or changed?

```sql
UPDATE flights
    SET duration = 430
    WHERE origin = `New York`
-- where is telling me which rows I want to update. Not all of rows
    AND destionation = `London`
```

DELETE Query

```text
DELETE FROM countries
    WHERE destination = `Tokyo`
```

看到 31分