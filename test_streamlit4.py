import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import test_streamlit4_L2 as ts4
import pandas as pd

# Streamlit app
def main():
    st.set_page_config("Weather For You")
    st.title('Location-Based Weather for You')
    st.markdown("Know what to weather to expect for your area. Temperature extremes, Humidity, Precipitation, Wind, Sun, and Storms available for your Continental US address.")
    st.sidebar.markdown(f"### Enter Your Address Below:")
    selected_option = st.sidebar.checkbox('Select to Compare Locations',False)


    if selected_option: #this one is when you want to compare addresses
        # st.write("Multiple Locations")
        
        user_input1a = st.sidebar.text_input('Enter first address in the Continential USA:', value='1600 Pennsylvania Avenue NW, Washington, DC 20500')
        user_input1b = st.sidebar.text_input('Enter second address in the Continential USA:', value='416 Main St, Lebanon, KS 66952')
        st.sidebar.markdown(f"###### Acceptable formats:")
        st.sidebar.markdown(f"###### Street, City, State, Zip - 1600 Pennsylvania Avenue NW, Washington, DC 20500")
        st.sidebar.markdown(f"###### Street, City, State - 1600 Pennsylvania Avenue NW, Washington, DC")
        st.sidebar.markdown(f"###### Street, Zip - 1600 Pennsylvania Avenue NW, 20500")
        st.sidebar.markdown(f"###### City, State - Washington, DC")


        # Display the user input from the sidebar
        # st.sidebar.markdown(f"##### Current Location")
        # st.sidebar.write('Showing:', user_input1)
        
        # fig1, fig2, fig3, fig4, r2, r3, r4 =ts2.get_figures(user_input1,user_input4,user_input2,user_input3)
        
        # Create a dropdown menu to select the plot type
        plot_type = st.selectbox('Select a plot type:', ['Monthly Weather', 'Expected Precipitation', 'Expected Sunshine', 'Cold Temperature Extremes',  'Severe Storms'])
    
        # databases_slim3.get_raw_clim(latitude,longitude)
        # databases_slim3.get_raw_torn(latitude,longitude,diff,yr1,yr2)
        # databases_slim3.get_raw_wind(latitude,longitude,diff,yr1,yr2)
        # databases_slim3.get_raw_hail(latitude,longitude,diff,yr1,yr2)
        # databases_slim3.get_raw_rhws(latitude,longitude)
        # databases_slim3.get_raw_cloudy(latitude,longitude)
        # databases_slim3.get_raw_pcounts(latitude,longitude)
    # get_fig1(address_in)
    # get_fig2(address_in)
    # get_fig3(address_in)
    # get_fig4(address_in)
    # get_severe(address_in,diff,yr1,yr2)
    # get_fig1_2(address_in1, address_in2)
    # get_fig2_2(address_in1, address_in2)
    # get_fig3_2(address_in1, address_in2)
    # get_fig4_2(address_in1, address_in2)
    # get_severe_2(address_in1, address_in2, diff,yr1,yr2)
    
        
        # Display the selected plot
        if plot_type == 'Monthly Weather':
            fig1, ckval1, ckval2=ts4.get_fig1_2(user_input1a,user_input1b)
            if  (ckval1==1) & (ckval2==1): 
                # st.write('Showing:', user_input1)
                st.pyplot(fig1)
                st.markdown("##### Interpreting the figures: Top (Temperature ranges for your location): Red - Maximum and Minimum temperatures, Blue - Average daily temperature range for the month, Black - Average daily temperature. Bottom (Relative Humidity for your location): Blue - Highest average value, Red - Lowest average value.")
            elif (ckval1==0) & (ckval2==1):
                    st.markdown(f"#### Oops! We encountered a problem with your request.")
                    st.markdown(f"Information cannot be found for {user_input1a}.")
                    st.markdown(f"Please check the address formatting or try a different location.")

            elif (ckval1==1) & (ckval2==0):
                    st.markdown(f"#### Oops! We encountered a problem with your request.")
                    st.markdown(f"Information cannot be found for {user_input1b}.")
                    st.markdown(f"Please check the address format or try a different location.")

            elif (ckval1==0) & (ckval2==0):
                    st.markdown(f"#### Oops! We encountered a problem with your request.")
                    st.markdown(f"Information cannot be found for either address.")
                    st.markdown(f"Please check the address format or try a different locations.")
            
        elif plot_type == 'Expected Precipitation':
            fig2, ckval1, ckval2=ts4.get_fig2_2(user_input1a,user_input1b)
            if  (ckval1==1) & (ckval2==1): 
                # st.write('Showing:', user_input1)
                # st.write('Showing:', user_input2)
                st.pyplot(fig2)
                st.write('Interpreting the figures: Top - Total precipitation as equilant water (ie. water content in snow, ice, and hail), Bottom: Total number of days with 0.01" or more of precipitation.')
            elif (ckval1==0) & (ckval2==1):
                    st.markdown(f"#### Oops! We encountered a problem with your request.")
                    st.markdown(f"Information cannot be found for {user_input1a}.")
                    st.markdown(f"Please check the address formatting or try a different location.")

            elif (ckval1==1) & (ckval2==0):
                    st.markdown(f"#### Oops! We encountered a problem with your request.")
                    st.markdown(f"Information cannot be found for {user_input1b}.")
                    st.markdown(f"Please check the address format or try a different location.")

            elif (ckval1==0) & (ckval2==0):
                    st.markdown(f"#### Oops! We encountered a problem with your request.")
                    st.markdown(f"Information cannot be found for either address.")
                    st.markdown(f"Please check the address format or try a different locations.")
            
        elif plot_type == 'Expected Sunshine':
            fig3, ckval1, ckval2=ts4.get_fig3_2(user_input1a,user_input1b)
            if  (ckval1==1) & (ckval2==1): 
                # st.write('Showing:', user_input1)
                st.pyplot(fig3)
            elif (ckval1==0) & (ckval2==1):
                    st.markdown(f"#### Oops! We encountered a problem with your request.")
                    st.markdown(f"Information cannot be found for {user_input1a}.")
                    st.markdown(f"Please check the address formatting or try a different location.")

            elif (ckval1==1) & (ckval2==0):
                    st.markdown(f"#### Oops! We encountered a problem with your request.")
                    st.markdown(f"Information cannot be found for {user_input1b}.")
                    st.markdown(f"Please check the address format or try a different location.")

            elif (ckval1==0) & (ckval2==0):
                    st.markdown(f"#### Oops! We encountered a problem with your request.")
                    st.markdown(f"Information cannot be found for either address.")
                    st.markdown(f"Please check the address format or try a different locations.")
            
        elif plot_type == 'Cold Temperature Extremes':
            fig4, ckval1, ckval2=ts4.get_fig4_2(user_input1a,user_input1b)
            if  (ckval1==1) & (ckval2==1): 
                # st.write('Showing:', user_input1)
                st.pyplot(fig4)
            elif (ckval1==0) & (ckval2==1):
                    st.markdown(f"#### Oops! We encountered a problem with your request.")
                    st.markdown(f"Information cannot be found for {user_input1a}.")
                    st.markdown(f"Please check the address formatting or try a different location.")

            elif (ckval1==1) & (ckval2==0):
                    st.markdown(f"#### Oops! We encountered a problem with your request.")
                    st.markdown(f"Information cannot be found for {user_input1b}.")
                    st.markdown(f"Please check the address format or try a different location.")

            elif (ckval1==0) & (ckval2==0):
                    st.markdown(f"#### Oops! We encountered a problem with your request.")
                    st.markdown(f"Information cannot be found for either address.")
                    st.markdown(f"Please check the address format or try a different locations.")

            
        elif plot_type == 'Severe Storms':
            st.markdown(f"Choose the distance from your locations and the year range")
            
            user_input4 = st.slider('Distance from address in miles:', min_value=5, max_value=100, value=10, step=5, format='%i')
            
            user_input2, user_input3 = st.slider('Year Range:', min_value=1955, max_value=2022, value=(1990,2022), format='%i')
            # user_input2 = st.sidebar.number_input('Start Year: (min=1955)', min_value=1955, step=1, value=1996)
            # user_input3 = st.sidebar.number_input('End Year: (max=2022)', min_value=user_input2, step=1, value=2022)
            st.write('Year Range:', user_input2, '-', user_input3)
            
            r21, r31, r41, ckval1, r22, r32, r42, ckval2=ts4.get_severe_2(user_input1a,user_input1b,user_input4,user_input2,user_input3)

            # fig4, ckval=ts4.get_fig4(address_in)
            if (ckval1==1) & (ckval2==1):
                # r2 (tornado) - # yr, mo, dy, date, mag, lat, lon
                # r3 (wind) - # yr, date, mag, lat, lon
                # r4 (hail) - # yr, date, mag, lat, lon
    
                st.divider()    
                st.markdown(f"### Tornados:")
                col1a, col2a = st.columns(2)

                with col1a:
                    st.text(user_input1a.split(",")[0])
                    if len(r21)>0:
                        dft1 = pd.DataFrame(np.array(r21)[:,3::], columns=("Date", "EF Category", "Latitude", "Longitude"))
                        st.markdown(f"There are {dft1.shape[0]:,} tornados EF-1 or stronger in your search.")
                        st.dataframe(dft1,hide_index=True, use_container_width=True)
                    else:
                        st.markdown(f"There are no tornado events in your search area.")
        
                with col2a:
                    st.text(user_input1b.split(",")[0])
                    if len(r22)>0:
                        dft2 = pd.DataFrame(np.array(r22)[:,3::], columns=("Date", "EF Category", "Latitude", "Longitude"))
                        st.markdown(f"There are {dft2.shape[0]:,} tornados EF-1 or stronger in your search.")
                        st.dataframe(dft2,hide_index=True, use_container_width=True)
                    else:
                        st.markdown(f"There are no tornado events in your search area.")

                st.divider()    
                st.markdown(f"### Strong Winds:")
                col1b, col2b = st.columns(2)

                with col1b:
                    if len(r31)>0:
                        dfw1 = pd.DataFrame(np.array(r31)[:,1::], columns=("Date", "Wind Speed (mph)", "Latitude", "Longitude"))
                        st.markdown(f"There are {dfw1.shape[0]:,} strong wind events in your search.")
                        st.dataframe(dfw1,hide_index=True, use_container_width=True)
                    else:
                        st.markdown(f"There are no strong wind events in your search area.")
                
                with col2b:
                    if len(r32)>0:
                        dfw2 = pd.DataFrame(np.array(r32)[:,1::], columns=("Date", "Wind Speed (mph)", "Latitude", "Longitude"))
                        st.markdown(f"There are {dfw2.shape[0]:,} strong wind events in your search.")
                        st.dataframe(dfw2,hide_index=True, use_container_width=True)
                    else:
                        st.markdown(f"There are no strong wind events in your search area.")

                st.divider()    
                st.markdown(f"### Hail:")
                col1c, col2c = st.columns(2)

                with col1c:
                    if len(r41)>0:
                        dfh1 = pd.DataFrame(np.array(r41)[:,1::], columns=("Date", "Hail Diameter (in)", "Latitude", "Longitude"))
                        st.markdown(f"There are {dfh1.shape[0]:,} damaging hail in your search.")
                        st.dataframe(dfh1,hide_index=True, use_container_width=True)
                    else:
                        st.markdown(f"There are no damaging hail events in your search area.")
                
                with col2c:
                    if len(r42)>0:
                        dfh2 = pd.DataFrame(np.array(r42)[:,1::], columns=("Date", "Hail Diameter (in)", "Latitude", "Longitude"))
                        st.markdown(f"There are {dfh2.shape[0]:,} damaging hail in your search.")
                        st.dataframe(dfh2,hide_index=True, use_container_width=True)
                    else:
                        st.markdown(f"There are no damaging hail events in your search area.")
            elif (ckval1==0) & (ckval2==1):
                    st.markdown(f"#### Oops! We encountered a problem with your request.")
                    st.markdown(f"Information cannot be found for {user_input1a}.")
                    st.markdown(f"Please check the address formatting or try a different location.")

            elif (ckval1==1) & (ckval2==0):
                    st.markdown(f"#### Oops! We encountered a problem with your request.")
                    st.markdown(f"Information cannot be found for {user_input1b}.")
                    st.markdown(f"Please check the address format or try a different location.")

            elif (ckval1==0) & (ckval2==0):
                    st.markdown(f"#### Oops! We encountered a problem with your request.")
                    st.markdown(f"Information cannot be found for either address.")
                    st.markdown(f"Please check the address format or try a different locations.")

    
                # st.markdown(f"On average this region annually expects: {round(swrating[0])} damaging wind events, {round(swrating[1])} large hail events, and {round(swrating[2]*100)}% chance of a tornado rated EF-1 or stronger.")
        
    else:
        # st.write("Single Location")

    
        user_input1 = st.sidebar.text_input('Enter an address in the Continential USA:', value='1600 Pennsylvania Avenue NW, Washington, DC 20500')
        st.sidebar.markdown(f"###### Acceptable formats:")
        st.sidebar.markdown(f"###### Street, City, State, Zip - 1600 Pennsylvania Avenue NW, Washington, DC 20500")
        st.sidebar.markdown(f"###### Street, City, State - 1600 Pennsylvania Avenue NW, Washington, DC")
        st.sidebar.markdown(f"###### Street, Zip - 1600 Pennsylvania Avenue NW, 20500")
        st.sidebar.markdown(f"###### City, State - Washington, DC")
        # Display the user input from the sidebar
        # st.sidebar.markdown(f"##### Current Location")
        # st.sidebar.write('Showing:', user_input1)
        
        # fig1, fig2, fig3, fig4, r2, r3, r4 =ts2.get_figures(user_input1,user_input4,user_input2,user_input3)
        
        # Create a dropdown menu to select the plot type
        plot_type = st.selectbox('Select a plot type:', ['Monthly Weather', 'Expected Precipitation', 'Expected Sunshine', 'Cold Temperature Extremes',  'Severe Storms'])
    
        # databases_slim3.get_raw_clim(latitude,longitude)
        # databases_slim3.get_raw_torn(latitude,longitude,diff,yr1,yr2)
        # databases_slim3.get_raw_wind(latitude,longitude,diff,yr1,yr2)
        # databases_slim3.get_raw_hail(latitude,longitude,diff,yr1,yr2)
        # databases_slim3.get_raw_rhws(latitude,longitude)
        # databases_slim3.get_raw_cloudy(latitude,longitude)
        # databases_slim3.get_raw_pcounts(latitude,longitude)
    # get_fig1(address_in)
    # get_fig2(address_in)
    # get_fig3(address_in)
    # get_fig4(address_in)
    # get_severe(address_in,diff,yr1,yr2)
    # get_fig1_2(address_in1, address_in2)
    # get_fig2_2(address_in1, address_in2)
    # get_fig3_2(address_in1, address_in2)
    # get_fig4_2(address_in1, address_in2)
    # get_severe_2(address_in1, address_in2, diff,yr1,yr2)
    
        
        # Display the selected plot
        if plot_type == 'Monthly Weather':
            fig1, ckval=ts4.get_fig1(user_input1)
            if ckval==1: 
                st.write('Showing:', user_input1)
                st.pyplot(fig1)
                st.markdown("##### Interpreting the figures: Top (Temperature ranges for your location): Red - Maximum and Minimum temperatures, Blue - Average daily temperature range for the month, Black - Average daily temperature. Bottom (Relative Humidity for your location): Blue - Highest average value, Red - Lowest average value.")
                
            else:
                st.markdown(f"#### Oops! We encountered a problem with your request.")
                st.markdown(f"Information cannot be found for {user_input1}.")
                
            
        elif plot_type == 'Expected Precipitation':
            fig2, ckval=ts4.get_fig2(user_input1)
            if ckval==1: 
                st.write('Showing:', user_input1)
                st.pyplot(fig2)
                st.write('Interpreting the figures: Top - Total precipitation as equilant water (ie. water content in snow, ice, and hail), Bottom: Total number of days with 0.01" or more of precipitation.')
            else:
                st.markdown(f"#### Oops! We encountered a problem with your request.")
                st.markdown(f"Information cannot be found for {user_input1}.")
                st.markdown(f"Please check the address format or try a different location.")
            
        elif plot_type == 'Expected Sunshine':
            fig3, ckval=ts4.get_fig3(user_input1)
            if ckval==1: 
                st.write('Showing:', user_input1)
                st.pyplot(fig3)
            else:
                st.markdown(f"#### Oops! We encountered a problem with your request.")
                st.markdown(f"Information cannot be found for {user_input1}.")
                st.markdown(f"Please check the address format or try a different location.")
            
        elif plot_type == 'Cold Temperature Extremes':
            fig4, ckval=ts4.get_fig4(user_input1)
            if ckval==1: 
                st.write('Showing:', user_input1)
                st.pyplot(fig4)
            else:
                st.markdown(f"#### Oops! We encountered a problem with your request.")
                st.markdown(f"Information cannot be found for {user_input1}.")
                st.markdown(f"Please check the address format or try a different location.")
            
        elif plot_type == 'Severe Storms':
            st.markdown(f"Choose the distance from your location and the year range")
            
            user_input4 = st.slider('Distance from address in miles:', min_value=5, max_value=100, value=10, step=5, format='%i')
            
            user_input2, user_input3 = st.slider('Year Range:', min_value=1955, max_value=2022, value=(1990,2022), format='%i')
            # user_input2 = st.sidebar.number_input('Start Year: (min=1955)', min_value=1955, step=1, value=1996)
            # user_input3 = st.sidebar.number_input('End Year: (max=2022)', min_value=user_input2, step=1, value=2022)
            st.write('Year Range:', user_input2, '-', user_input3)
            
            r2, r3, r4, ckval=ts4.get_severe(user_input1,user_input4,user_input2,user_input3)
            # fig4, ckval=ts3.get_fig4(address_in)
            if ckval==1:
                # r2 (tornado) - # yr, mo, dy, date, mag, lat, lon
                # r3 (wind) - # yr, date, mag, lat, lon
                # r4 (hail) - # yr, date, mag, lat, lon
                print(f'{len(r2)} {len(r3)} {len(r4)}')

                st.divider()    
                st.markdown(f"### Tornados:")
                if len(r2)>0:
                    dft = pd.DataFrame(np.array(r2)[:,3::], columns=("Date", "EF Category", "Latitude", "Longitude"))
                    st.markdown(f"There are {dft.shape[0]:,} tornados EF-1 or stronger in your search.")
                    st.dataframe(dft,hide_index=True, use_container_width=True)
                else: 
                    st.markdown(f"There are no tornados in your search area.")
    
                st.divider()    
                st.markdown(f"### Strong Winds:")
                if len(r3)>0:
                    dfw = pd.DataFrame(np.array(r3)[:,1::], columns=("Date", "Wind Speed (mph)", "Latitude", "Longitude"))
                    st.markdown(f"There are {dfw.shape[0]:,} strong wind events in your search.")
                    st.dataframe(dfw,hide_index=True, use_container_width=True)
                else:
                    st.markdown(f"There are no tornados in your search area.")                    
    
                st.divider()    
                st.markdown(f"### Hail:")
                if len(r4)>0:
                    dfh = pd.DataFrame(np.array(r4)[:,1::], columns=("Date", "Hail Diameter (in)", "Latitude", "Longitude"))
                    st.markdown(f"There are {dfh.shape[0]:,} damaging hail in your search.")
                    st.dataframe(dfh,hide_index=True, use_container_width=True)
                else:
                    st.markdown(f"There are no tornados in your search area.")
                    
            else:
                st.markdown(f"#### Oops! We encountered a problem with your request.")
                st.markdown(f"Information cannot be found for {user_input1}.")
                st.markdown(f"Please check the address format or try a different location.")
    
                # st.markdown(f"On average this region annually expects: {round(swrating[0])} damaging wind events, {round(swrating[1])} large hail events, and {round(swrating[2]*100)}% chance of a tornado rated EF-1 or stronger.")
    
    
    st.divider()    
    
    st.markdown(f"###### Climate Data derived from the Climatology Lab Gridded Dataset. Detailed information and datasets in NetCDF4 format are available at https://www.climatologylab.org/gridmet.html")
    st.markdown(f"###### Severe Weather Data sourced from the NOAA Storm Prediction Center's Severe Weather Maps, Graphics, and Data Page. Available at https://www.spc.noaa.gov/wcm/")


if __name__ == '__main__':
    main()