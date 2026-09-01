import pandas as pd
#list data
data = [100,102,104,200,202]

series = pd.Series(data,index=['a','b','c','d','e'])
#update series using loc[]
series['e'] += 200
# print(series)



#dictionary data , keys act like indices
calories = {"Day 1":1898,"Day 2":1992,"Data 3":2080}
ds = pd.Series(calories)
#update series using loc[] 
ds.loc["Day 1"] += 100
print(ds.iloc[0])
print(ds.loc["Day 2"])
print(ds)
# filter by value
print(ds[ds >= 2000])
print(ds[ds<2000])


# Home work
pokemon = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard"]
ps = pd.Series(pokemon)
print(ps)

student_record = {
    "Name" : "ABCD",
    "Roll No." : 43,
    "Grades" : ['A+','A','A+','A'],
    "Languages known":['English','German'],
    "Hobbies" : ['coding','sleeping','exercise','reading']
}
sd = pd.Series(student_record)
print(sd)
