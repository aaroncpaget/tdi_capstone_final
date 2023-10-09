import psycopg2
import sys
import os

# Available functions in this document
# r1=databases_slim4.get_raw_clim(latitude,longitude)
# r2=databases_slim4.get_raw_torn(latitude,longitude,diff,yr1,yr2)
# r3=databases_slim4.get_raw_wind(latitude,longitude,diff,yr1,yr2)
# r4=databases_slim4.get_raw_hail(latitude,longitude,diff,yr1,yr2)
# r6=databases_slim4.get_raw_cloudy(latitude,longitude)

def get_raw_clim(latitude,longitude):
    latitude1=round(latitude,1)
    longitude1=round(longitude,1)

    query_raw_clim=f"SELECT * FROM public.climate_all WHERE lat={latitude1} AND lon={longitude1} ORDER BY month;"

#     sql_connect_string = os.getenv("DB_URL")

    db_params={'dbname':'tdi_project_paget',
              'user':'tdi_project_paget_user',
              'password':'vuzGpp2mkBShGr2zzPZzyDw6d7BR57En',
              'host':'dpg-ck2dhs7qj8ts73e37550-a.oregon-postgres.render.com',
              'port': '5432'}

    try:
        conn=psycopg2.connect(**db_params)

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        
    cur=conn.cursor()

    try:
        cur.execute(query_raw_clim)
        results1=cur.fetchall()
        # print('r1')

    except psycopg2.Error as e:
        print("Error executing the quere:", e)
        conn.close()
#     returned values in order (12,17)
#     month         
#     lat           
#     lon           
#     rhmax         
#     rhmin         
#     ws_avg        
#     pr_avg        
#     pr_days       
#     t_avg         
#     tmax_mean     
#     t_max         
#     t_above90     
#     t_above100    
#     tmin_mean     
#     t_min         
#     t_below0     
#     t_below32              
    return results1


def get_raw_torn(latitude,longitude,diff,yr1,yr2):

    query_raw_torn=f"SELECT * FROM public.torn_data WHERE slat>={latitude-diff} AND slat<={latitude+diff} AND slon>= {longitude-diff} AND slon<={longitude+diff} AND yr>= {yr1} AND yr<= {yr2} AND mag>= 1 ORDER BY yr;"

#     sql_connect_string = os.getenv("DB_URL")

    db_params={'dbname':'tdi_project_paget',
              'user':'tdi_project_paget_user',
              'password':'vuzGpp2mkBShGr2zzPZzyDw6d7BR57En',
              'host':'dpg-ck2dhs7qj8ts73e37550-a.oregon-postgres.render.com',
              'port': '5432'}

    try:
        conn=psycopg2.connect(**db_params)

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        
    cur=conn.cursor()

    try:
        cur.execute(query_raw_torn)
        results2=cur.fetchall()

    except psycopg2.Error as e:
        print("Error executing the quere:", e)
        conn.close()
        
    # return results1, results2
    return results2




def get_raw_wind(latitude,longitude,diff,yr1,yr2):

    query_raw_wind=f"SELECT * FROM public.wind_data WHERE slat>={latitude-diff} AND slat<={latitude+diff} AND slon>= {longitude-diff} AND slon<={longitude+diff} AND yr>= {yr1} AND yr<= {yr2} AND mag>= 50 ORDER BY yr;"

#     sql_connect_string = os.getenv("DB_URL")

    db_params={'dbname':'tdi_project_paget',
              'user':'tdi_project_paget_user',
              'password':'vuzGpp2mkBShGr2zzPZzyDw6d7BR57En',
              'host':'dpg-ck2dhs7qj8ts73e37550-a.oregon-postgres.render.com',
              'port': '5432'}

    try:
        conn=psycopg2.connect(**db_params)

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)

    cur=conn.cursor()

    try:
        cur.execute(query_raw_wind)
        results3=cur.fetchall()

    except psycopg2.Error as e:
        print("Error executing the quere:", e)
        conn.close()
        
    # return results1, results2
    return results3





def get_raw_hail(latitude,longitude,diff,yr1,yr2):

    query_raw_hail=f"SELECT * FROM public.hail_data WHERE slat>={latitude-diff} AND slat<={latitude+diff} AND slon>= {longitude-diff} AND slon<={longitude+diff} AND yr>= {yr1} AND yr<= {yr2} AND mag>= 0.75 ORDER BY yr;"

#     sql_connect_string = os.getenv("DB_URL")

    db_params={'dbname':'tdi_project_paget',
              'user':'tdi_project_paget_user',
              'password':'vuzGpp2mkBShGr2zzPZzyDw6d7BR57En',
              'host':'dpg-ck2dhs7qj8ts73e37550-a.oregon-postgres.render.com',
              'port': '5432'}

    try:
        conn=psycopg2.connect(**db_params)

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        
    cur=conn.cursor()

    try:
        cur.execute(query_raw_hail)
        results4=cur.fetchall()

    except psycopg2.Error as e:
        print("Error executing the quere:", e)
        conn.close()
        
    # return results1, results2
    return results4




def get_raw_cloudy(latitude,longitude):
    latitude25=(round(latitude*4)/4+0.125)
    longitude25=(round(longitude*4)/4+0.125)

    query_raw_cloudy=f"SELECT * FROM public.cloudy_25 WHERE lat={latitude25} AND lon={longitude25} ORDER BY month;"

#     sql_connect_string = os.getenv("DB_URL")

    db_params={'dbname':'tdi_project_paget',
              'user':'tdi_project_paget_user',
              'password':'vuzGpp2mkBShGr2zzPZzyDw6d7BR57En',
              'host':'dpg-ck2dhs7qj8ts73e37550-a.oregon-postgres.render.com',
              'port': '5432'}

    try:
        conn=psycopg2.connect(**db_params)

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        
    cur=conn.cursor()

    try:
        cur.execute(query_raw_cloudy)
        results6=cur.fetchall()

    except psycopg2.Error as e:
        print("Error executing the quere:", e)
        conn.close()
        
    return results6





