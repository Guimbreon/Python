# MySQL Python Connector

This is a simple Python script that demonstrates how to connect to a MySQL database and retrieve data from a specific column of a specified table.

## Requirements

This script requires Python 3 and the `mysql-connector-python` package to be installed. You can install it via pip using the following command:

- Python 3.X
- pip install mysql-connector-python

## Configuration

Before running the script, you will need to modify the following variables in the code to match your MySQL database credentials:

	host = "localhost"
	user = "your_user"
	password = "password"
	database = "name"


Replace `your_user`, `password`, and `name` with your own MySQL database credentials.

## Usage

1. Clone this repository to your local machine.
2. Navigate to the cloned repository folder and run the script using the following command:

	python3 mysql_connector.py

3. Follow the prompts to select the table and column you want to retrieve data from.
4. The script will output the data from the selected column in the specified table.

## Contributing

Contributions to this repository are welcome. If you have suggestions or improvements to make, please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the GNU License - see the LICENSE.md file in the beggining of the repository.
