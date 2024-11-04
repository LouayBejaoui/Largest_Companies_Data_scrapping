from bs4 import BeautifulSoup;
import requests;

url ='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page =requests.get(url) 
soup = BeautifulSoup(page.text ,'html.parser')

table =soup.find_all('table')[0]

header_titles = table.find_all('th')

titles = [title.text.strip() for title in header_titles]
import pandas as pd;

df =pd.DataFrame(columns=titles)

rows = table.find_all('tr')

for row in rows[1:] : 
    contents = row.find_all('td')
    cont = [content.text.strip() for content in contents]
    
    l =len(df)
    df.loc[l]=cont
    
df.to_csv(r'C:\Users\louay\Desktop\web tries\PythonWebscrapping\csv files\companies.csv', index= False)
