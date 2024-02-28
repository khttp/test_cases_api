## Flask App
Develop a Flask API that exposes endpoints for managing test cases and their execution results
across multiple test assets, with data stored in a SQLite database.

## Requirements:
1. Set up a SQLite database to store test cases and their execution results with appropriate
table schema.

<img src="https://github.com/khttp/test_cases_api/blob/master/assets/testcasedbschema.png" alt="image" width="500" height="auto">

2. Create endpoints for:
   
    -  Creating a new test case and storing it in the SQLite database
    -  Retrieving a list of all test cases from the SQLite database
    -  Retrieving a single test case by its ID from the SQLite database
    -  Updating an existing test case in the SQLite database
    -  Deleting a test case by its ID from the SQLite database
    -  Recording the execution result of a test case for a specific test asset in the SQLite database
    -  Retrieving the execution results of all test cases for a specific test asset from the SQLite database
3. Implement data validation and error handling for each endpoint.
4. Write unit tests to ensure the functionality of each endpoint.


[postman documentation](https://documenter.getpostman.com/view/9645042/2sA2rFRzKX) 
