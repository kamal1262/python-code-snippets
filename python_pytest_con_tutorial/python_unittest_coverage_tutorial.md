
Link to the tutorial: https://www.youtube.com/watch?v=7BJ_BKeeJyM


unittest 
- pytest
- coverage.py 
- pytest-cov 

With all these things I achieve 100% Test Coverage in Python.
100% test coverage is the same as 100% code coverage, but from the perspective of your tests.

## Steps in this video
- Create files app.py and test_app.py
- import unittest into test_app.py
- create unit tests for non existent Fibonacci function
- test, test fails
- create Fibonacci function,
- test passes.
- install pytest with $ pip install pytest
- run test using pytest
- install coverage with $ pip install coverage

*run*
```
$ coverage run app.py  #analyses file
$ coverage report -m    #outputs anaylsys and shows un covered lines
$ coverage html           # create a more concise html version of the report
I try out a few things and get 10% code coverage
I then install pytest-cov using
$ pip install pytest-cov
I then run 
$ pytest --cov=app
and modify the test_app.py file until I get 100% code coverage
I also generate a html version of the report using
$ pytest --cov=app --cov-report=html
```
