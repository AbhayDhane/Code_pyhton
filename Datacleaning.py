import pandas as pd

df = pd.read_excel('/content/Customer Call List.xlsx')

df

df.drop_duplicates(inplace = True)

df =  df.drop(columns=['Not_Useful_Column'])

# issue wiht the last_name column
df['Last_Name']
#removing the special chars from last name
df['Last_Name'] =  df['Last_Name'].str.strip('..._/')

#phone number!,,---> Standard is  123-543-2345

df['Phone_Number']

# conver every phone no. into string
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x)) #1
df['Phone_Number']

df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]','',regex = True) #2
df['Phone_Number']
# to convert every phone number into standard format 123456789 -----> 123-456-6789
df['Phone_Number'] =  df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10]) #3
df['Phone_Number']

#replace nan-- Na-- with nothing

df['Phone_Number'] = df['Phone_Number'].str.replace('nan--','')
df['Phone_Number'] = df['Phone_Number'].str.replace('Na--','')

df['Phone_Number']
# Yes ---> Y
# No ---> N

df['Paying Customer'] = df['Paying Customer'].str.replace('Yes','Y')
df['Paying Customer'] = df['Paying Customer'].str.replace('No','N')

df
