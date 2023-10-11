import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import databases_slim4
import math


# get_fig1(address_in)
# get_fig2(address_in)
# get_fig3(address_in)
# get_fig4(address_in)
# get_severe(address_in,diff,yr1,yr2)

# r1=databases_slim4.get_raw_clim(latitude,longitude)
# r2=databases_slim4.get_raw_torn(latitude,longitude,diff,yr1,yr2)
# r3=databases_slim4.get_raw_wind(latitude,longitude,diff,yr1,yr2)
# r4=databases_slim4.get_raw_hail(latitude,longitude,diff,yr1,yr2)
# r5=databases_slim4.get_raw_rhws(latitude,longitude)
# r6=databases_slim4.get_raw_cloudy(latitude,longitude)
# r7=databases_slim4.get_raw_pcounts(latitude,longitude)

# month, lat, lon, rhmax, rhmin, ws_avg, pr_avg, pr_days, t_avg, tmax_mean, t_max, t_above90, t_above100, tmin_mean, t_min, t_below32, t_below0
# 0      1    2    3      4      5       6       7        8      9          10     11         12          13         14     15         16    
# r1 (climate) - month, lat, lon, p_mean, tmax_mean, tmin_mean, tavg_mean, t_max, t_min, t_below32, t_below0, t_above50
# r2 (tornado) - # yr, mo, dy, date, mag, lat, lon
# r3 (wind) - # yr, date, mag, lat, lon
# r4 (hail) - # yr, date, mag, lat, lon
# r6 (sunny) - # month, lat, lon, srad_cloudy, srad_pcloudy, srad_sunny

def get_fig1(address_in):
    latitude, longitude, ckval=geocode_latlon(address_in)
    if ckval==0: latitude, longitude, ckval1=geocode_latlon('1600 Pennsylvania Avenue NW, Washington, DC 20500')
    r1=databases_slim4.get_raw_clim(latitude,longitude)
    # r5=databases_slim4.get_raw_rhws(latitude,longitude)
    if (len(r1)<12):
        ckval=0

    if (ckval==1):
    
        months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        
        # make Temperature, Wind, and RH plots
        fig1, (ax1,ax3)=plt.subplots(ncols=1,nrows=2,layout='constrained',figsize=(5, 8),gridspec_kw={'height_ratios': [3, 1]})
        y11=np.squeeze(np.array(r1)[:, 9])
        y22=np.squeeze(np.array(r1)[:,13])
        ax1.plot(months,np.squeeze(np.array(r1)[:, 8]),linestyle='-',color='k',label='Average Temperature')
        ax1.fill_between([0,1,2,3,4,5,6,7,8,9,10,11],y22,y11,hatch='..',alpha=0.1,color='b', label='Average Temperature Range')
        ax1.plot(months,np.squeeze(np.array(r1)[:,10]),linestyle='-',color='r',label='Record High/Low')
        ax1.legend(loc='lower center', fontsize="9")
        ax1.plot(months,np.squeeze(np.array(r1)[:,14]),linestyle='-',color='r',label='Minimum Temperature')
        ax1.plot(months,np.squeeze(np.array(r1)[:, 9]),linestyle='-',color='b',label='Average High')
        ax1.plot(months,np.squeeze(np.array(r1)[:,13]),linestyle='-',color='b',label='Average Low')
        vrng=(np.max(np.squeeze(np.array(r1)[:,10]))-np.min(np.squeeze(np.array(r1)[:,14])))/10
        ax1.set_ylim([np.min(np.squeeze(np.array(r1)[:,14]))-1.5*vrng, vrng+np.max(np.squeeze(np.array(r1)[:,10]))])
        ax1.set_title('Monthly Average Temperatures')
        ax1.set_xlabel('Month')
        ax1.set_ylabel('Temperature (°F)')
        ax1.yaxis.grid(True,linestyle='--')
        
        ax3.plot(months,np.squeeze(np.array(r1)[:,3]),linestyle='-',color='b',label='Average Max')
        ax3.plot(months,np.squeeze(np.array(r1)[:,4]),linestyle='-',color='r',label='Average Min')
        ax3.legend(loc='lower center', fontsize="10")
        ax3.set_ylim([0,np.ceil(1.2*np.max(np.array(r1)[:,3]))])
        ax3.set_title('Monthly Average Relative Humidity')
        ax3.set_xlabel('Month')
        ax3.set_ylabel('Relative Humidity (%)')
        ax3.yaxis.grid(True,linestyle='--')

    else: 
        fig1, (ax1,ax3)=plt.subplots(ncols=1,nrows=2,layout='constrained',figsize=(5, 8),gridspec_kw={'height_ratios': [3, 1]})

    return fig1, ckval

