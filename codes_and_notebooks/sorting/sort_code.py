# Sorting algorithms


import numpy as np


class my_sort_class():
    def __init__(self):
        self.meth='max'
        self.meth_orig='max'

    def sort(self, dd, method='default'):
        
        if method=='default':
           fun=self.meth
        else:
           fun=method
           
        if fun=='ss' :
           return self.my_sort(dd)
        elif fun=='ms':
           return self.my_sort_b(dd)
        elif fun=='dbc':
           return self.my_sort_2(dd)
        elif fun=='msr':
             return self.my_sort_c(dd)
        elif fun=='vms':
           return self.my_sort_3(dd)
        elif fun=='max':
           return self.my_sort_4(dd)
        elif fun=='numpy':
            return self.np.sort(dd)
        elif fun=='smart':
            return self.my_sort_smart(dd)        
        else:
            print("Method %s not defined" % fun)
        
    def set_method(self, meth='default'):
        
        if meth=='default':
           self.meth=self.meth_orig
        else:   
           self.meth=meth
    
    def info(self):
        print("\nSorting function: %s " % self.meth)
       
    def my_sort(self,dd):
        '''
        Single swap per cycle sorting function 
        '''
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
                     break
                 
        return ds

    def my_sort_b(self,dd):
        '''
        Multiple swap per cycle sorting function
        '''
        ds=np.copy(dd)
        ll=np.arange(ds.size-1)
        flag=True
        
        while flag:
              flag=False
              for id in ll:
                  if ds[id] > ds[id+1]:
                     temp=ds[id]
                     ds[id]=ds[id+1]
                     ds[id+1]=temp
                     flag=True
                 
        return ds

    def my_sort_c(self,dd):
        '''
        msr: Multiple swap with recursion
        '''
        ds=np.copy(dd)
        ll=np.arange(ds.size-1)
        flag=False
    
        for id in ll:
            if ds[id] > ds[id+1]:
               temp=ds[id]
               ds[id]=ds[id+1]
               ds[id+1]=temp
               flag=True
               
        if flag:
           ds=self.my_sort_c(ds)
        
        return ds
       
    def my_sort_2(self,dd):
        '''
        Double cycle sorting function
        '''    
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
           
    def my_sort_2b(self,dd):
        
        ds=np.copy(dd)
        ll=np.arange(ds.size)
        
        for id in ll:
            ll2=np.arange(id+1, ds.size)
            for jd in ll2:
                if ds[id] > ds[jd]:
                   ds[id]=ds[jd]
                   ds[jd]=dd[id]
                
        return ds
        
            
    def my_sort_3(self,dd):
        '''
        Vectorized version of the multiple swap sorting function
        '''    
        ds=np.copy(dd)
        sz=ds.size
        sz1=sz-1
        ll=np.arange(sz1)
    
        w=np.where(np.array([ds[id] > ds[id+1] for id in ll]))
        w=np.ravel(w)
            
        
        while w.size > 0:
              for id in w:
                  temp=ds[id]
                  ds[id]=ds[id+1]
                  ds[id+1]=temp
              w=np.where(np.array([ds[id] > ds[id+1] for id in ll]))
              w=np.ravel(w)
        
        return ds
    
    def my_sort_4(self,dd):
        '''
        Maximum element sorting function
        '''    
        sz=dd.size
        ll=np.arange(sz)   
        ds=np.array([])
        
        flag=np.repeat(True, sz)
        
        w=np.where(flag==True)
        w=np.ravel(w)
        
        count=sz
        
        while count > 0:
              count=count-1
              mn=dd[w[0]]
              idm=w[0]
        
              for id in w:
                    if dd[id] < mn:
                       mn=dd[id]
                       idm=id                
               
              flag[idm]=False       
              ds=np.append(ds, mn)
              w=np.where(flag==True)
              w=np.ravel(w)
                  
        return ds
        
    def my_sort_smart(self, ds, thr=60, info=False, sdef=200, n_sample=50):
        '''
        The function chooses between ms and max algorithms to sort data
        
        Args:
            ds:  data set to be sorted
            thr: parameter used to define an average 'distance' (par) between 
                 data to be swapped. par='size of the dataset'/thr. If
                 the 'distance' estimated from a sample drawn from the original
                 dataset is lower than par, the ms algorithm is chosen; 
                 otherwise, max is used.
            info: if True, diagnostic info are printed (default False)
            sdef: distance estimation is performed only if the size
                  of the dataset is larger than sdef (default 200).
                  If the size of the dataset is smaller than sdef, the max
                  algorithm is used.
            n_sample: size of the sample drawn from the original dataset
                      to be sorted (default 50)
        '''
        sz=ds.size
        
        distance=0.
        par=0.
        p_choice=False
       
        if sz > sdef:
           distance=self.sample(n_sample, ds)     
           par=sz/thr
           if distance < par: p_choice=True
           
        if p_choice:
           dd=self.my_sort_b(ds)
        else:
           dd=self.my_sort_4(ds)
           
        if info:
           print("\n*** Smart sort ***\nSize: %5i" % sz)
           print("Distance: %5.2f" % distance)
           print("Thr:      %5.2f" % thr)
           print("Par:      %5.2f" % par)
           print("P_choice  %s" % p_choice)
           if p_choice:
              print("ms algorithm is chosen")
           else:
              print("max algorithm is chosen")
                   
        return dd
           
        
    def sample(self,ns, ss):
        '''
        Function used by my_sort_smart to decide which method
        to use for sorting data
        '''
        sample=ss[0:ns]
        ls=np.arange(ns)
        
        distance=0
        
        for id in ls:
            ld=np.arange(id+1,ns)
            for jd in ld:
                if ss[id] > ss[jd]:
                   distance=distance+(jd-id)
                              
        distance=distance/ns
        
        return distance
            

    