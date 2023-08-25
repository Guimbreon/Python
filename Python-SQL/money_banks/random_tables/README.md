# Bank Project

This project is a Python script that creates and populates a MySQL database for a bank, using the `mysql.connector` module. It consists of three tables: `people`, `earnings`, and `money`.

## Requirements

To run this script, you need to have Python 3 installed and the `mysql-connector-python` package installed. You also need to have a MySQL server set up.

## Installation

1. Clone the repository to your local machine.
2. In the project directory, run the command `pip install mysql-connector-python`.
3. Open the `bank.py` file and edit the following lines with your MySQL server information:
    ```
    host = "localhost"
    user = "user"
    password = "password"
    database = "bank"
    ```
4. Run the `bank.py` file.

## Tables

### People

The `people` table contains two columns: `id` and `money`. The `id` column is an integer primary key, and the `money` column is an integer that represents the amount of money each person has in the bank.

### Earnings

The `earnings` table contains three columns: `id`, `perc`, and `returns`. The `id` column is an integer primary key, and the `perc` column is a float that represents the percentage of earnings. The `returns` column is a float that represents the actual amount of earnings.

### Money

The `money` table contains three columns: `id`, `old`, and `new`. The `id` column is an integer primary key, and the `old` and `new` columns are floats that represent the previous and current amounts of money in the bank.

## License

This project is licensed under the GNU License - see the LICENSE.md file in the beggining of the repository.

