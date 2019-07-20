Trying to find some way to use databases to make it easier for our web applications to store and manipulate and use data ultimately.

And the types of databases that we're going to be talking about are relational databases. Which you can think of as effectively storing data inside of a table.

Designing these sorts of tables, but we're going to do so using technology called SQL, or S-Q-L. Structured query language, which is a language designed to allow us to very easily interact with databases.

In this class, we're going to be using a particular version of SQL called PostgreSQL. Although there are a bunch of different versions of SQL that have slightly different features and slightly different aspects, but they're very similar.

# Getting Started
* [Installing Postgress on Mac](https://www.postgresql.org/download/macosx/). Postgres.app is a simple, native macOS [app](https://github.com/PostgresApp/PostgresApp/releases/) that runs in the menubar without the need of an installer. It includes everything you need to get started.
* [PostgreSQL can be administered from the command line. Enter the psql command line by typing `psql`. This post introduces the basic operations](https://medium.freecodecamp.org/how-to-get-started-with-postgresql-9d3bc1dd1b11)
* [PostgreSQL 11.1 Documentation](https://www.postgresql.org/docs/11/index.html).
* [Chinese Version Document](https://docs.postgresql.tw/)

# Example 1: create.sql
* [Youtube tutorial](https://youtu.be/Eda-NmcE5mQ?t=268)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/SQL/create.sql)

## I've Learned:
* Take flight as example, create a [table](https://www.tutorialspoint.com/postgresql/postgresql_create_table.htm) using data type and constraint. 
* All of information needs to have a particular data type. PostgreSQL has a rich set of native data types available to users and this is [the document](https://www.postgresql.org/docs/11/datatype.html).
 * [Understanding PostgreSQL INTEGER data type.](https://www.postgresql.org/docs/11/datatype-numeric.html#DATATYPE-INT)
 * [Understanding PostgreSQL SERIAL data type.](https://www.tutorialspoint.com/postgresql/postgresql_using_autoincrement.htm) 
 * [What is the difference between DECIMAL and NUMERIC datatype?](https://stackoverflow.com/questions/33730538/difference-between-decimal-and-numeric-datatype-in-psql) The first answer has great example and concepts.
 * [Understanding PostgreSQL Timestamp data type.](http://www.postgresqltutorial.com/postgresql-timestamp/)
 * [Understanding the ENUM types](https://www.postgresql.org/docs/9.1/datatype-enum.html), a way of saying one of a finite number of discrete possible values.
* Commonly used [constraints](https://www.tutorialspoint.com/postgresql/postgresql_constraints.htm) available in PostgreSQL. Like PRIMARY Key.
 * A primary key is a column used to identify a row uniquely in a table like id. You define primary keys through primary key constraints. Technically, a primary key constraint is the combination of a not-null constraint and a UNIQUE constraint. A table can have one and only one primary key.
 * [What is NULL and NOT NULL](https://www.tutorialspoint.com/postgresql/postgresql_null_values.htm)
 * UNIQUE Constraint − Ensures that all values in a column are different. So for instance, if you were managing a database of users and every user has a user name, you might want that user name field to be a unique column because you don't want two different users to have the same username.
 * A column can be assigned a [default value](https://www.postgresql.org/docs/9.3/ddl-default.html).
 * CHECK Constraint − The CHECK constraint ensures that all values in a column satisfy certain conditions. For example, I only want to allow values that are less than 50 or less than 100.
* In this case, I start a server up locally on my own computer. I also can find PostgreSQL databases that are hosted online. Like [Heroku](https://www.heroku.com/), which is an online platform for hosting web sites and databases. And you'll be able to connect to that database remotely using your computer to connect to some database that's online.

## Adavanced Learning: 
* How to [rename your table.](http://www.postgresqltutorial.com/postgresql-rename-table/)


## Example 2: insert.sql
* [Youtube tutorial](https://youtu.be/Eda-NmcE5mQ?t=669)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/SQL/insert.sql)

## I've Learned:
* Using [INSERT query](https://www.tutorialspoint.com/postgresql/postgresql_insert_query.htm) to insert data into table. 
* Reading data from a database by [SELECT query](http://www.postgresqltutorial.com/postgresql-select/)
 * [WHERE clause](https://www.tutorialspoint.com/postgresql/postgresql_where_clause.htm) is used to specify a condition while fetching the data from single table or joining with multiple tables. It is also used in UPDATE, DELETE statement, etc.
 * [DISTINCT clause](http://www.postgresqltutorial.com/postgresql-select-distinct/)
* Functions
 * [SUM function](https://www.tutorialspoint.com/postgresql/postgresql_sum_function.htm) and How to group together rows in a table that have identical data through [GROUP BY](https://www.tutorialspoint.com/postgresql/postgresql_group_by.htm)
 * [AVG function](https://www.tutorialspoint.com/postgresql/postgresql_avg_function.htm)
 * [COUNT function](https://www.tutorialspoint.com/postgresql/postgresql_count_function.htm)
 * [MAX](https://www.tutorialspoint.com/postgresql/postgresql_max_function.htm) and [MIN function](https://www.tutorialspoint.com/postgresql/postgresql_min_function.htm)
* [IN operator syntax](http://www.postgresqltutorial.com/postgresql-in/)
* [LIKE operator syntax](https://www.w3schools.com/sql/sql_like.asp)
* [BETWEEN operator](http://www.postgresqltutorial.com/postgresql-between/)

## Example 3: update.sql
* [Youtube tutorial](https://youtu.be/Eda-NmcE5mQ?t=1602)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/SQL/update.sql)

## I've Learned:
* Update some data inside the database using [UPDATE query](https://www.tutorialspoint.com/postgresql/postgresql_update_query.htm)


## Example 4: delete.sql
* [Youtube tutorial](https://youtu.be/Eda-NmcE5mQ?t=1718)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/SQL/delete.sql)

## I've Learned:
* Delete data inside the database using [DELETE query](https://www.tutorialspoint.com/postgresql/postgresql_delete_query.htm)
* When I delete one row, and then I add another row. That the numbers just keep adding up and they don't fill in the blanks

## Example 5: limit.sql
* [Youtube tutorial](https://youtu.be/Eda-NmcE5mQ?t=1841)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/SQL/limit.sql)

## I've Learned:
* [LIMIT](https://www.tutorialspoint.com/postgresql/postgresql_limit_clause.htm) means I only want to get back a certain number of results.

## Adavanced Learning: 
* [OFFSET](https://www.postgresql.org/docs/8.0/queries-limit.html) says to skip that many rows before beginning to return rows.

## Example 6: order.sql
* [Youtube tutorial](https://youtu.be/Eda-NmcE5mQ?t=1868)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/SQL/order.sql)

## I've Learned:
* [ORDER BY](https://www.tutorialspoint.com/postgresql/postgresql_order_by.htm) clause is used to sort the data in ascending or descending order, based on one or more columns.
* Count how many flights have particular origin.
* There are a couple of different ways that you can go about interacting with the database. One is via the command line, one is [Adminer.cs50.net](https://adminer.cs50.net/) which is a third party database service that lets you interact with a database online.
* [GROUP BY clause](https://www.tutorialspoint.com/postgresql/postgresql_group_by.htm) is used in collaboration with the SELECT statement to group together those rows in a table that have identical data.
* Select the popular places from which people are flying by the [HAVING clause](https://www.tutorialspoint.com/postgresql/postgresql_having_clause.htm)

## Adavanced Learning: 
* [Introduction to PostgreSQL ORDER BY clause.](http://www.postgresqltutorial.com/postgresql-order-by/)


#[Foreign Keys](https://youtu.be/Eda-NmcE5mQ?t=2218)
A foreign key is going to be a method that we're going to use in order to connect multiple tables together. SQL is often called a relational database. And it's called a relational database because one thing that makes it quite powerful is the ability to take multiple different tables and relate them together in some way.


## Example 7: passengers.sql
* [Youtube tutorial](https://youtu.be/Eda-NmcE5mQ?t=2515)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/SQL/passengers.sql)


It is pretty tough now to keep track of passengers. There's no easy way to add like a column for a passenger.

Passengers are a whole different entity, let's keep track of that in a different table. But there's relationships between the tables. A foreign key it's just a fancy way of saying we're referencing the key from a different table. So my flight ID column is referencing the primary key of that flights table.

Joins are very useful once you start dealing with multiple tables. Because when a join allows you to do is take two different tables that are related in some way, and group them together in one when you try to select them.


## I've Learned:
* [We use REFERENCES clause to define a foreign key constraint.](http://www.postgresqltutorial.com/postgresql-foreign-key/) Generally speaking, the references keyword is almost always used with referencing an ID of a different table.
* An [INNER JOIN](https://www.tutorialspoint.com/postgresql/postgresql_using_joins.htm) is the most common type of join and is the default type of join. You can use INNER keyword optionally. A [JOIN clause](http://www.postgresqltutorial.com/postgresql-inner-join/) allows you to do is take two different tables that are related in some way, and group them together in one query when you try to select them.
* We select the orgin, destination and name columns, but there might be flights that have no passengers. 

```
SELECT origin, destination, name FROM flights LEFT JOIN passengers 
ON passengers.flight_id = flights.id;
```

In this situation, we can use `LEFT JOIN` and going to take the table on the left, in this case is the flights table. It's going to make sure that all of the rows in the flights table including the results without matches.

`RIGHT JOIN` selects all of the rows from the right table, even if there are no matches on the left table.

## Adavanced Learning: 
* [FULL OUTER JOIN](http://www.postgresqltutorial.com/postgresql-full-outer-join/)

# [Create Index](http://www.postgresqltutorial.com/postgresql-indexes/postgresql-create-index/)
As data gets big, it can be helpful to add an index to your table. In order to make it faster to look up that data. But it will actually slow down things like updating data or inserting data. When I need to insert the flight into the table, and then go into the index and update the index.
* [A great post from Medium](https://medium.com/d-d-mag/postgresql-%E7%95%B6%E4%B8%AD%E7%9A%84-index-e7e1e8d9340c)


#Example 8: nestingquery.sql
* [Youtube tutorial](https://youtu.be/Eda-NmcE5mQ?t=3164)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/SQL/nestingquery.sql)


## I've Learned:
* [A subquery or Inner query or Nested query is a query within another PostgreSQL query and embedded within the WHERE clause. We try to combine multiple queries together into one query.](https://www.tutorialspoint.com/postgresql/postgresql_sub_queries.htm)

# [SQL injection](https://youtu.be/Eda-NmcE5mQ?t=3390)
What does the login page do when user entering the username and password? We're processing the query like this example:
```postgresql
SELECT * FROM users
    WHERE (username = `alice`)
    AND (password = `12345`);
```
The login page will select the matching username and has a matching password in database. And if the user didn't input valid credentials, either because the user name didn't exist or the user name did exist but they typed in the wrong password, then the result of this query would be that no rows got returned.

In reality, the query probably doesn't look exactly like this. For security reasons, most databases will not store the actual password of a user and will instead store a hash of the password.

And a hacker might be able to do something like this.  And of course the string one equals the string one, those are the same thing. We called the [SQL injection](https://zh.wikipedia.org/wiki/SQL%E6%B3%A8%E5%85%A5). This is a pretty significant security concern that you want to be thinking about.


```postgresql
SELECT * FROM users
    WHERE (username = `hacker`)
    AND (password = `1` OR `1` = `1`);
```


# [Race Conditions](https://youtu.be/Eda-NmcE5mQ?t=3779) 
A race condition comes about when there's a possibility that you've got a database somewhere that's potentially accessed by multiple different people, and things goes wrong if people try to do things at the same time.

The example of race condition is when two person withdraw money at the same time in different ATM. So here comes the idea "transactions", it is about locking the database. Make sure that nobody else can touch the database while I'm running a transaction.


## I've Learned:
* [SQL transactions](https://www.tutorialspoint.com/postgresql/postgresql_transactions.htm) like BEGIN and COMMIT transaction.


# Example 9: list.py
* [Youtube tutorial](https://youtu.be/Eda-NmcE5mQ?t=4149)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/SQL/nestingquery.sql)


#[SQLAlchelmy](http://flask-sqlalchemy.pocoo.org/2.3/)
SQL alchemy is a Python library that is used to connect Python and SQL. To connect these two worlds and to allow Python code to be able to run SQL queries.

## Documents of SQLAlchelmy
* [Flask official document](http://flask-sqlalchemy.pocoo.org/2.3/)
* [SQLAlchelmy Glossary](https://docs.sqlalchemy.org/en/latest/glossary.html#term-dbapi)

## I've Learned:
* [How to install and make sure your SQLAlchemy version.](https://docs.sqlalchemy.org/en/13/intro.html)
 * You have to change the directory where you install SQLAlchemy(/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages) and [checking the installed SQLAlchemy version](https://docs.sqlalchemy.org/en/13/intro.html#checking-the-installed-sqlalchemy-version).
* [Getting the os environemt](https://www.jianshu.com/p/5fb5dc9d4906)
* [Creating a database engine](https://docs.sqlalchemy.org/en/latest/core/engines.html#engine-creation-api) and [connections](https://docs.sqlalchemy.org/en/13/core/connections.html#module-sqlalchemy.engine)

CSV stands for comma separated value, just an easy way to represent data. If I just give this to SQL, SQL doesn't immediately know how to understand the CSV.

Here is the example of writing Python code that reads this CSV file and and takes each row and inserts it into my table.

# Example 10: import.py
* [Youtube tutorial](https://youtu.be/Eda-NmcE5mQ?t=4511)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/SQL/import.py)


We're going to give me a text based way of looking up what passengers are on a flight. It prints out all my flights giving me their ID, their origin, their destination, and how long. And if I want to know who is on flight number two, I type in flight two, and then it says, OK, here are the passengers on flight 2.

# Example 11: passengers.py
* [Youtube tutorial](https://youtu.be/Eda-NmcE5mQ?t=4922)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/SQL/passengers.py)

After we complete the passengers.py, we want to merge with our flask applications. The example here is airline zero which is a flask application.



[DML](https://www.geeksforgeeks.org/sql-ddl-dml-dcl-tcl-commands/)

[ACID](https://zh.wikipedia.org/wiki/ACID)



* [heroku](https://www.heroku.com/postgres)

Adminer
* https://adminer.cs50.net/
* Adminer is a third party database service that lets you interact with a database online.

