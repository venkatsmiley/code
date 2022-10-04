#!/usr/bin/env python
# coding: utf-8

# In[57]:


import numpy as np 
import 


a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]] , dtype=('int32'))
print(a)


print(a.itemsize)

print(a.size)

print(a.shape)

print(a.nbytes)

a[0,0:-1:2]

b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

print(b)

b[:,1,:]


# In[95]:


##### ALL ZERO MATRIX :

np.zeros((2,5))

np.ones((2,5))

np.full((2,5) , 99 , dtype='float')

b=np.full_like(a,4)

np.random.rand(4,3)

np.identity((5) , dtype='int64')

arr=np.array([1,2,3])

r=np.repeat([arr],5,axis=1)

c=np.array([1,2,3])

b=c.copy()

c[0]=8

print(b)
print(c)


# In[102]:


a=np.array([1,2,3,4])

print(a)

print(a+2)

print(a*2)

print(a/2)

print(a**2)

c=np.sin(a)

print(c)


# In[107]:


a=np.ones((2,3) , dtype='int')
print(a)

b=np.full((3,2) , 2)
print(b)

c=np.matmul(a,b)
print(c)


# In[112]:


stats=np.array([[1,2,3],[4,5,6]])
c=np.min(stats)
print(c)

c=np.max(stats)
print(c)

c=np.sum(stats)
print(c)


# In[115]:


before=np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after=before.reshape((8,1))
print(after)


# In[118]:


v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])

np.hstack([v1,v2,v2,v1])


# In[127]:


filedata=np.genfromtxt('rough.txt' , delimiter=',')
filedata=filedata.astype('int64')
print(filedata[filedata>50])


# In[137]:


a=np.array([1,2,3,4,5,6,7,8,9])


# In[ ]:





# In[ ]:




