# Bank Total Calculator

This is a Python script that calculates the total amount of money earned by clients in a bank, taking into account their earnings percentage and returns.

## Requirements

- Python 3.x
- mysql-connector-python

## Installation

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up a MySQL database with the required schema.
4. Update the `mydb` variable in the code with your MySQL database credentials.
5. Run the script using `python bank_total_calculator.py`.

## Usage

1. The script connects to a MySQL database and retrieves data from the `people`, `earnings`, and `money` tables.
2. The script calculates the total amount of money earned by clients by multiplying their earnings percentage and returns with their respective money values and adding them up.
3. The script then compares the calculated total with the current total stored in the `money` table.
4. If the totals match, the script displays a message saying that the values haven't changed.
5. If the totals don't match, the script updates the `new` and `old` columns in the `money` table with the calculated and previous total values, respectively.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the GNU License - see the LICENSE.md file in the beggining of the repository.