#****************************************************************************************************************
def get_fig1_2(address_in1, address_in2):
    latitude, longitude, ckval1=geocode_latlon(address_in1)
    if ckval1==0: latitude, longitude, ckval11=geocode_latlon('1600 Pennsylvania Avenue NW, Washington, DC 20500')
    r1=databases_slim4.get_raw_clim(latitude,longitude)
    latitude, longitude, ckval2=geocode_latlon(address_in2)
    if ckval2==0: latitude, longitude, ckval21=geocode_latlon('1600 Pennsylvania Avenue NW, Washington, DC 20500')
    r2=databases_slim4.get_raw_clim(latitude,longitude)
    # r5=databases_slim4.get_raw_rhws(latitude,longitude)
    if (len(r1)<12):
        ckval1=0
    if (len(r2)<12):
        ckval2=0
    if (ckval1==1) & (ckval2==1):

        months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    
        ll=np.minimum(np.min(np.squeeze(np.array(r1)[:,14])),np.min(np.squeeze(np.array(r2)[:,14])) )
        uu=np.maximum(np.max(np.squeeze(np.array(r1)[:,10])),np.max(np.squeeze(np.array(r2)[:,10])) )
        vrng=(uu-ll)/10
        
        # make Temperature, Wind, and RH plots
        fig1, ((ax1, ax2),(ax3,ax4))=plt.subplots(2,2,figsize=(8,8),layout='constrained',gridspec_kw={'height_ratios':[3,1],'width_ratios':[1,1]})
        ax1.plot(months,np.squeeze(np.array(r1)[:, 8]),linestyle='-',color='k',label='Average Temperature')
        ax1.fill_between(months,np.squeeze(np.array(r1)[:, 9]),np.squeeze(np.array(r1)[:,13]),hatch='..',alpha=0.1,color='b', label='Average Temperature Range')
        ax1.plot(months,np.squeeze(np.array(r1)[:,10]),linestyle='-',color='r',label='Record High/Low')
        ax1.legend(loc='lower center', fontsize="9")
        ax1.plot(months,np.squeeze(np.array(r1)[:,14]),linestyle='-',color='r',label='Minimum Temperature')
        ax1.plot(months,np.squeeze(np.array(r1)[:, 9]),linestyle='-',color='b',label='Average High')
        ax1.plot(months,np.squeeze(np.array(r1)[:,13]),linestyle='-',color='b',label='Average Low')
        ax1.set_ylim([ll-1.5*vrng, 0.5*vrng+uu])
        ax1.set_title(f'{address_in1.split(",")[0]} \n Monthly Average Temperatures')
        ax1.set_xlabel('Month')
        ax1.set_ylabel('Temperature (°F)')
        ax1.set_xticks(months)
        ax1.set_xticklabels(months,rotation=45)
        ax1.yaxis.grid(True,linestyle='--')
        
        ax2.plot(months,np.squeeze(np.array(r2)[:, 8]),linestyle='-',color='k',label='Average Temperature')
        ax2.fill_between(months,np.squeeze(np.array(r2)[:, 9]),np.squeeze(np.array(r2)[:,13]),hatch='..',alpha=0.1,color='b', label='Average Temperature Range')
        ax2.plot(months,np.squeeze(np.array(r2)[:,10]),linestyle='-',color='r',label='Record High/Low')
        ax2.legend(loc='lower center', fontsize="9")
        ax2.plot(months,np.squeeze(np.array(r2)[:,14]),linestyle='-',color='r',label='Minimum Temperature')
        ax2.plot(months,np.squeeze(np.array(r2)[:, 9]),linestyle='-',color='b',label='Average High')
        ax2.plot(months,np.squeeze(np.array(r2)[:,13]),linestyle='-',color='b',label='Average Low')
        ax2.set_ylim([ll-1.5*vrng, 0.5*vrng+uu])
        ax2.set_title(f'{address_in2.split(",")[0]} \n Monthly Average Temperatures')
        ax2.set_xlabel('Month')
        ax2.set_ylabel('Temperature (°F)')
        ax2.set_xticks(months)
        ax2.set_xticklabels(months,rotation=45)
        ax2.yaxis.grid(True,linestyle='--')
        
        
        ax3.plot(months,np.squeeze(np.array(r1)[:,3]),linestyle='-',color='b',label='Average Max')
        ax3.plot(months,np.squeeze(np.array(r1)[:,4]),linestyle='-',color='r',label='Average Min')
        ax3.legend(loc='lower center', fontsize="10")
        ax3.set_ylim([0,np.ceil(1.2*np.max(np.array(r1)[:,3]))])
        ax3.set_title('Monthly Average Relative Humidity')
        ax3.set_xlabel('Month')
        ax3.set_ylabel('Relative Humidity (%)')
        ax3.set_xticks(months)
        ax3.set_xticklabels(months,rotation=45)
        ax3.yaxis.grid(True,linestyle='--')
        
        ax4.plot(months,np.squeeze(np.array(r2)[:,3]),linestyle='-',color='b',label='Average Max')
        ax4.plot(months,np.squeeze(np.array(r2)[:,4]),linestyle='-',color='r',label='Average Min')
        ax4.legend(loc='lower center', fontsize="10")
        ax4.set_ylim([0,np.ceil(1.2*np.max(np.array(r2)[:,3]))])
        ax4.set_title('Monthly Average Relative Humidity')
        ax4.set_xlabel('Month')
        ax4.set_ylabel('Relative Humidity (%)')
        ax4.set_xticks(months)
        ax4.set_xticklabels(months,rotation=45)
        ax4.yaxis.grid(True,linestyle='--')

    else:
        fig1, (ax1,ax3)=plt.subplots(ncols=1,nrows=2,layout='constrained',figsize=(5, 8),gridspec_kw={'height_ratios': [3, 1]})
        
    return fig1, ckval1, ckval2

