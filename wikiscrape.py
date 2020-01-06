import requests
from bs4 import BeautifulSoup
import pandas as pd

def getURLContent(link):
	source = requests.get(link).text
	soup = BeautifulSoup(source, "lxml")
	return soup

## ----------------------------- CO2 Emissions DEMO
# soup = getURLContent("https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions")

# # Data we want to gather: Country Name, Fossil CO2 Emissions since 1990
# country = []
# co2 = []

# # Find table with relevant data
# table = soup.find('table', {'class':['wikitable', 'sortable', 'query-tablesorter']})

# # Separate the table into rows
# trs = table.find_all('tr')
# # Delete header row and aggregate rows
# trs = trs[5:]

# # Gather data from the rows and put them into their respective arrays
# for tr in trs:
# 	tds = tr.find_all('td')
# 	country.append(tds[0].text.replace("\xa0",""))
# 	co2.append(tds[1].text.replace(",",""))

# # Use pandas to print and aggregate data
# df = pd.DataFrame()
# df['country'] = country
# df['co2'] = co2
# df['co2'] = df['co2'].astype(float)

# print(df.sort_values(by=['co2'],ascending = False).head(10))



## ----------------------------- Games DEMO

# # Get the HTML from the content
# soup = getURLContent("https://en.wikipedia.org/wiki/List_of_best-selling_video_games")

# # Find the table with the relevant data (Top 50 Video Games)
# tables = soup.find('table',{'class':'plainrowheaders'})

# # Establish the data we want to gather: Game Title, Copies Sold, Release Date
# title = []
# sales = []
# rdate = []

# # Get each row in an array
# trs = tables.find_all('tr')
# # Delete header row
# del(trs[0])

# # Put each data cell into it's respective array
# # Also clean data of extraneous information as well as for type conversion
# for tr in trs:
# 	tds = tr.find_all('td')
# 	title.append(tds[0].text.replace("\n",""))
# 	sales.append(tds[1].text.replace("\n","").replace(",","").replace("[b]",""))
# 	rdate.append(tds[3].text.replace("\n","").replace("[c]",""))

# # Create and Initialize Pandas DataFrame to store data
# df = pd.DataFrame()
# df['title'] = title
# df['sales'] = sales
# df['sales'] = df['sales'].astype('int')
# df['rdate'] = rdate
# df['rdate'] = df['rdate'].astype('datetime64[ns]')

# # Get user input to find sort value
# print("What would you like to sort by? [title || sales || rdate]")
# sort_val = input()

# # Output
# print(df.sort_values(by=[sort_val], ascending=False))


## ----------------------------- WizardsoWP DEMO

# soup = getURLContent("https://en.wikipedia.org/wiki/List_of_Wizards_of_Waverly_Place_episodes")

# tables = soup.find_all('table',{'class':'wikitable plainrowheaders wikiepisodetable'})

# ep_num = []
# director = []

# for x in range(0,len(tables)):
# 	trs = tables[x].find_all('tr')
# 	del(trs[0])
# 	for tr in trs:
# 		tds = tr.find_all('td')
# 		ep_num.append(tds[1].text)
# 		director.append(tds[2].text)

# df = pd.DataFrame()
# df['ep_num'] = ep_num
# df['director'] = director

# print(df.head(5))
# print("The number of times Victor was director was " + str(sum(df['director'].str.count("Victor"))))

## ------------------------------ Countries by Area DEMO

# soup = getURLContent("https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area")

# table = soup.find('table',{'class':'wikitable sortable'})

# rows = table.find_all('tr')
# del rows[0]

# countries = []
# populations = []

# for row in rows:
# 	countries.append(row.find_all('td')[1].text.strip().replace("*",""))
# 	populations.append(int(row.find_all('td')[2].text.strip().replace(",","")))


# df = pd.DataFrame()
# df['country'] = countries
# df['population'] = populations

# df = df.sort_values(by=['population'], ascending=False)

# print(df)