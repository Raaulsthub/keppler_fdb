from csv_cleaning import csv_load, data_clean
from sql_connector import db_cursor

data = csv_load("planets.csv")
print(data.describe(), end='\n\n')
print(data_clean(data).describe())
# cursor_db = db_cursor("", "")

