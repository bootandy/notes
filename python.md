## Style:
* Dont add __init__.py unless you need that dir to be a package.
* If you access a property or dictionary reference 3 times or more then pull it out into a variable.
* [Don't use `select *`](https://stackoverflow.com/questions/3639861/why-is-select-considered-harmful) when dealing with an SQL database

* [Gist of python mistakes](https://gist.github.com/bootandy/6fee9cf5f6e1cfc4484b0205464fee4f)#


## Generic Notes:
#### Print stack trace without exception being raised
* `traceback.print_stack()`

#### Python repeatable hashing: PYTHONHASHSEED
* [PythonHashSeed](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED)
allows repeatable hashing, such as for self tests for the interpreter itself, or to allow a cluster of python processes to share hash values.

#### Generator: yield from
* `yield from g` == `for v in g: yield v`

## Other:
* [Old Mock Gotchas](https://alexmarandon.com/articles/python_mock_gotchas/)

#### SQLAlchmey:
* [Common SQL ALchmey misunderstandings](http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
* **Query.one()** executes the query and raises MultipleResultsFound if the number of rows was more than 1, and NoResultFound no rows were found. Otherwise it returns the sole result row (as tuple)
* **Query.first()** executes the query with LIMIT 1 and returns the result row as tuple, or None if no rows were found
* **Query.scalar()** executes the query and raises MultipleResultsFound  if the number of rows was more than 1. If no rows were found, it returns None. Otherwise it returns the first column of the sole result row. 


## How 2 upload to PyPi:
* Build it:
  * python setup.py sdist

* Register it:
  * twine register dist/project_name-x.y.z.tar.gz
  * twine register dist/mypkg-0.1-py2.py3-none-any.whl

* Upload it:
	* twine upload dist/*