#****************************************************************************************************************
def get_fig2(address_in):
    latitude, longitude, ckval=geocode_latlon(address_in)
    if ckval==0: latitude, longitude, ckval1=geocode_latlon('1600 Pennsylvania Avenue NW, Washington, DC 20500')
    r1=databases_slim4.get_raw_clim(latitude,longitude)

    if (len(r1)<12):
        ckval=0

    if (ckval==1):
    
        months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        
        # make Temperature, Wind, and RH plots
        # make Monthly Precip and Number of Rainy Days plot
        v21=np.array([31,28.25,31,30,31,30,31,31,30,31,30,31])*np.squeeze(np.array(r1)[:,6])/25.4
        v22=np.array([31,28.25,31,30,31,30,31,31,30,31,30,31])*np.squeeze(np.array(r1)[:,7])
        s21='{:.1f}'.format(np.sum(v21))
        s22='{:.1f}'.format(np.sum(v22))
    
        bbox_props=dict(boxstyle='round',facecolor='lightyellow',alpha=0.7,edgecolor='k')
        
        fig2, (ax21,ax22)=plt.subplots(ncols=1,nrows=2,layout='constrained')
        
        # ax21.plot(months,np.squeeze(np.array(r1)[:,3]),linestyle='-',color='b',label='Monthly Average Precipitation')
        ax21.bar(months,v21,label='Monthly Average Precipitation')
        ax21.set_ylim([0, np.ceil( 1.3*np.max(v21) ) ])
        ax21.set_title('Monthly Average Precipitation')
        ax21.set_xlabel('Month')
        ax21.set_ylabel('Equivalent Water (in)')
        ax21.yaxis.grid(True,linestyle='--')
        ax21.text(0.5,0.90,f'Annual Total: {s21} inches',transform=ax21.transAxes,ha='center',fontsize=10,bbox=bbox_props)
        
        # ax22.plot(months,np.squeeze(np.array(r7)[:,3]),linestyle='-',color='b',label='Number of Rainy Days')
        ax22.bar(months,v22,label='Number of "Rainy" Days')
        ax22.set_title('Average Number of Days with Precipitation')
        ax22.set_xlabel('Month')
        ax22.set_ylabel('Number of Days')
        ax22.set_ylim([0, np.ceil(np.max(v22*1.3)) ])
        ax22.yaxis.grid(True,linestyle='--')
        ax22.text(0.5,0.90,f'Total: {s22} days',transform=ax22.transAxes,ha='center',fontsize=10,bbox=bbox_props)

    else: 
        fig2, (ax1,ax3)=plt.subplots(ncols=1,nrows=2,layout='constrained',figsize=(5, 8),gridspec_kw={'height_ratios': [3, 1]})

    return fig2, ckval

