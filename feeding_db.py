import mysql.connector
from csv_cleaning import csv_load, data_clean, add_planet_name

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
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

    selSt = "select co_id from Corpo_Celeste where co_nome = '" + str(instance['pl_hostname']) + "'"
    cursor_db.execute(selSt)
    records = cursor_db.fetchall()
    idSt = records[0][0]

    try:
        cursor_db.execute("insert into Estrela values ("
                          + str(idSt)
                          + ",'"
                          + str(instance['ra_str'])
                          + "',"
                          + str(instance['ra'])
                          + ",'"
                          + str(instance['dec_str'])
                          + "',"
                          + str(instance['dec'])
                          + ","
                          + str(instance['st_dist'])
                          + ","
                          + str(instance['st_disterr1'])
                          + ","
                          + str(instance['st_disterr2'])
                          + ","
                          + str(instance['st_optmag'])
                          + ","
                          + str(instance['st_optmagerr'])
                          + ",'"
                          + str(instance['st_optband'])
                          + "',"
                          + str(instance['st_teff'])
                          + ","
                          + str(instance['st_tefferr1'])
                          + ","
                          + str(instance['st_tefferr2'])
                          + ")")
        db.commit()
    except:
        print("Problema na adição de uma Estrela em Estrela")

    selPl = "select co_id from Corpo_Celeste where co_nome = '" + str(instance['pl_name']) + "'"
    cursor_db.execute(selPl)
    records = cursor_db.fetchall()
    idPl = records[0][0]

    try:
        cursor_db.execute("insert into Planeta values ("
                          + str(idPl)
                          + ","
                          + str(idSt)
                          + ",'"
                          + str(instance['pl_discmethod'])
                          + "',"
                          + str(instance['pl_orbper'])
                          + ","
                          + str(instance['pl_orbpererr1'])
                          + ","
                          + str(instance['pl_orbpererr2'])
                          + ","
                          + str(instance['pl_orbsmax'])
                          + ","
                          + str(instance['pl_orbsmaxerr1'])
                          + ","
                          + str(instance['pl_orbsmaxerr2'])
                          + ","
                          + str(instance['pl_orbeccen'])
                          + ","
                          + str(instance['pl_orbeccenerr1'])
                          + ","
                          + str(instance['pl_orbeccenerr2'])
                          + ","
                          + str(instance['pl_orbincl'])
                          + ","
                          + str(instance['pl_orbinclerr1'])
                          + ","
                          + str(instance['pl_orbinclerr2'])
                          + ",'"
                          + str(instance['pl_bmassprov'])
                          + "',"
                          + str(instance['pl_dens'])
                          + ","
                          + str(instance['pl_denserr1'])
                          + ","
                          + str(instance['pl_denserr2'])
                          + ","
                          + str(instance['pl_ttvflag'])
                          + ","
                          + str(instance['pl_nnotes'])
                          + ",'"
                          + str(instance['rowupdate'])
                          + "')")
        db.commit()
    except:
        print("Problema na adição de um Planeta em Planeta")
