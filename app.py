from importlib.metadata import pass_none

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

df=pd.read_csv('India.csv')

list_of_states=list(df['State'].unique())
list_of_states.insert(0,'overall India')

st.sidebar.title('India Census 2011 Data Viz')

selected_states=st.sidebar.selectbox('Select a State', list_of_states)
primary=st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary=st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot=st.sidebar.button('Plot Graph')

if plot:
    if selected_states=='overall India':

        fig=px.scatter_mapbox(df,lat='Latitude',lon='Longitude',size=primary,color=secondary,
                              zoom=3,size_max=35,width=1200,height=700,
                              color_continuous_scale='viridis',mapbox_style='carto-positron',hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df=df[df['State']==selected_states]

        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary, color=secondary,
                                zoom=3, size_max=35, width=1200, height=700,
                                color_continuous_scale='viridis',mapbox_style='carto-positron',hover_name='District')

        st.plotly_chart(fig, use_container_width=True)



