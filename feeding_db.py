import mysql.connector
from csv_cleaning import csv_load, data_clean, add_planet_name

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="D4t@B3!z3d1",
    database="Kepler"
)

data = csv_load("planets.csv")
print(data.describe(), end='\n\n')
data = data_clean(data)
print(data.describe())
data = add_planet_name(data)
print(data['pl_name'].head(10))
cursor_db = db.cursor()

for columm, instance in data.iterrows():
    try:
        cursor_db.execute("insert into Corpo_Celeste values (default,'"
                          + str(instance['pl_hostname'])
                          + "',"
                          + str(instance['st_mass'])
                          + ","
                          + str(instance['st_masserr1'])
                          + ","
                          + str(instance['st_masserr2'])
                          + ","
                          + str(instance['st_rad'])
                          + ","
                          + str(instance['st_raderr1'])
                          + ","
                          + str(instance['st_raderr2'])
                          + ")")
        db.commit()
    except:
        print("Problema na adição de uma Estrela em Corpo_Celeste")
    try:
        cursor_db.execute("insert into Corpo_Celeste values (default,'"
                          + str(instance['pl_name'])
                          + "',"
                          + str(instance['pl_bmassj'])
                          + ","
                          + str(instance['pl_bmassjerr1'])
                          + ","
                          + str(instance['pl_bmassjerr2'])
                          + ","
                          + str(instance['pl_radj'])
                          + ","
                          + str(instance['pl_radjerr1'])
                          + ","
                          + str(instance['pl_radjerr2'])
                          + ")")
        db.commit()
    except:
        print("Problema na adição de um Planeta em Corpo_Celeste")
