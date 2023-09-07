import streamlit as st
import pandas as pd 
import numpy as np 

import plotly.graph_objects as go
from plotly.subplots import make_subplots


st.title("SHALE GAS")

DPR= pd.read_csv("Rig_date.csv")




page = st.sidebar.radio("Navigation", ["DPR", "DUC"])

if page == "DPR":
    regions = list(np.unique(DPR["Region"]))


    page = st.sidebar.radio("Navigation", regions )

    df = DPR[DPR["Region"] == page]




    







    def pivot_gen(df, val, agg_='mean', idx='Month', cols='Year'):

        return pd.pivot_table(df, values=val, index=idx, columns=cols, aggfunc=agg_, margins=True)
       

    # Assuming you have the DataFrame 'your_dataframe' containing the data

    # Get the pivot tables

   

    year_start, year_end = st.slider('Select year range', min_value=2009, max_value=2023, value=(2018, 2023))
    month_start, month_end = st.slider('Select week range', min_value=1, max_value=12 ,value=(1, 12))


    filtered_df = df[(df['Year'] >= year_start) & (df['Year'] <= year_end)]
    filtered_df = filtered_df[(filtered_df['Month'] >= month_start) & (filtered_df['Month'] <=  month_end)]

    cols = ['Rig count', 'Production per rig Crude Oil',
       'Legacy production change Crude Oil', 'Total production Crude Oil',
       'Production per rig Natural Gas',
       'Legacy production change Natural Gas', 'Total production Natural Gas']

#(bbl/d) (Mcf/d) 


    st.subheader("Piviots Tables for {}".format(page))
    for i in cols:
        st.subheader(i)
        st.dataframe(pivot_gen(filtered_df,i).round(2),width = 700)


else:
    df = pd.read_csv("DUC.csv")
    regions = ['Anadarko', 'Appalachia', 'Bakken', 'DPR Regions', 'Eagle Ford','Haynesville', 'Niobrara', 'Permian']
    page = st.sidebar.radio("Navigation", regions )
    def pivot_gen(df, val, agg_='mean', idx='Month', cols='Year'):
        return pd.pivot_table(df, values=val, index=idx, columns=cols, aggfunc=agg_, margins=True)

     



   


    

   



    


    year_start, year_end = st.slider('Select year range', min_value=2009, max_value=2023, value=(2018, 2023))
    month_start, month_end = st.slider('Select week range', min_value=1, max_value=12 ,value=(1, 12))


    filtered_df = df[(df['Year'] >= year_start) & (df['Year'] <= year_end)]
    filtered_df = filtered_df[(filtered_df['Month'] >= month_start) & (filtered_df['Month'] <=  month_end)]


    st.subheader("Piviots Tables for {}".format(page))
    for i in filtered_df.columns:
        if page in i :
            st.subheader(i)
            st.dataframe(pivot_gen(filtered_df,i).round(2),width = 700)
        else:
            pass

        


            


      