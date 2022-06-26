
from itertools import count


counties = ["Arapahoe","Denver","Jefferson"]
myemptylist = []
myotheremptylist = list()

#print(counties[2])
#print(counties[-2])
#print(len(counties))
#print(counties[0:3])
#counties.append("El Paso")
#counties.insert(2,"El Paso")
#print(counties)
#counties.pop(2)
#counties.pop(3)

#print(counties)
#counties.insert(1,"El Paso")
#counties.remove("Arapahoe")
#counties[1] = "Jefferson"
#counties[2] = "Denver"
#counties.append("Arapahoe")
#print(counties)

counties_tuples = ("Arapahoe","Denver","Jefferson","Sams Town")
#print(counties_tuple[0:-2])

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
###print(counties_dict)
###print(len(counties_dict))

#you can do the same thing instead of print with >>>items() but in VS code
#you may need the print function works fine in propmt
#counties_dict.items()

#if you want just the keys do the below

###print(counties_dict.keys())

#if you just want the values

###print(counties_dict.values())

#getting specific values for keys you use >>>.get end this comment

###print(counties_dict["Arapahoe"])

voting_data = list()
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

#print(len(voting_data))

voting_data.insert(1,{'county' : "El Paso", 'registered_voters': 461149})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data[1] = {"county":"Jefferson", "registered_voters": 432438}
voting_data[2] = {"county":"Denver", "registered_voters": 463353}
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

#print(voting_data)

# a better way would be to use this to specify keys and values...
# voting_data [1] ["county"]=  "New Name"

#if counties[1] == 'Denver':
    #print(counties[1])

#if "El Paso" in counties:
    #print("yo it is here")
#else:
#    print("dude where is my town")

#x = 5
#y = 6
#if x == 5 or y == 5:
#   print("True") 
#else:
#   print("False")


#if "Arapahoe" in counties or "El Paso" in counties:

#    print("Arapahoe or El Paso are in the list of counties.")

#else:
#    print("Arapahoe or El Paso is not in the list of counties.")

#for county in counties:
#    print(county)

#for num in range(5):
#    print(num)

#a better way to use range and len to pull the county names by their interger len index
#for i in range(len(counties)):
 #   print(counties[i])

#these two pull the county names correctly

#        for county in counties_tuples:

 #           print(county)

  #      for i in range(len(counties_tuples)):

   #         print(counties_tuples[i])

#this guy prints the list (not the county name)for every instance on the list

        #for county in counties_tuples:

            #print(counties)

#for county in counties_dict:
 #   print(county)

#for voters in counties_dict.values():
 #   print(voters)

#for county in counties_dict:
 #   print(counties_dict[county])

#for voters in counties_dict.items():
    #print(voters)

#for county, voters in counties_dict.items():
    #print(county, voters)

### the f'in point When iterating over a dictionary:

#The first variable declared in the for loop is assigned to the keys.
#The second variable is assigned to the values.

###use a g dam f-string to formate annoying text like this again


#for county, voters in counties_dict.items():
 #   print(f"{county} county has {voters} registered voters.")

#for i in range(len(voting_data)):
 #     print(voting_data[i]["county"])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#only value
for county_dict in voting_data:

     print(county_dict['registered_voters'])

#only name
for county_dict in voting_data:
    print(county_dict['county'])

print(dir(counties_dict))