#****************************************************************************************************************
def get_fig2_2(address_in1, address_in2):
    latitude, longitude, ckval1=geocode_latlon(address_in1)
    if ckval1==0: latitude, longitude, ckval11=geocode_latlon('1600 Pennsylvania Avenue NW, Washington, DC 20500')
    r1=databases_slim4.get_raw_clim(latitude,longitude)
    latitude, longitude, ckval2=geocode_latlon(address_in2)
    if ckval2==0: latitude, longitude, ckval21=geocode_latlon('1600 Pennsylvania Avenue NW, Washington, DC 20500')
    r2=databases_slim4.get_raw_clim(latitude,longitude)

    if (len(r1)<12):
        ckval1=0
    if (len(r2)<12):
        ckval2=0
    if (ckval1==1) & (ckval2==1):

        months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        uu=np.maximum(np.max(np.squeeze(np.array(r1)[:,6])),np.max(np.squeeze(np.array(r2)[:,6])) )
    
        # make Temperature, Wind, and RH plots
        # make Monthly Precip and Number of Rainy Days plot
        # fig2, (ax21,ax22)=plt.subplots(ncols=1,nrows=2,layout='constrained')
        v21=np.array([31,28.25,31,30,31,30,31,31,30,31,30,31])*np.squeeze(np.array(r1)[:,6])/25.4
        v22=np.array([31,28.25,31,30,31,30,31,31,30,31,30,31])*np.squeeze(np.array(r2)[:,6])/25.4
        v23=np.array([31,28.25,31,30,31,30,31,31,30,31,30,31])*np.squeeze(np.array(r1)[:,7])
        v24=np.array([31,28.25,31,30,31,30,31,31,30,31,30,31])*np.squeeze(np.array(r2)[:,7])
        s21='{:.1f}'.format(np.sum(v21))
        s22='{:.1f}'.format(np.sum(v22))
        s23='{:.1f}'.format(np.sum(v23))
        s24='{:.1f}'.format(np.sum(v24))
    
        bbox_props=dict(boxstyle='round',facecolor='lightyellow',alpha=0.7,edgecolor='k')
    
        fig2, ((ax21, ax22),(ax23,ax24))=plt.subplots(2,2,figsize=(8,8),layout='constrained',gridspec_kw={'height_ratios':[1,1],'width_ratios':[1,1]})
        
        # ax21.plot(months,np.squeeze(np.array(r1)[:,3]),linestyle='-',color='b',label='Monthly Average Precipitation')
        ax21.bar(months,v21,label='Monthly Average Precipitation')
        ax21.set_ylim([0, np.ceil( 1.3*uu) ])
        ax21.set_title(f'{address_in1.split(",")[0]} \n Monthly Average Precipitation')
        ax21.set_xlabel('Month')
        ax21.set_ylabel('Equivalent Water (in)')
        ax21.yaxis.grid(True,linestyle='--')
        ax21.set_xticks(months)
        ax21.set_xticklabels(months,rotation=45)
        ax21.text(0.5,0.90,f'Annual Total: {s21} inches',transform=ax21.transAxes,ha='center',fontsize=10,bbox=bbox_props)
        
        ax22.bar(months,v22,label='Monthly Average Precipitation')
        ax22.set_ylim([0, np.ceil( 1.3*uu) ])
        ax22.set_title(f'{address_in2.split(",")[0]} \n Monthly Average Precipitation')
        ax22.set_xlabel('Month')
        ax22.set_ylabel('Equivalent Water (in)')
        ax22.yaxis.grid(True,linestyle='--')
        ax22.set_xticks(months)
        ax22.set_xticklabels(months,rotation=45)
        ax22.text(0.5,0.90,f'Annual Total: {s22} inches',transform=ax22.transAxes,ha='center',fontsize=10,bbox=bbox_props)
    
        # ax22.plot(months,np.squeeze(np.array(r7)[:,3]),linestyle='-',color='b',label='Number of Rainy Days')
        ax23.bar(months,v23,label='Number of "Rainy" Days')
        ax23.set_title('Average Number of Days with Precipitation')
        ax23.set_xlabel('Month')
        ax23.set_ylabel('Number of Days')
        ax23.set_ylim([0, 31])
        ax23.yaxis.grid(True,linestyle='--')
        ax23.set_xticks(months)
        ax23.set_xticklabels(months,rotation=45)
        ax23.text(0.5,0.90,f'Total: {s23} days',transform=ax23.transAxes,ha='center',fontsize=10,bbox=bbox_props)
    
        ax24.bar(months,v24,label='Number of "Rainy" Days')
        ax24.set_title('Average Number of Days with Precipitation')
        ax24.set_xlabel('Month')
        ax24.set_ylabel('Number of Days')
        ax24.set_ylim([0, 31 ])
        ax24.yaxis.grid(True,linestyle='--')
        ax24.set_xticks(months)
        ax24.set_xticklabels(months,rotation=45)
        ax24.text(0.5,0.90,f'Total: {s24} days',transform=ax24.transAxes,ha='center',fontsize=10,bbox=bbox_props)

    else:
        fig2, (ax1,ax3)=plt.subplots(ncols=1,nrows=2,layout='constrained',figsize=(5, 8),gridspec_kw={'height_ratios': [3, 1]})

    return fig2, ckval1, ckval2

