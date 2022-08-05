import pandas as pd


# returns a local csv
def csv_load(address):
    return pd.read_csv(address)

# drops certain columns of the data frame, only the ones used on the database will ramain
def data_clean(data):
    data.drop(labels=['rowid', 'pl_orbperlim', 'pl_orbsmaxlim', 'pl_orbeccenlim', 'pl_orbincllim', 'pl_bmassjlim',
                      'pl_radjlim', 'pl_denslim', 'st_distlim', 'st_optmaglim', 'st_optmagblend',
                      'st_tefflim', 'st_masslim', 'st_radlim', 'pl_kepflag', 'pl_k2flag'], axis=1, inplace=True)
    data = data.fillna('null')
    return data

# adds a new column, wich is the name of the planet (name of the star + the planet letter)
def add_planet_name(data):
    for instance in data:
        data['pl_name'] = data['pl_hostname'] + ' ' + data['pl_letter']
    return data
