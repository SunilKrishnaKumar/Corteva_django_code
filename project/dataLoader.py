import os
import sqlite3
import pandas as pd
import numpy as np
import logging

logging.basicConfig(filename='project/logs/log_info.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

logger = logging.getLogger("mylogger")

def WeatherUpdate(data_dir, cursor):
    logger.info('Updating Weather Data DB')
    row_count = 0

    for filename in os.listdir(data_dir):
        f = os.path.join(data_dir,filename)
        df = pd.read_fwf(f, names=['date','max_temp','min_temp','precipitation'])
        s = pd.Series(filename.split('.')[0], index=range(df.shape[0]))
        df.insert(0,'station_id',s)
        df.replace(9999, np.nan, inplace=True)
        df.replace(-9999, np.nan, inplace=True)
        df['date'] = df['date'].apply(lambda x: str(x))
        df['date'] = df['date'].apply(lambda x:x[:4] + '-' + x[4:6] + '-' + x[6:])
        
        listOfEntries = cursor.execute(f"""SELECT * FROM weatherData_weather WHERE station_id == '{filename.split('.')[0]}';""").fetchall()
        row_count += cursor.rowcount
        if len(listOfEntries) > 0:
            continue
        else:
            df.to_sql('weatherData_weather', connection, if_exists='append',index=False)

    logger.info(f"Number of entries added : {row_count}") ### TODO: time logging
    

def WeatherStatsUpdate(cursor):
    
    
    logger.info('Updating Weather Data DB')
    row_count = cursor.execute(f"""SELECT COUNT(*) FROM weatherData_weatherstats;""").fetchall()[0][0]
    if row_count == 0: ##TODO
        cursor.execute(f"""INSERT INTO weatherData_weatherstats 
                       (id, station_id, avg_max_temp, avg_min_temp, total_precipitation)
                       VALUES (0,'TRIAL', NULL,NULL,NULL);""")
    cursor.execute(f"""INSERT INTO weatherData_weatherstats 
                   SELECT NULL, station_id, 
                   round(avg(max_temp)/10,2) as avg_max_temp, 
                   round(avg(min_temp)/10,2) as avg_min_temp, 
                   sum(precipitation)/100 as total_precipitation 
                   from weatherData_weather GROUP by station_id;""")
    cursor.execute("""DELETE FROM weatherData_weatherstats
                        WHERE station_id = 'trial';""")
    row_count = cursor.execute(f"""SELECT COUNT(*) FROM weatherData_weatherstats;""").fetchall()[0][0]
    logger.info(f"Number of entries added : {row_count}") ### TODO: time logging
    
    
    


if __name__ == "__main__":
    data_dir = '/Users/sunil/Documents/Corteva/project/wx_data'
    connection = sqlite3.connect('/Users/sunil/Documents/Corteva/project/db.sqlite3')
    cursor = connection.cursor()
    # WeatherUpdate(data_dir, cursor)
    WeatherStatsUpdate(cursor)
    connection.commit()
    connection.close()
    