#****************************************************************************************************************
def get_fig3(address_in):
    latitude, longitude, ckval=geocode_latlon(address_in)
    if ckval==0: latitude, longitude, ckval1=geocode_latlon('1600 Pennsylvania Avenue NW, Washington, DC 20500')
    r1=databases_slim4.get_raw_cloudy(latitude,longitude)
    adh1=np.zeros(12)
    for i in range(0,12,1): adh1[i]=average_daylight_hours(latitude,i+1)
    
    if (len(r1)<12):
        ckval=0

    if (ckval==1):
        months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        
        # make Sunny Days and Daylight hours plot
        fig3, (ax31,ax32)=plt.subplots(ncols=1,nrows=2,layout='constrained')
        
        dict1={"Sunny": np.array(r1)[:,5],"Partly Cloudy":  np.array(r1)[:,4], "Cloudy": np.array(r1)[:,3] }
        c=['#FFCC00','#77CEEB','#808080']
        width=0.25
        multiplier=0
        cind=0
        x=np.arange(len(months))
        for boolean, dictvals in dict1.items():
            offset=width*multiplier
            rects=ax31.bar(x+offset,dictvals,width=width,label=boolean, bottom=np.zeros(12),color=c[cind])
            # rects=ax31.bar(x+offset,dictvals,width=width, bottom=np.zeros(12))
            # ax31.bar_label(rects, padding=3)
            multiplier+=1
            cind+=1
        ax31.legend(loc='upper right', ncols=3)
        ax31.set_title('Expected Sky Conditions')
        ax31.set_xticks(x+width/(multiplier), months)
        ax31.set_xlabel('Month')
        ax31.set_ylabel('Days of Month (%)')
        ax31.set_ylim([0, 100])
        ax31.yaxis.grid(True,linestyle='--')
        
        #    ax32.plot(months,adh,linestyle='-',color='b',label='Average Daylight Hours')
        ax32.bar(months,adh1,label='Average Daylight Hours')
        ax32.set_ylim([0, np.ceil(np.max(1.2*adh1))])
        ax32.set_title('Average Daylight Hours')
        ax32.set_xlabel('Month')
        ax32.set_ylabel('Hours per Day')
        ax32.yaxis.grid(True,linestyle='--')

    else: 
        fig3, (ax1,ax3)=plt.subplots(ncols=1,nrows=2,layout='constrained',figsize=(5, 8),gridspec_kw={'height_ratios': [3, 1]})

    return fig3, ckval

#****************************************************************************************************************
def get_fig3_2(address_in1,address_in2):
    latitude, longitude, ckval1=geocode_latlon(address_in1)
    if ckval1==0: latitude, longitude, ckval11=geocode_latlon('1600 Pennsylvania Avenue NW, Washington, DC 20500')
    r1=databases_slim4.get_raw_cloudy(latitude,longitude)
    adh1=np.zeros(12)
    for i in range(0,12,1): adh1[i]=average_daylight_hours(latitude,i+1)

    latitude, longitude, ckval2=geocode_latlon(address_in2)
    if ckval2==0: latitude, longitude, ckval21=geocode_latlon('1600 Pennsylvania Avenue NW, Washington, DC 20500')
    r2=databases_slim4.get_raw_cloudy(latitude,longitude)
    adh2=np.zeros(12)
    for i in range(0,12,1): adh2[i]=average_daylight_hours(latitude,i+1)
 
    if (len(r1)<12):
        ckval1=0
    if (len(r2)<12):
        ckval2=0
    if (ckval1==1) & (ckval2==1):
        uu=np.maximum(np.max(adh1),np.max(adh2))
        months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        
        # make Sunny Days and Daylight hours plot
        fig3, ((ax31, ax32),(ax33,ax34))=plt.subplots(2,2,figsize=(8,8),layout='constrained',gridspec_kw={'height_ratios':[1,1],'width_ratios':[1,1]})
        
        dict1={"Sunny": np.array(r1)[:,5],"Partly Cloudy":  np.array(r1)[:,4], "Cloudy": np.array(r1)[:,3] }
        dict2={"Sunny": np.array(r2)[:,5],"Partly Cloudy":  np.array(r2)[:,4], "Cloudy": np.array(r2)[:,3] }
        c=['#FFCC00','#77CEEB','#808080']
        width=0.25
        multiplier=0
        cind=0
        x=np.arange(len(months))
        for boolean, dictvals in dict1.items():
            offset=width*multiplier
            rects1=ax31.bar(x+offset,dictvals,width=width,label=boolean, bottom=np.zeros(12),color=c[cind])
            multiplier+=1
            cind+=1
        ax31.legend(loc='upper right', ncols=3)
        ax31.set_title(f'{address_in1.split(",")[0]} \n Expected Sky Conditions')
        ax31.set_xticks(x+width/(multiplier), months)
        ax31.set_xlabel('Month')
        ax31.set_ylabel('Days of Month (%)')
        ax31.set_ylim([0, 100])
        ax31.yaxis.grid(True,linestyle='--')
        ax31.set_xticklabels(months,rotation=45)
        
        cind=0
        for boolean, dictvals in dict2.items():
            offset=width*multiplier
            rects2=ax32.bar(x+offset,dictvals,width=width,label=boolean, bottom=np.zeros(12),color=c[cind])
            multiplier+=1
            cind+=1
        ax32.legend(loc='upper right', ncols=3)
        ax32.set_title(f'{address_in2.split(",")[0]} \n Expected Sky Conditions')
        ax32.set_xticks(x+width/(multiplier), months)
        ax32.set_xlabel('Month')
        ax32.set_ylabel('Days of Month (%)')
        ax32.set_ylim([0, 100])
        ax32.yaxis.grid(True,linestyle='--')
        ax32.set_xticklabels(months,rotation=45)
        
        ax33.bar(months,adh1,label='Average Daylight Hours')
        ax33.set_ylim([0, np.ceil(uu)])
        ax33.set_title('Average Daylight Hours')
        ax33.set_xlabel('Month')
        ax33.set_ylabel('Hours per Day')
        ax33.yaxis.grid(True,linestyle='--')
        ax33.set_xticks(months)
        ax33.set_xticklabels(months,rotation=45)
        
        ax34.bar(months,adh2,label='Average Daylight Hours')
        ax34.set_ylim([0, np.ceil(uu)])
        ax34.set_title('Average Daylight Hours')
        ax34.set_xlabel('Month')
        ax34.set_ylabel('Hours per Day')
        ax34.yaxis.grid(True,linestyle='--')
        ax34.set_xticks(months)
        ax34.set_xticklabels(months,rotation=45)

    else:
        fig3, (ax1,ax3)=plt.subplots(ncols=1,nrows=2,layout='constrained',figsize=(5, 8),gridspec_kw={'height_ratios': [3, 1]})

    return fig3, ckval1, ckval2

