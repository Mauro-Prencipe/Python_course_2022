import numpy as np

class data_class():
    def __init__(self):
        self.sz=300
        self.num_scramble=10
        self.num_scramble2=50
        self.limit=0.8
        self.data=np.array([])
        self.data_sw=np.array([])
        self.data_sw2=np.array([])
        self.data_sw3=np.array([])
        self.data_s=np.array([])
        self.w_size=0

    def set_data(self, sz=0, scramble=0, scramble2=0, limit=0):

        if sz == 0:
           sz=self.sz
        else:
           self.sz=sz
      
        if scramble == 0:
           scramble=self.num_scramble
        else:
           self.num_scramble=scramble
           
        if scramble2 == 0:
           scramble2=self.num_scramble2
        else:
            self.num_scramble2=scramble2
           
        if limit == 0:
           limit=self.limit
        else:
           self.limit=limit
     
        ratio_scramble=scramble/sz
        ratio_scramble2=scramble2/sz
    
        if ratio_scramble > limit:
           scramble=int(limit*sz)
       
        if ratio_scramble2 > limit:
           scramble2=int(limit*sz)

        self.data=np.random.uniform(0, 1, sz)
        self.data_s=np.sort(self.data)
        self.data_sw=self.scramble(scramble, self.data_s)
        self.data_sw2=self.scramble(scramble2, self.data_s)     
        self.data_sw3=self.scramble_b(scramble2, self.data_s)
        
        w=np.where(np.array([self.data[id] > self.data[id+1] for id in np.arange(sz-1)]))
        w=np.ravel(w)
    
        self.w_size=w.size

    def scramble(self, num, dd):
     
        num_data=dd.size
        data_sw=np.copy(dd)

        rlist=np.random.choice(num_data, size=num*2, replace=False)
        rlist=rlist.reshape(2, num)

        rlist1=rlist[0]
        rlist2=rlist[1]    
    
        for i,j in zip(rlist1, rlist2):
            temp=data_sw[i]
            data_sw[i]=data_sw[j]
            data_sw[j]=temp                
        
        return data_sw

    def scramble_b(self, num,dd):
    
        num_data=dd.size-1
        data_sw=np.copy(dd)
        rlist1=np.random.choice(num_data, size=num, replace=False)
        rlist2=rlist1+1
    
        for i,j in zip(rlist1, rlist2):
              temp=data_sw[i]
              data_sw[i]=data_sw[j]
              data_sw[j]=temp                
        
        return data_sw        
