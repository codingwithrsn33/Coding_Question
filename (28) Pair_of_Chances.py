def pair_of_countries(countries):
    for i in range(len(countries)):
        for j in range(i+1 , len(countries)):
            print(countries[i] , countries[j])
        
print(pair_of_countries(['USA','India','Australia','Pakistan','South frica']))