#****************************************************************************************************************
def get_fig4(address_in):
    latitude, longitude, ckval=geocode_latlon(address_in)
    if ckval==0: latitude, longitude, ckval1=geocode_latlon('1600 Pennsylvania Avenue NW, Washington, DC 20500')
    r1=databases_slim4.get_raw_clim(latitude,longitude)

    if (len(r1)<12):
        ckval=0

    if (ckval==1):
        months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        fig4, (ax41,ax42)=plt.subplots(ncols=1,nrows=2,layout='constrained')
        v41=np.array([31,28,31,30,31,30,31,31,30,31,30,31])*np.squeeze(np.array(r1)[:,16])
        v42=np.array([31,28,31,30,31,30,31,31,30,31,30,31])*np.squeeze(np.array(r1)[:,15])
        ul41=np.ceil(np.maximum(1,1.2*np.max(v41)))
        ul42=np.ceil(np.maximum(1,1.2*np.max(v42)))
        s41='{:.1f}'.format(np.sum(v41))
        s42='{:.1f}'.format(np.sum(v42))
        
        bbox_props=dict(boxstyle='round',facecolor='lightyellow',alpha=0.7,edgecolor='k')
        
        ax41.bar(months,v41,label='Days Below 32°F')
        ax41.set_ylim([0, ul41])
        ax41.set_title('Days Below 32°F')
        ax41.set_xlabel('Month')
        ax41.set_ylabel('Average Number of Days')
        ax41.yaxis.grid(True,linestyle='--')
        ax41.text(0.5,0.90,f'Total: {s41} days',transform=ax41.transAxes,ha='center',fontsize=10,bbox=bbox_props)
        
        ax42.bar(months,v42,label='Days Below 0°F')
        ax42.set_ylim([0, ul42])
        ax42.set_title('Days Below 0°F')
        ax42.set_xlabel('Month')
        ax42.set_ylabel('Average Number of Days')
        ax42.yaxis.grid(True,linestyle='--')
        ax42.text(0.5,0.90,f'Total: {s42} days',transform=ax42.transAxes,ha='center',fontsize=10,bbox=bbox_props)

    else: 
        fig4, (ax1,ax3)=plt.subplots(ncols=1,nrows=2,layout='constrained',figsize=(5, 8),gridspec_kw={'height_ratios': [3, 1]})
    
    return fig4, ckval

