# SQL

## Mistakes:
#### Bad Update:
This SQL doesn't do what you might think. It will update all entries in Exam_Result not just andy's exams
```
update Exam_Result set score = 99 FROM Student s, Exam_Result er WHERE s.id = er.student_id and s.name='andy'; 
```
This is what you wanted to do:
```
update Exam_Result set score = 99 FROM Student s WHERE s.id = Exam_Result.student_id and s.name='andy';
```


And this is how to fix it from a DB backup via CSV after it has gone wrong:

```
\copy Exam_Result (exam_id, student_id, score) to out.csv CSV;
create table fix(exam_id int, student_id int, score int);
\copy fix from out.csv CSV;
update Exam_Result set score = f.score FROM fix f where f.exam_id=Exam_Result.exam_id and f.student_id=Exam_Result.student_id;
```
## Sample SQL
#### Test if there is a null in a PG array
`
select exists (
    select 1 
    from unnest(array[1, null]) s(a)
    where a is null
);
`
#### OnConflict / Upsert:
(PostgreSQL >= 9.5) Allows this:
```
INSERT INTO users (id, level)
VALUES (1, 0)
ON CONFLICT (id) DO UPDATE
SET level = users.level + 1;
```



# Postgres:
## Performance:
Background: Our upgrade to Postgresql 10 went badly due to parallel queries. 
If  Postgres 10 performance sucks then try turning off parallel queries.

[This site generates a tuned pg config](https://pgtune.leopard.in.ua/#/) for you based on your system:

## Indexes:
##### Postgres primary key sorted in the reverse order. Will it use the index efficiently?
[PG: Yes, OtherDB: Maybe](https://dba.stackexchange.com/questions/19797/postgres-primary-key-sorted-in-the-reverse-order-will-it-use-the-index-efficien)
##### Cluster:
CLUSTER instructs PostgreSQL to cluster the table specified by table_name based on the index specified by index_name.
The index must already have been defined on table_name.
Data is physically reordered

## Functions:
#### Create Function: IMMUTABLE STABLE VOLATILE
* IMMUTABLE [default] indicates that the function cannot modify the database and always returns the same result, it is immediately replaced with the function value.
* STABLE indicates that the function cannot modify the database, and that within a single table scan it will consistently return the same result for the same argument values
* VOLATILE indicates that the function value can change even within a single table scan, so no optimizations can be made. (eg: time functions)
[Doc](https://www.postgresql.org/docs/current/sql-createfunction.html)

## Backups:
Attempt  to configure your Wall-E database backup 
 * So they back up on a a time frequency not size frequency by tuning:  max_wal_size

## PG Logging:
Things you really should turn on for your [PG logs](https://www.postgresql.org/docs/9.5/runtime-config-logging.html)
#### log_lock_waits 
* This is useful in determining if lock waits are causing poor performance.
#### log_statement(ddl)
* Logs statements changing the DB
#### log_min_duration_statement
* Causes the duration of each completed statement to be logged if the  statement ran for at least the specified number of milliseconds.  


 
