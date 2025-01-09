multdict={1:{'name':"Shahadat","Phone":98975478},
2:{'name':"Nabil","Phone":6709370},
3:{'name':"shabbu","Phone":916328906}}
print(multdict)

#Adding the data
print(multdict[1])
multdict[4]={'name':"Shahadat","Phone":98975478}
print(multdict)

#Updating the value
multdict[3]['name']="Afzal"
print(multdict)

#Delete

del multdict[4]
print(multdict)

# Going through the data
print(multdict)
for i in multdict.keys():
    print(i,multdict[i])

print(multdict)
for i in multdict.keys():
    print(i,multdict[i] ['name'],multdict[i]['Phone'])


# Going a level deeper with marks

data={1:{'name':"Shahadat","Phone":98975478, 'marks':{'hin':45,'mth':47,'eng':50}
},
2:{'name':"Nabil","Phone":6709370, 'marks':{'hin':35,'mth':41,'eng':13}},
3:{'name':"shabbu","Phone":916328906, 'marks':{'hin':12,'mth':31,'eng':34}}}
print(data)
for i in data.keys():
    print(i,data[i]['name'],data[i]['marks'])
print(data[1]['name'])


swig={'Patna':{'Subregion':'Patnacity','restaurants':{ 201:{
    "name":"ZaikaBiryani",
    "rating":'4.5',
    "rating_count": "200+ ratings",
    "cost": "₹ 400",
    "address": "Ashok Rajpath, Patnacity",
    "cuisine": "Indian, Biryani",
    "menu":{
        "Biryani":{'Price':'200',"veg_or_non_veg": "Non-Veg"}
    }
}}}}

print(swig)

print("_"*60)

for i in swig.keys():
    print(i,swig[i],['resturants'])