#****************************************************************************************************************
def get_fig4_2(address_in1, address_in2):
    latitude, longitude, ckval1=geocode_latlon(address_in1)
    if ckval1==0: latitude, longitude, ckval21=geocode_latlon('1600 Pennsylvania Avenue NW, Washington, DC 20500')
    r1=databases_slim4.get_raw_clim(latitude,longitude)

    latitude, longitude, ckval2=geocode_latlon(address_in2)
    if ckval2==0: latitude, longitude, ckval21=geocode_latlon('1600 Pennsylvania Avenue NW, Washington, DC 20500')
    r2=databases_slim4.get_raw_clim(latitude,longitude)

    if (len(r1)<12):
        ckval1=0
    if (len(r2)<12):
        ckval2=0
    if (ckval1==1) & (ckval2==1):
        months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        fig4, ((ax41, ax42),(ax43,ax44))=plt.subplots(2,2,figsize=(8,8),layout='constrained',gridspec_kw={'height_ratios':[1,1],'width_ratios':[1,1]})
        
        v41=np.array([31,28,31,30,31,30,31,31,30,31,30,31])*np.squeeze(np.array(r1)[:,16])
        v42=np.array([31,28,31,30,31,30,31,31,30,31,30,31])*np.squeeze(np.array(r2)[:,16])
        v43=np.array([31,28,31,30,31,30,31,31,30,31,30,31])*np.squeeze(np.array(r1)[:,15])
        v44=np.array([31,28,31,30,31,30,31,31,30,31,30,31])*np.squeeze(np.array(r2)[:,15])
        s41='{:.1f}'.format(np.sum(v41))
        s42='{:.1f}'.format(np.sum(v42))
        s43='{:.1f}'.format(np.sum(v43))
        s44='{:.1f}'.format(np.sum(v44))
        
        ula=np.ceil(1.2*np.maximum(np.max(v41),np.max(v42)))
        ulb=np.ceil(1.2*np.maximum(np.max(v43),np.max(v44)))
        
        bbox_props=dict(boxstyle='round',facecolor='lightyellow',alpha=0.7,edgecolor='k')
        
        ax41.bar(months,v41,label='Days Below 32°F')
        ax41.set_ylim([0, ula])
        ax41.set_title(f'{address_in1.split(",")[0]} \n Days Below 32°F')
        ax41.set_xlabel('Month')
        ax41.set_ylabel('Average Number of Days')
        ax41.yaxis.grid(True,linestyle='--')
        ax41.set_xticks(months)
        ax41.set_xticklabels(months,rotation=45)
        ax41.text(0.5,0.90,f'Total: {s41} days',transform=ax41.transAxes,ha='center',fontsize=10,bbox=bbox_props)
        
        ax42.bar(months,v42,label='Days Below 32°F')
        ax42.set_ylim([0, ula])
        ax42.set_title(f'{address_in2.split(",")[0]} \n Days Below 32°F')
        ax42.set_xlabel('Month')
        ax42.set_ylabel('Average Number of Days')
        ax42.yaxis.grid(True,linestyle='--')
        ax42.set_xticks(months)
        ax42.set_xticklabels(months,rotation=45)
        ax42.text(0.5,0.90,f'Total: {s42} days',transform=ax42.transAxes,ha='center',fontsize=10,bbox=bbox_props)
        
        ax43.bar(months,v43,label='Days Below 0°F')
        ax43.set_ylim([0, ulb])
        ax43.set_title('Days Below 0°F')
        ax43.set_xlabel('Month')
        ax43.set_ylabel('Average Number of Days')
        ax43.yaxis.grid(True,linestyle='--')
        ax43.set_xticks(months)
        ax43.set_xticklabels(months,rotation=45)
        ax43.text(0.5,0.90,f'Total: {s43} days',transform=ax43.transAxes,ha='center',fontsize=10,bbox=bbox_props)
        
        ax44.bar(months,v44,label='Days Below 0°F')
        ax44.set_ylim([0, ulb])
        ax44.set_title('Days Below 0°F')
        ax44.set_xlabel('Month')
        ax44.set_ylabel('Average Number of Days')
        ax44.yaxis.grid(True,linestyle='--')
        ax44.set_xticks(months)
        ax44.set_xticklabels(months,rotation=45)
        ax44.text(0.5,0.90,f'Total: {s44} days',transform=ax44.transAxes,ha='center',fontsize=10,bbox=bbox_props)

    else:
        fig4, (ax1,ax3)=plt.subplots(ncols=1,nrows=2,layout='constrained',figsize=(5, 8),gridspec_kw={'height_ratios': [3, 1]})

    return fig4, ckval1, ckval2

#****************************************************************************************************************
def get_severe(address_in,diff,yr1,yr2):
    latitude, longitude, ckval=geocode_latlon(address_in)
    if ckval==0: latitude, longitude, ckval1=geocode_latlon('1600 Pennsylvania Avenue NW, Washington, DC 20500')
    diff=diff/69.04
    r2=databases_slim4.get_raw_torn(latitude,longitude,diff,yr1,yr2)
    r3=databases_slim4.get_raw_wind(latitude,longitude,diff,yr1,yr2)
    r4=databases_slim4.get_raw_hail(latitude,longitude,diff,yr1,yr2)

    if (len(r2)==0) & (len(r3)==0) & (len(r4)==0):
        r1=databases_slim4.get_raw_clim(latitude,longitude)
        if len(r1)==0:
            ckval=0

    return r2, r3, r4, ckval

