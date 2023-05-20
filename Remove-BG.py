#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install rembg')


# In[2]:


get_ipython().system('pip install --ignore-installed llvmlite')
get_ipython().system('pip install --upgrade numba')


# In[3]:


get_ipython().system('pip install numpy')
get_ipython().system('pip install opencv-python')


# In[6]:


from rembg import remove 
from PIL import Image 
input_path = 'cl.jpg'
output_path = 'output.png'
input =Image.open(input_path)
output = remove(input)
output.save(output_path)


# In[ ]:




