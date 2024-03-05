#--------------------------------------------------Imported Needed Libraries--------------------------------------------
import pandas as pd
import streamlit as st
from st_pages import Page,show_pages,add_page_title
import numpy as np
import mysql.connector
from sqlalchemy import create_engine
import plotly.express as px
import seaborn as sns

#-------------------------------------------------MySQL SQLAlchemy Connection---------------------------------------
engine = create_engine('mysql+mysqlconnector://root:1234@localhost/phonepe',echo=False)
config = {
    'user':'root',    'host':'127.0.0.1',
    'password':'1234', 'database':'phonepe'
}
connection = mysql.connector.connect(**config)
cursor = connection.cursor(buffered=True)

cursor.execute("""select State from map_trans;""")
state_result = cursor.fetchall()
state_df = pd.DataFrame(state_result,columns=['State'])
state_list = state_df['State'].unique()

#--------------------------------------------------Streamlit Setup----------------------------------------------------
st.set_page_config(page_title = 'Home', layout = 'wide')
st.title(":blue[Phonepe Pulse Data Visulization]")
st.write('Note : Data available from 2018 to 2023')
st.write('## :orange[State wise Insights]')
tab1,tab2 = st.tabs(['Transaction','User'])

#---------------------------------------------------Transaction Block-------------------------------------------------
with tab1:
    state = st.selectbox('**State**',state_list,key='state') 
    col1, col2 = st.columns(2)
                  
    with col1:     
            year = st.selectbox('**Year**',('All','2018','2019','2020','2021','2022','2023'),key ='year')  
    with col2:        
            quarter = st.selectbox('**Quarter**',('All','1','2','3','4'),key='quarter')

    if year == 'All':
        year = '2023'

    yr_li=['2018','2019','2020','2021','2022','2023']    
    if year in yr_li and quarter=='All':
         year = year
         quarter = 4 
     
         
    cursor.execute(f"""select State,Transaction_count,Transaction_amount,Transaction_type from agg_trans where Year={year} and Quarter={quarter};""")
    agg_trans = cursor.fetchall() 
    agg_trans_df = pd.DataFrame(agg_trans,columns=['State','Transaction_count','Transaction_amount','Transaction_type'])
    agg_trans_df = agg_trans_df[agg_trans_df['State']==state]
 
    cursor.execute(f"""select State,District,Transaction_count,Transaction_amount from map_trans where Year={year} and Quarter={quarter};""")
    map_trans = cursor.fetchall() 
    map_trans_df = pd.DataFrame(map_trans,columns=['State','District','Count','Amount'])
    map_trans_df = map_trans_df[map_trans_df['State']==state]
    map_trans_df.drop('State',axis=1,inplace=True)

    total = sum(agg_trans_df['Transaction_count'])
    col1,col2 = st.columns(2)
    col1.metric(
    label = f'Total Phonepe Transaction count till {year} (UPI+Cards+Wallets)',
    value = '{:.2f} Lakhs'.format(total/1000000),
    delta = 'Upward Trend'
)        
    total = sum(agg_trans_df['Transaction_amount'])
    col2.metric(
    label = f'Total Phonepe Transaction amount till {year} (UPI+Cards+Wallets)',
    value = '{:.2f} Cr.'.format(total/100000000),
    delta = 'Upward Trend'
)   
    st.write(f'#### :orange[Sum of transactions across different categories in {state} up to {year}]')
    fig = px.bar(agg_trans_df,x='Transaction_type',y='Transaction_amount',labels={'Transaction_type':'Type of Transactions','Transaction_amount':'Transaction Amount'})
    fig.update_traces(marker_color=['orange','blue','green','yellow'])
    st.plotly_chart(fig)

    st.write(f'#### :orange[Number of transactions across different categories in {state} up to {year}]')
    fig = px.pie(agg_trans_df,values='Transaction_count',names='Transaction_type',labels={'Transaction_type':'Type of Transactions','Transaction_count':'Transaction Count'})
    fig.update_traces(marker_colors=['orange','blue','green','yellow','red'])
    st.plotly_chart(fig)
    
    st.write('### :orange[District wise Transactions]')
    st.dataframe(map_trans_df,hide_index=True,use_container_width=True)

#-----------------------------------------------------User Block----------------------------------------------------    
with tab2:
    col1, col2, col3 = st.columns(3)
    with col1:
           state = st.selectbox('**State**',state_list,key='state2')        
    with col2:     
            year = st.selectbox('**Year**',('All','2018','2019','2020','2021','2022'),key ='year2')  
    with col3:        
            quarter = st.selectbox('**Quarter**',('All','1','2','3','4'),key='quarter2')

    if year == 'All':
        year = '2022'

    yr_li=['2018','2019','2020','2021','2022']    
    if year in yr_li and quarter=='All':
        year = year
        quarter = 1  

    cursor.execute(f"""select State,users_count,Brand,users_precentage from agg_user where Year={year} and Quarter={quarter};""")
    agg_user = cursor.fetchall() 
    agg_user_df = pd.DataFrame(agg_user,columns=['State','User Count','Brand','Percentage'])
    agg_user_df = agg_user_df[agg_user_df['State']==state]
 
    cursor.execute(f"""select State,District,Total_users from map_user where Year={year} and Quarter={quarter};""")
    map_user = cursor.fetchall() 
    map_user_df = pd.DataFrame(map_user,columns=['State','District','User Count'])
    map_user_df = map_user_df[map_user_df['State']==state]
    map_user_df.drop('State',axis=1,inplace=True)     


    total = sum(agg_user_df['User Count'])
    col2.metric(
    label = f'Total Phonepe user count till {year} (UPI+Cards+Wallets)',
    value = '{:.2f} K.'.format(total/10000),
    delta = 'Upward Trend'
)  
    st.write(f'### :orange[Most used Mobile Brands till {year} in {state}]')
    fig = px.treemap(agg_user_df,
                     path=['Brand'],
                     values='User Count',
                     color='Percentage',
                     color_continuous_scale='ylorbr',
                     hover_data={'Percentage':':.2%'},
                     hover_name='Brand'
                     )
    fig.update_layout(width=1100,height=600)
    st.plotly_chart(fig)

    st.write('### :orange[District wise Transactions]')
    st.dataframe(map_user_df,hide_index=True)