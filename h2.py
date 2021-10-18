# a=[1,2,6999,4,59,5399,85,100000,100000]
# p=max(a)
# c=[]
# v=0
# for i in a:
#     if i<p :
#         c.append(i)
        
# print(max(c))

a=[1,2,6999,4,59,5399,85,100000,100000]
p=min(a)
c=[]
v=0
for i in a:
    if i>p :
        c.append(i)
        
print(min(c))
import  requests
country="Kyrgyzstan"
token_API = f"https://covid-api.mmediagroup.fr/v1/cases?country={country}"
covid= requests.get(token_API)
covid_json=covid.json()
print(covid_json['All']['confirmed'])


