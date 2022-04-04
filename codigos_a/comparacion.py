import json


dfcovid_atl_cord = []
dfcovid_atl = []
dfcovid_cord = []
dfcovid_mayores = []

with open('C:/Users/SENA/Desktop/workspace.hector/Status Colombia Covid.txt') as f:
    dfcovid = json.load(f)

for x in dfcovid:
    if x["Province"] in "Atlantico":
        dfcovid_atl.append({
            "Confirmed_atl" : x["Confirmed"],
            "Deaths_atl" : x["Deaths"],
            "Recovered_atl" : x["Recovered"],
            "Active_atl" : x["Active"],
            "Date_atl" : x["Date"]
        })
    elif x["Province"] in "Cordoba":
        dfcovid_cord.append({
            "Confirmed_cord" : x["Confirmed"],
            "Deaths_cord" : x["Deaths"],
            "Recovered_cord" : x["Recovered"],
            "Active_cord" : x["Active"],
            "Date_cord" : x["Date"]
        })
print(dfcovid_atl)
print(dfcovid_cord)

dfcovid_atl_cord.append(dfcovid_cord)
dfcovid_atl_cord.append(dfcovid_atl)










