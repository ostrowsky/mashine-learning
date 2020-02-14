#!/usr/bin/env python
# coding: utf-8

# In[205]:


import numpy as np
from math import sin, exp

def f(x):
    result = []
    for i in x:
        result.append(sin(i/5) * exp(i/10) + 5*exp(-i/2))
    return result


# In[225]:


from matplotlib import pylab
matrix = [[1,1], [1,15]]
A = np.array(matrix)
x = np.arange(15.0)
y = f(x)


# In[226]:


from scipy import linalg


# In[227]:


x_1 = linalg.solve(A,f([1.0,15.0]))
print "корни многочлена первой степени", x_1
print "правая часть многочлена первой степени", np.dot(A,x_1)
print "значения функции в точках 1 и 15", f([1.0, 15.0])
pylab.plot([1.0, 15], np.dot(A,x_1))
pylab.plot(x,y)
pylab.show()


# In[228]:


matrix = [[1,1,1], [1,8,64], [1,15,225]]
A = np.array(matrix)


# In[229]:


x_2 = linalg.solve(A,f([1.0, 8.0,15.0]))
print "корни многочлена второй степени", x_2
print "правая часть многочлена второй степени", np.dot(A,x_2)
print "значения функции в точках 1,8 и 15", f([1.0, 8.0, 15.0])
pylab.plot([1.0, 8.0, 15], np.dot(A,x_2))
pylab.plot(x,y)
pylab.show()


# In[233]:


matrix = [[1,1,1,1], [1,4,16,256], [1,10,100,1000], [1,15,225,3375]]
A = np.array(matrix)
x_3 = linalg.solve(A,f([1.0, 4.0, 10.0,15.0]))
print "корни многочлена Третьей степени", x_3
print "правая часть многочлена второй степени", np.dot(A,x_3)
print "значения функции в точках 1,8 и 15", f([1.0, 4.0, 10.0, 15.0])
pylab.plot([1.0, 4.0, 10.0, 15.0], np.dot(A,x_3))
pylab.plot(x,y)
pylab.show()
final_str = ' '
for i in x_3:
    final_str +=str(round(i,2))+' '
print final_str


# In[235]:


with open('submission_2', 'w') as f:
    f.write(final_str)


# In[ ]:




