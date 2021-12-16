# A sorting algorithm
# 
# Usage: my_sort(data)

import numpy as np

num_data=400
data=np.random.uniform(0, 1, num_data)

def my_sort(dd):
    
    ds=np.copy(dd)
    ll=np.arange(ds.size-1)
    flag=True
    
    while flag:
          for id in ll:
              flag=False
              if ds[id] > ds[id+1]:
                 temp=ds[id]
                 ds[id]=ds[id+1]
                 ds[id+1]=temp
                 flag=True
              if flag:
                 break
             
    return ds
           
def my_sort_2(dd):
    
    ds=np.copy(dd)
    ll=np.arange(ds.size)
    
    for id in ll:
        ll2=np.arange(id+1, ds.size)
        for jd in ll2:
            if ds[id] > ds[jd]:
               temp=ds[id]
               ds[id]=ds[jd]
               ds[jd]=temp
               
    return ds
           