#****************************************************************************************************************
def get_severe_2(address_in1, address_in2,diff,yr1,yr2):
    latitude, longitude, ckval1=geocode_latlon(address_in1)
    if ckval1==0: latitude, longitude, ckval1a=geocode_latlon('1600 Pennsylvania Avenue NW, Washington, DC 20500')
    diff=diff/69.04

    r21=databases_slim4.get_raw_torn(latitude,longitude,diff,yr1,yr2)
    r31=databases_slim4.get_raw_wind(latitude,longitude,diff,yr1,yr2)
    r41=databases_slim4.get_raw_hail(latitude,longitude,diff,yr1,yr2)

    if (len(r21)==0) & (len(r31)==0) & (len(r41)==0):
        r1=databases_slim4.get_raw_clim(latitude,longitude)
        if len(r1)==0:
            ckval1=0

    latitude, longitude, ckval2=geocode_latlon(address_in2)
    if ckval2==0: latitude, longitude, ckval2a=geocode_latlon('1600 Pennsylvania Avenue NW, Washington, DC 20500')
    r22=databases_slim4.get_raw_torn(latitude,longitude,diff,yr1,yr2)
    r32=databases_slim4.get_raw_wind(latitude,longitude,diff,yr1,yr2)
    r42=databases_slim4.get_raw_hail(latitude,longitude,diff,yr1,yr2)

    if (len(r22)==0) & (len(r32)==0) & (len(r42)==0):
        r1=databases_slim4.get_raw_clim(latitude,longitude)
        if len(r1)==0:
            ckval2=0

    return r21, r31, r41, ckval1, r22, r32, r42, ckval2











#****************************************************************************************************************
def average_daylight_hours(latitude, month):
    # Convert latitude from degrees to radians
    latitude_rad = math.radians(latitude)
   
    # Define the number of days in each month
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
   
    # Calculate the day of the year for the middle of the given month
    day_of_year = sum(list(days_in_month.values())[:month]) - (days_in_month[month] // 2)
   
    # Calculate the solar declination angle for the given day of the year
    declination_angle = -23.44 * math.cos(math.radians((360/365.0) * (day_of_year + 10)))
   
    # Calculate the daylight hours using the latitude and declination angle
    daylight_hours = 2 * math.degrees(math.acos(-math.tan(latitude_rad) * math.tan(math.radians(declination_angle)))) / 15
   
    return daylight_hours


#****************************************************************************************************************
def geocode_latlon(address):
    params = { 'format'        :'json', 
              'addressdetails': 1, 
               'q'             : address}
    headers = { 'user-agent'   : 'TDI' }   #  Need to supply a user agent other than the default provided 
                                           #  by requests for the API to accept the query.
    response=requests.get('http://nominatim.openstreetmap.org/search', params=params, headers=headers)
    if (len(response.json())==0): return [float(38.897699700000004), float(-77.03655315), 0]
    latval=response.json()[0]['lat']
    lonval=response.json()[0]['lon']
    return [float(latval), float(lonval), 1]



#****************************************************************************************************************
def haversine(lat1,lon1,lat2,lon2):
    lat1r=lat1*3.1416/180
    lon1r=lon1*3.1416/180
    lat2r=float(lat2)*3.1416/180
    lon2r=float(lon2)*3.1416/180
    R=3959.0
    dlon=lon2r-lon1r
    dlat=lat2r-lat1r
    a=np.sin(dlat/2)**2 +np.cos(lat1r) * np.cos(lat2r) * np.sin(dlon/2)**2
    c=2*np.arctan2(np.sqrt(a),np.sqrt(1-a))
    dist=R * c
    return round(dist)

#****************************************************************************************************************
def calcdir(lat1,lon1,lat2,lon2):
    lat1r=lat1*3.1416/180
    lon1r=lon1*3.1416/180
    lat2r=float(lat2)*3.1416/180
    lon2r=float(lon2)*3.1416/180
    angle=np.arctan2(lat2r-lat1r,lon2r-lon1r)
    angle_deg=angle*180/3.1416
    directions=['N','NE','E','SE','S','SW','W','NW']
    if angle_deg<0:
        angle_deg+=360
    index=int((angle_deg+22.5)/45)%8
    
    return directions[index]

#****************************************************************************************************************
def convert_and_sort_dates(df, date_column_name):
    # Define a lambda function to convert 'yy' to a four-digit year
    convert_year = lambda yy: '19' + yy if int(yy) >= 30 else '20' + yy
   
    # Split the specified date column into month, day, and year, and apply the lambda function to convert the year
    df['Date'] = pd.to_datetime(df[date_column_name].str.split('/').apply(lambda x: f'{x[0]}/{x[1]}/{convert_year(x[2])}'), format='%m/%d/%Y')

    # Sort the DataFrame by the 'date' column
    df = df.sort_values(by='Date',ascending=False)
    df['Date']=df['Date'].dt.strftime('%m-%d-%Y')

    return df

