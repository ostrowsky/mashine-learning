#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
with open('sentences.txt', 'r') as f:
    read_data = f.readlines()
print read_data



# In[41]:


j = 0
words = []
tokens = {}
for line in read_data:
    line = re.split('[^a-z]', line.lower())
    for i in line:
        while '' in line:
            line.remove('')
        if i not in words:
            words.append(i)
            tokens[j] =i
            j+=1
print tokens
 



# In[104]:


import numpy as np
shape = (len(read_data), len(tokens))
matrix = np.zeros(shape)

for token in tokens:                        #(len(matrix[0,:])):
    i = 0
    for line in read_data:
        
        counter = 0
        for word in re.split('[^a-z]', line.lower()):
            #print i, token, tokens[token],word, line
            if tokens[token] == word:
                counter += 1
                #print counter
        matrix[i, token] = counter
        #if matrix[i,token] > 2.0:
            #print i, token, tokens[token], matrix[i, token], line
        i += 1
print matrix
 


# In[103]:


import numpy as np
shape = (len(read_data), len(tokens))
matrix = np.zeros(shape)

for token in tokens:                        #(len(matrix[0,:])):
    i = 0
    for line in read_data:
        
        counter = 0
        for word in re.split('[^a-z]', line.lower()):
            #print i, token, tokens[token],word, line
            if tokens[token] == word:
                counter += 1
                #print counter
        matrix[i, token] = counter
        #if matrix[i,token] > 2.0:
            #print i, token, tokens[token], matrix[i, token], line
        i += 1
print matrix


# In[151]:


from scipy.spatial import distance
line_1 = matrix[0,:]
distances = []
for i in range(1,len(matrix[:,0])):
    line =  matrix[i,:]
    distances.append((i,distance.cosine(line_1, line)))
final_str = ''
for i in range(2):
    final_str += ' '+str(sorted(distances, key=lambda i:i[1] )[i][0])
print final_str


# In[152]:


with open('submission_1', 'w') as f:
    f.write(final_str)


# In[ ]:




