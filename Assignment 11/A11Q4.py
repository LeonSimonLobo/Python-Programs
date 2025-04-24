import pandas as pd 
import numpy as np
john_data=[]
judy_data=[]
print("Enter whether John and Judy are visiting as 'True' or 'False':")
for i in range(10):
    john_val=input(f"Day {i+1} - John: ").strip().capitalize()
    judy_val=input(f"Day {i+1} - Judy: ").strip().capitalize()
    john_data.append(john_val=="True")
    judy_data.append(judy_val=="True")
df=pd.DataFrame({'John':john_data,'Judy':judy_data})
party_days=(df['John']&df['Judy']).values 
days_til_party=np.full(len(df),fill_value=-1) 
next_party=None 
for i in reversed(range(len(df))): 
    if party_days[i]: 
        next_party=i 
        days_til_party[i]=0 
    elif next_party is not None: 
        days_til_party[i]=next_party-i 
df['days_til_party']=days_til_party.astype(int) 
print(df) 