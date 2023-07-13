# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 16:20:08 2023

@author: Tyler
"""

#Covid 19 cases per state as of 2021
import pandas as pd 
infected_states2021=pd.read_csv('C:\\Users\Tyler\Python assignments\\01-01-2021.csv')
infected_states2021.to_excel('C:\\Users\Tyler\Python assignments\\01-01-2021.xlsx')
AData=pd.read_excel('C:\\Users\Tyler\Python assignments\\01-01-2021.xlsx',index_col=1)
Data_clean_2021=AData[['Confirmed']]
#Covid 19 cases per state as of 2022
infected_states2022=pd.read_csv('C:\\Users\Tyler\Python assignments\\01-01-2022.csv')
infected_states2022.to_excel('C:\\Users\Tyler\Python assignments\\01-01-2022.xlsx')
BData=pd.read_excel('C:\\Users\Tyler\Python assignments\\01-01-2022.xlsx',index_col=1)
Data_clean_2022=BData[['Confirmed']]

#Covid 19 Cases per state as of 2023
infected_states2023=pd.read_csv('C:\\Users\Tyler\Python assignments\\01-01-2023.csv')
infected_states2023.to_excel('C:\\Users\Tyler\Python assignments\\01-01-2023.xlsx')
CData=pd.read_excel('C:\\Users\Tyler\Python assignments\\01-01-2023.xlsx',index_col=1)
Data_clean_2023=CData[['Confirmed']] 

top_state_cases_2021=Data_clean_2021.sort_values('Confirmed',ascending=False).head(10)

top_state_cases_2022=Data_clean_2022.sort_values('Confirmed',ascending=False).head(10)

top_state_cases_2023=Data_clean_2023.sort_values('Confirmed',ascending=False).head(10)



df_list=[top_state_cases_2021,top_state_cases_2022,top_state_cases_2023]

Data_merged = pd.concat(df_list, axis='columns')
total_cases_df=Data_merged.set_axis(['2020 Cases','2021 Cases','2022 Cases'], axis='columns')

#Filling in data Gaps
#Tennessee
tn2=Data_clean_2022.loc['Tennessee','Confirmed']
tn3=Data_clean_2023.loc['Tennessee','Confirmed']
tn_lst=[tn2,tn3-tn2]

tn_dict=dict(zip(['2021 Cases','2022 Cases'],tn_lst))
df1=pd.DataFrame(tn_dict,index=['Tennessee'])
#Michigan
Mg1=Data_clean_2021.loc['Michigan','Confirmed']
Mg2=Data_clean_2022.loc['Michigan','Confirmed']
Mg_lst=[Mg1,Mg2-Mg1]
Mg_dict=dict(zip(['2020 Cases','2021 Cases'],Mg_lst))
df2=pd.DataFrame(Mg_dict,index=['Michigan'])




#subtraction function
dfa= total_cases_df.assign(diff2_1=total_cases_df['2021 Cases']-total_cases_df['2020 Cases'],diff3_2=total_cases_df['2022 Cases']-total_cases_df['2021 Cases'])
diff2_1=total_cases_df['2021 Cases']-total_cases_df['2020 Cases']
diff3_2=total_cases_df['2022 Cases']-total_cases_df['2021 Cases']
dfa_lst=[top_state_cases_2021,diff2_1,diff3_2]

dfinc=pd.concat(dfa_lst, axis='columns')
dfinc=dfinc.set_axis(['2020 Cases','2021 Cases','2022 Cases'], axis='columns')


#Merge
DFF=dfinc.fillna(df1)
DFF2=DFF.fillna(df2)
DFF2.plot.bar(xlabel='States',ylabel='Total Confirmed Cases(Millions)',title='Total Confirmed Cases Per State Per Year')
DFF2.to_csv('C:\\Users\Tyler\Python assignments\\Top 10 States Data.csv')
#Arizona specific

az1=Data_clean_2021.loc['Arizona','Confirmed']
az2=Data_clean_2022.loc['Arizona','Confirmed']
az3=Data_clean_2023.loc['Arizona','Confirmed']

azlst=[az1,az2,az3]
azdict=dict(zip(['2020 Cases','2021 Cases','2022 Cases'],azlst))

az= pd.DataFrame.from_records(azdict,index=['Arizona'])
dif1=az['2021 Cases']-az['2020 Cases']
dif2=az['2022 Cases']-az['2021 Cases']
dfb_lst=[az['2020 Cases'],dif1,dif2]
az=pd.concat(dfb_lst, axis='columns')
az=az.set_axis(['2020 Cases','2021 Cases','2022 Cases'], axis='columns')


az.plot.bar(ylabel='Total Confirmed Cases(Millions)',title='Total Cases For Arizona')
az.to_csv('C:\\Users\Tyler\Python assignments\\Arizona Cases Data.csv')

#All States/Provinces Data
Big_Data=[Data_clean_2021,Data_clean_2022,Data_clean_2023]

dfc=pd.concat(Big_Data,axis='columns')
dfc=dfc.set_axis(['2020 Cases','2021 Cases','2022 Cases'], axis='columns')
dfc.plot.bar(ylabel='Total Confirmed Cases(Millions)',title='Total Cases Per State Per Year')
dfc.to_csv('C:\\Users\Tyler\Python assignments\\United States Cases.csv')
# Lowest States/Provinces Cases Data
lowest_state_cases_2021=Data_clean_2021.sort_values('Confirmed',ascending=True).head(20)

lowest_state_cases_2022=Data_clean_2022.sort_values('Confirmed',ascending=True).head(20)

lowest_state_cases_2023=Data_clean_2023.sort_values('Confirmed',ascending=True).head(20)

df2_list=[lowest_state_cases_2021,lowest_state_cases_2022,lowest_state_cases_2023]
Data_merged2 = pd.concat(df2_list, axis='columns')
lowest_cases_df=Data_merged2.set_axis(['2020 Cases','2021 Cases','2022 Cases'], axis='columns')
lowest_cases_df=lowest_cases_df.sort_values('2020 Cases',ascending=True).head(10)
dfd= lowest_cases_df.assign(diff2_1=lowest_cases_df['2021 Cases']-lowest_cases_df['2020 Cases'],diff3_2=lowest_cases_df['2022 Cases']-lowest_cases_df['2021 Cases'])
ldiff1=lowest_cases_df['2021 Cases']-lowest_cases_df['2020 Cases']
ldiff2=lowest_cases_df['2022 Cases']-lowest_cases_df['2021 Cases']
dfd_lst=[lowest_cases_df['2020 Cases'],ldiff1,ldiff2]

dfd=pd.concat(dfd_lst, axis='columns')
dfd=dfd.set_axis(['2020 Cases','2021 Cases','2022 Cases'], axis='columns')
gph=dfd.plot.bar(xlabel='States',ylabel='Total Confirmed Cases(Thousands)',title='Lowest Cases in the United States')

gph1=dfd.plot.bar(xlabel='States',ylabel='Total Confirmed Cases(Thousands)',title='Lowest Cases in the United States',ylim=(0,1000))
dfd.to_csv('C:\\Users\Tyler\Python assignments\\Lowest 10 States or Provinces.csv')
