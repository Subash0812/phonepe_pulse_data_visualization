#-----------------------------------------------------imported needed libraries----------------------------------------
import os 
import json 
import numpy as np
import pandas as pd
import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine

#-----------------------------------------------------MySQL SQLAlchemy Connection-------------------------------------
config = {
    'user':'root',    'host':'127.0.0.1',
    'password':'1234', 'database':'phonepe'
}
connection = mysql.connector.connect(**config)
cursor = connection.cursor()
engine = create_engine('mysql+mysqlconnector://root:1234@localhost/phonepe',echo=False)

def format_state(state):
    words = state.split('-')
    return ' '.join([word.capitalize() for word in words])
print("Data Storing to MySQL......")


#--------------------------------------------Aggregated Transaction---------------------------------------------------
path= "D:/phonepe/data/data/aggregated/transaction/country/india/state/"
Agg_state_list=os.listdir(path)
Agg_state_list
clm={'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              clm['Transaction_type'].append(Name)
              clm['Transaction_count'].append(count)
              clm['Transaction_amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quarter'].append(int(k.strip('.json')))
Agg_Trans=pd.DataFrame(clm)
Agg_Trans['State'] = Agg_Trans['State'].apply(format_state)    
Agg_Trans['State'] = Agg_Trans['State'].str.replace('Andaman & Nicobar Islands','Andaman & Nicobar')
Agg_Trans.to_sql('agg_trans',con=engine,if_exists='replace',index=False)


#----------------------------------------------Aggregated User---------------------------------------------------------
path= "D:/phonepe/data/data/aggregated/user/country/india/state/"
Agg_state_list=os.listdir(path)
Agg_state_list
df2={'State':[], 'Year':[],'Quarter':[],'Brand':[], 'Users_count':[], 'Users_precentage':[]}

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            try:
                for z in D['data']['usersByDevice']:
                        brand = z['brand']
                        count = z['count']
                        percentage = z['percentage']
                        df2['Brand'].append(brand)
                        df2['Users_count'].append(count)
                        df2['Users_precentage'].append(percentage*100)
                        df2['State'].append(i)
                        df2['Year'].append(j)
                        df2['Quarter'].append(int(k.strip('.json')))
            except:
                pass                        
Agg_User=pd.DataFrame(df2)
Agg_User['State'] = Agg_User['State'].apply(format_state)    
Agg_User['State'] = Agg_User['State'].str.replace('Andaman & Nicobar Islands','Andaman & Nicobar')
Agg_User.to_sql('agg_user',con=engine,if_exists='replace',index=False)


#-------------------------------------------------Map transaction------------------------------------------------------
path= "D:/phonepe/data/data/map/transaction/hover/country/india/state/"
Agg_state_list=os.listdir(path)
Agg_state_list
df3={'State':[], 'Year':[],'Quarter':[],'District':[], 'Transaction_count':[], 'Transaction_Amount':[]}

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['hoverDataList']:
                    amount = z['metric'][0]['amount']
                    count = z['metric'][0]['count']
                    name = z['name']
                    df3['Transaction_Amount'].append(amount)
                    df3['Transaction_count'].append(count)
                    df3['District'].append(name)
                    df3['State'].append(i)
                    df3['Year'].append(j)
                    df3['Quarter'].append(int(k.strip('.json')))
Map_trans=pd.DataFrame(df3)
Map_trans['State'] = Map_trans['State'].apply(format_state)    
Map_trans['State'] = Map_trans['State'].str.replace('Andaman & Nicobar Islands','Andaman & Nicobar')
Map_trans['District'] = Map_trans['District'].str.capitalize()
Map_trans['District'] = Map_trans['District'].str.replace('district','')
Map_trans.to_sql('map_trans',con=engine,if_exists='replace',index=False)

#--------------------------------------------------Map User-----------------------------------------------------------
path= "D:/phonepe/data/data/map/user/hover/country/india/state/"
Agg_state_list=os.listdir(path)
Agg_state_list
df4={'State':[], 'Year':[],'Quarter':[],'District':[], 'Total_users':[]}

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['hoverData']:
                    district = z
                    users = D['data']['hoverData'][z]['registeredUsers']
                    df4['District'].append(district)
                    df4['Total_users'].append(users)
                    df4['State'].append(i)
                    df4['Year'].append(j)
                    df4['Quarter'].append(int(k.strip('.json')))                        
Map_user=pd.DataFrame(df4)
Map_user['State'] = Map_user['State'].apply(format_state)    
Map_user['State'] = Map_user['State'].str.replace('Andaman & Nicobar Islands','Andaman & Nicobar')
Map_user['District'] = Map_user['District'].str.capitalize()
Map_user['District'] = Map_user['District'].str.replace('district','')
Map_user.to_sql('map_user',con=engine,if_exists='replace',index=False)


#-------------------------------------------------Top transaction---------------------------------------------------
path= "D:/phonepe/data/data/top/transaction/country/india/state/"
Agg_state_list=os.listdir(path)
Agg_state_list
df5={'State':[], 'Year':[],'Quarter':[],'Pincode':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['pincodes']:
                    pincode = z['entityName']
                    count = z['metric']['count']
                    trans = z['metric']['amount']
                    df5['Pincode'].append(pincode)
                    df5['Transaction_amount'].append(trans)
                    df5['Transaction_count'].append(count)
                    df5['State'].append(i)
                    df5['Year'].append(j)
                    df5['Quarter'].append(int(k.strip('.json')))                        
Top_trans=pd.DataFrame(df5)
Top_trans['State'] = Top_trans['State'].apply(format_state)    
Top_trans['State'] = Top_trans['State'].str.replace('Andaman & Nicobar Islands','Andaman & Nicobar')
Top_trans.to_sql('top_trans',con=engine,if_exists='replace',index=False)


#---------------------------------------------------Top User----------------------------------------------------------
path= "D:/phonepe/data/data/top/user/country/india/state/"
Agg_state_list=os.listdir(path)
Agg_state_list
df6={'State':[], 'Year':[],'Quarter':[],'Pincode':[], 'User_count':[]}

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['pincodes']:
                    pincode = z['name']
                    count = z['registeredUsers']
                    df6['Pincode'].append(pincode)
                    df6['User_count'].append(count)
                    df6['State'].append(i)
                    df6['Year'].append(j)
                    df6['Quarter'].append(int(k.strip('.json')))                        
Top_user=pd.DataFrame(df6)
Top_user['State'] = Top_user['State'].apply(format_state)    
Top_user['State'] = Top_user['State'].str.replace('Andaman & Nicobar Islands','Andaman & Nicobar')
Top_user.to_sql('top_user',con=engine,if_exists='replace',index=False)
print('Data Successfully Stored.')

