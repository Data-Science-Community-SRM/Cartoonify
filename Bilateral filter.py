#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


img_path = r'C:\Users\ANUSHKA GARG\Desktop\Bilateral filter\images\img1.jpg'
img = cv2.imread(img_path)
cv2.imshow("image", img)
cv2.waitKey(0)
plt.imshow(img)


# In[3]:


# Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("image", gray)
cv2.waitKey(0)
plt.imshow(gray, cmap="Greys_r")


# In[4]:


gray = cv2.medianBlur(gray, 3)
cv2.imshow("image", gray)
cv2.waitKey(0)
plt.imshow(gray, cmap = "BuPu_r")


# In[5]:


edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
cv2.imshow("image", edges)
cv2.waitKey(0)
plt.imshow(edges, cmap="CMRmap")


# In[11]:


# bilateral filter
color = cv2.bilateralFilter(img, 5, 50, 5)
#color = cv2.bilateralFilter(img, 23, 51, 51)
cv2.imshow("image", color)
cv2.waitKey(0)
plt.imshow(color)


# In[7]:


cartoon = cv2.bitwise_and(color, color, mask = edges)
cv2.imshow("image", cartoon)
cv2.waitKey(0)
plt.imshow(cartoon)


# In[ ]:




