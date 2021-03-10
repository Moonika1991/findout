import sqlite3
import pandas as pd

con = sqlite3.connect('COVID_19.db')
cur = con.cursor()

data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data'
                   '/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv', sep=',')

col_names = data.head()

create_tab = 'CREATE TABLE covid_19 ( '

for name in col_names:
    create_tab += '"' + name + '"' + ' , '

create_tab = create_tab[:-3] + ')'


#create table
#cur.execute(create_tab)

#import data to table
data.to_sql('covid_19', con, if_exists='append', index=False)