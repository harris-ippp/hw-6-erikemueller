import requests, bs4


#open file
file = open('ELECTION_ID', 'r')
#set loop to open links based on ids in ELECTION_ID
for line in file.readlines():
    source = line.split()
    year = source[0]
    link = ["http://historical.elections.virginia.gov/elections/download/" + str(source[1]) + "/precincts_include:0/"]
#set scraping
    for url in link:
       resp=requests.get(url)
       #save scrapings to files based on year associated with that id
       file_name = year + ".csv"
       with open(file_name, "w") as out:
            out.write(resp.text)
