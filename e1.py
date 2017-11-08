import requests, pandas as pd
from bs4 import BeautifulSoup as bs
#set link
addr = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
#set request and site to scrape
resp = requests.get(addr)
#set html
html = resp.content
#set soup
soup = bs(resp.text, 'html.parser')

#find ids
electionid =soup.find_all("tr", "election_item")
#pull only ids
e_id = [x.get("id").rpartition('-')[2] for x in electionid]
# pull years into first column
year = [x.find("td").contents[0] for x in electionid]
#put ids in second columns
id = [year[x] + " " + e_id[x] for x in range(len(e_id))]
#name file
file_name = "ELECTION_ID"
#save file
with open (file_name, "w") as out:
    for item in id:
        out.write("{}\n".format(item))
