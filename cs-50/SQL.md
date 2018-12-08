# [SQL](https://youtu.be/Eda-NmcE5mQ)


Trying to find some way to use databases to make it easier for our web applications to store and manipulate and use data ultimately.

And the types of databases that we're going to be talking about today, are relational databases. Which you can think of as effectively storing data inside of a table.

Designing these sorts of tables, but we're going to do so using technology called SQL, or S-Q-L. Structured query language, which is a language designed to allow us to very easily interact with databases.

Interact with tables of data that have rows and columns, for instance.



## Example 1: [create.sql](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/SQL/create.sql)
* Download the [Postgres app](https://github.com/PostgresApp/PostgresApp/releases/)
* Take flight as example, create a [table](https://www.tutorialspoint.com/postgresql/postgresql_create_table.htm) and display the table you create.
* [What is NULL and NOT NULL](https://www.tutorialspoint.com/postgresql/postgresql_null_values.htm)
 * Learn how to list down all the records of "NULL" or "NOT NULL"
* The basic introduction of [SERIAL](https://www.tutorialspoint.com/postgresql/postgresql_using_autoincrement.htm) 
* Commonly used [constraints](https://www.tutorialspoint.com/postgresql/postgresql_constraints.htm) available in PostgreSQL. Like PRIMARY Key.
* A primary key is a column or a group of columns used to identify a row uniquely in a table. You define primary keys through primary key constraints. Technically, a primary key constraint is the combination of a not-null constraint and a UNIQUE constraint. A table can have one and only one primary key.
* [Rename table](http://www.postgresqltutorial.com/postgresql-rename-table/)




## Example 2: [insert.sql](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/SQL/insert.sql)
* Using [INSERT query](https://www.tutorialspoint.com/postgresql/postgresql_insert_query.htm) to insert data into table. 
* Reading data from a database by [SELECT query](https://www.tutorialspoint.com/postgresql/postgresql_select_query.htm)
* [WHERE clause](https://www.tutorialspoint.com/postgresql/postgresql_where_clause.htm) is used to specify a condition while fetching the data from single table or joining with multiple tables. It is also used in UPDATE, DELETE statement, etc.
* 
* Functions
 * [SUM Function](https://www.tutorialspoint.com/postgresql/postgresql_sum_function.htm) and How to group together rows in a table that have identical data through [GROUP BY](https://www.tutorialspoint.com/postgresql/postgresql_group_by.htm)
 * [AVG Function](https://www.tutorialspoint.com/postgresql/postgresql_avg_function.htm)
 * [COUNT Function](https://www.tutorialspoint.com/postgresql/postgresql_count_function.htm)
* [MAX](https://www.tutorialspoint.com/postgresql/postgresql_max_function.htm) and [MIN Function](https://www.tutorialspoint.com/postgresql/postgresql_min_function.htm)


## Example 3: [update.sql]()
* Data needs to be updated and changed





```

看到 31分



psql command

* [安裝](https://medium.freecodecamp.org/how-to-get-started-with-postgresql-9d3bc1dd1b11)
* [heroku](https://www.heroku.com/postgres)