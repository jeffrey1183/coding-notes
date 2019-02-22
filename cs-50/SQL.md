Trying to find some way to use databases to make it easier for our web applications to store and manipulate and use data ultimately.

And the types of databases that we're going to be talking about today, are relational databases. Which you can think of as effectively storing data inside of a table.

Designing these sorts of tables, but we're going to do so using technology called SQL, or S-Q-L. Structured query language, which is a language designed to allow us to very easily interact with databases.

Interact with tables of data that have rows and columns, for instance.



# Example 1: [create.sql](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/SQL/create.sql)
* [Youtube tutorial](https://youtu.be/j5wysXqaIV8?t=5631)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/Flask/notes)

## I've Learned:
* 


* Download the [Postgres app](https://github.com/PostgresApp/PostgresApp/releases/)
* [PostgreSQL 11.1 Documentation](https://www.postgresql.org/docs/11/index.html)
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
* Update some data inside the database using [UPDATE query](https://www.tutorialspoint.com/postgresql/postgresql_update_query.htm)


## Example 4: [delete.sql]()
* Delete data inside the database using [DELETE query](https://www.tutorialspoint.com/postgresql/postgresql_delete_query.htm)
* When I delete one row, and then I add another row. That the numbers just keep adding up and they don't fill in the blanks

## Example 5: [limit.sql]()
* [LIMIT clause](https://www.tutorialspoint.com/postgresql/postgresql_limit_clause.htm) is used to limit the data amount returned by the SELECT statement.
* [OFFSET](https://www.postgresql.org/docs/8.0/queries-limit.html) says to skip that many rows before beginning to return rows.

## Example 6: [order.sql]()
* [ORDER BY](https://www.tutorialspoint.com/postgresql/postgresql_order_by.htm) clause is used to sort the data in ascending or descending order, based on one or more columns.
* Count how many flights have particular origin.
* Select the popular places from which people are flying by [HAVING clause](https://www.tutorialspoint.com/postgresql/postgresql_having_clause.htm)

https://www.postgresql.org/docs/8.4/sql-select.html#SQL-LIMIT

LIMIT and OFFSET(https://www.postgresql.org/docs/11/queries-limit.html)

#Foreign Keys
A foreign key is going to be a method that we're going to use in order to connect multiple tables together. SQL is often called a relational database. And it's called a relational database because one thing that makes it quite powerful is the ability to take multiple different tables and relate them together in some way.

看到 40 分

You can imagine, if we only had this flights table as we had it before,


Passengers are a whole different entity, let's keep track of that in a different table. But there's relationships between the tables. A foreign key it's just a fancy way of saying we're referencing the key from a different table. So my flight ID column is referencing the primary key of that flights table.


A join allows you to do is take two different tables that are related in some way, and group them together in one when you try to select them.


Adminer
* https://adminer.cs50.net/
* Adminer is a third party database service that lets you interact with a database online.


SQLAlchelmy(http://docs.jinkan.org/docs/flask/patterns/sqlalchemy.html)


psql command
* [安裝](https://medium.freecodecamp.org/how-to-get-started-with-postgresql-9d3bc1dd1b11)
* [heroku](https://www.heroku.com/postgres)

