# print ("Hello World")


# type(3)
# type(73.81)
# type("Hello World")
# type(True)



counties = ["Arapahoe", "Denver", "Jefferson"]
counties.insert(1, "El Paso")
counties.remove("Arapahoe")
counties.pop(1)
counties.append("Denver")
counties.append("Arapahoe")
counties

# counties_tuple = ("arapahoe", "denver", "jefferson")
# len(counties_tuple)
# counties_tuple[1]


# counties_dict = {}
# counties_dict["arapahoe"] = 422829
# counties_dict["denver"] = 463353
# counties_dict["jefferson"] = 432438
# counties_dict.items()

# voting_data = []
# voting_data.append({"county":"Arapahoe", "registered_voters":422829})
# voting_data.append({"county":"Denver", "registered_voters":463353})
# voting_data.append({"county":"Jefferson", "registered_voters":432438})
# voting_data.insert(1,{"county":"El Paso", "registered_voters":431149})
# voting_data

for county in counties:
    print(county)
