#!/usr/bin/env python
# coding: utf-8

# In[50]:


def pluralize(lst):
    words=[]
    for word in lst:
        words.append([word,1])
    d = {}
    for element in words:
        
        if element[0] not in d:
        
            d[element[0]] = []
        
        d[element[0]].append(element[1])    
    s={}
    for i,j in d.items():
        s[i]=sum(j)
    final = set()
    
    for m,y in  s.items():
        if y>1:
            final.add(m+str("s"))
        else:
            final.add(m)
    

    return final




