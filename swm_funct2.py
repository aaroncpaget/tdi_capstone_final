import streamlit as st
import folium
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tempfile
from io import BytesIO
import requests
import test_streamlit4_L2 as ts4


def severe_weather_map(address_in,distance, dft, dfw, dfh):
    lat, lon, ckval=ts4.geocode_latlon(address_in)
    if ckval==0: lat, lon, ckval1=geocode_latlon('1600 Pennsylvania Avenue NW, Washington, DC 20500')
    d2=distance
    latlng=(lat,lon)

    
    latsc=1/69.03
    lonsc=1/(69.03*np.cos(np.deg2rad(lat)))
    dlat=d2*latsc
    dlon=d2*lonsc
    if d2<=10: Zoom_Start_val=11
    elif d2<=20: Zoom_Start_val=10
    elif d2<=40: Zoom_Start_val=9
    elif d2<=100: Zoom_Start_val=8
    elif d2<=150: Zoom_Start_val=7
    else: Zoom_Start_val=6

    # r2, r3, r4, ckval=ts4.get_severe(address_in,distance,start_year,end_year)
    
    # base map
    map_ = folium.Map(location=latlng, zoom_start=Zoom_Start_val, prefer_canvas=True)
    folium.Marker(latlng, popup=folium.Popup(location=latlng, parse_html=True)).add_to(map_)
    (folium.CircleMarker(latlng,
                         popup=folium.Popup(location=latlng, parse_html=True),
                         radius=5,
                         color='#3186cc',
                         fill_color='#3186cc')
     .add_to(map_))

    # circle marker at address
    (folium.CircleMarker(latlng,
                         popup=folium.Popup(location=latlng, parse_html=True),
                         radius=5,
                         color='#000000',
                         fill_color='#000000')
     .add_to(map_))

    # print(dft.head(1))
    # print(dfw.head(1))
    # print(dfh.head(1))
    # ******************** wind **************************
    #print(f'{lat1} N, {lon1} E')
    # dfw=pd.read_csv('1955-2022_wind.csv', usecols=['date','yr','slat','slon','mag'])
    dfw[dfw['Wind Speed (mph)']==-9]=0
    dfw['val_name']=(dfw['Date'].astype(str) + ' Wind Speed: ' +(dfw['Wind Speed (mph)']).astype(int).astype(str) +' mph') 
    td2w=dfw
    # td2w=dfw[(dfw['slat']>=lat-d2*latsc) & (dfw['slat']<=lat+d2*latsc) & 
    #          (dfw['slon']>=lon-d2*lonsc) & (dfw['slon']<=lon+d2*lonsc) & (dfw['mag']>=46) &
    #          (dfw['yr']>=start_year) & (dfw['yr']<=end_year)]

    # dfhw=dfw[dfw["mag"]>50/1.15]
    # dfhwl=dfhw[(np.abs(dfhw["slat"]-lat)<=dlat) & (np.abs(dfhw["slon"]-lon)<=dlon) & (dfhw["yr"]>=1996)  & (dfhw["yr"]<=2022)]
    # windrating=dfhwl.groupby(['date'])["mag"].count().size/27#/(np.cos(np.deg2rad(lat))*4*dlat*dlon)
    
    feature_groupw=folium.FeatureGroup("Wind Events")
    for lata, lnga, namea in zip(td2w['Latitude'].tolist(), td2w['Longitude'].tolist(), 
                                 td2w['val_name'].tolist()  ):
        feature_groupw.add_child(folium.CircleMarker(location=[lata,lnga],popup=namea,radius=2,
                         color='#222222',
                         fill_color=False ))
    map_.add_child(feature_groupw)

    # ******************** Hail **************************
    # dfh=pd.read_csv('1955-2022_hail.csv', usecols=['date','yr','slat','slon','mag'])
    dfh[dfh['Hail Diameter (in)']==-9]=0
    dfh['val_name']=(dfh['Date'].astype(str) + ' hail size: ' +dfh['Hail Diameter (in)'].astype(str) +' in') 
    td2h=dfh
    # td2h=dfh[(dfh['slat']>=lat-d2*latsc) & (dfh['slat']<=lat+d2*latsc) & 
    #          (dfh['slon']>=lon-d2*lonsc) & (dfh['slon']<=lon+d2*lonsc) & (dfh['mag']>=0.75) &
    #          (dfh['yr']>=start_year) & (dfh['yr']<=end_year)]

    # dfhh=dfh[dfh["mag"]>(.75*0.0393701)]
    # dfhhl=dfhh[(np.abs(dfhh["slat"]-lat)<=dlat) & (np.abs(dfhh["slon"]-lon)<=dlon) & (dfhh["yr"]>=1996)  & (dfhh["yr"]<=2022)]
    # hailrating=dfhhl.groupby(['date'])["mag"].count().size/27
    
    feature_grouph=folium.FeatureGroup("Hail Events")
    for lata, lnga, namea in zip(td2h['Latitude'].tolist(), td2h['Longitude'].tolist(), 
                                 td2h['val_name'].tolist()  ):
        feature_grouph.add_child(folium.CircleMarker(location=[lata,lnga],popup=namea,radius=2,
                         color='#ff4a44',
                         fill_color='#ff4a44' ))
    map_.add_child(feature_grouph)


    # ********************* Tornadoes *********************
    # dft=pd.read_csv('1950-2022_torn.csv', usecols=['date','yr','slat','slon','mag'])
    dft[dft['EF Category']==-9]=0
    dft['val_name']=(dft['Date'].astype(str) + ' EF-' + dft['EF Category'].astype(str)) 
    td2t=dft
    # td2t=dft[(dft['slat']>=lat-d2*latsc) & (dft['slat']<=lat+d2*latsc) & 
    #          (dft['slon']>=lon-d2*lonsc) & (dft['slon']<=lon+d2*lonsc) & (dft['mag']>=1) &
    #          (dft['yr']>=start_year) & (dft['yr']<=end_year)]

    # dfht=dft[dft["mag"]>=1]
    # dfhtl=dfht[(np.abs(dfht["slat"]-lat)<=dlat) & (np.abs(dfht["slon"]-lon)<=dlon) & (dfht["yr"]>=1996)  & (dfht["yr"]<=2022)]
    # tornrating=dfhtl.groupby(['date'])["mag"].count().size/27

    feature_group=folium.FeatureGroup("Tornadoes")
    for lata, lnga, namea in zip(td2t['Latitude'].tolist(), td2t['Longitude'].tolist(), 
                                 td2t['val_name'].tolist()  ):
        feature_group.add_child(folium.CircleMarker(location=[lata,lnga],popup=namea,radius=5,
                         color='#3186cc',
                         fill_color='#3186cc',linewidth=.5, opacity=0.9 ))
    map_.add_child(feature_group)

    #******************* add selectible layer legend to map *******************
    folium.LayerControl(collapsed=False).add_to(map_)

    
    
    #show map
    return map_, ckval #, np.array([windrating,hailrating,tornrating])

