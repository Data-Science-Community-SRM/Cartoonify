#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[26]:


image_path = r"C:\Users\rusal\Cartoonify\Project-5\scenery.jpg"


# In[27]:


image = cv2.imread(image_path)


# In[28]:


plt.imshow(image, cmap = "gray")


# ## Applying Pencil Sketching 

# ### Defining the functions

# In[29]:


def gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# In[30]:


def blur(image):
    return cv2.GaussianBlur(image,(25,25),0)


# In[31]:


def pen_sketch(image1,image2):
    return cv2.divide(image1,image2,scale = 250.0)


# ### We create a copy of the image and call the functions on the image

# In[32]:


img_copy = np.copy(image)


# In[33]:


gray_img = gray(img_copy)
plt.imshow(gray_img, cmap = "gray")


# In[34]:


blur_img = blur(gray_img)
plt.imshow(blur_img, cmap = "gray")


# #### This is how the final pencil sketch looks when applied on the image

# In[35]:


sketch_img = pen_sketch(gray_img,blur_img)
plt.imshow(sketch_img, cmap = "gray")


# #### Here is the original picture for comparison

# In[36]:


plt.imshow(image)


# ## Applying Pencil Edge

# ### Defining the functions (We shall use the same GrayScale function as above)

# In[37]:


def med_blur(image):
    return cv2.medianBlur(image, 25)


# In[38]:


def laplacian(image):
    return cv2.Laplacian(image, -1, ksize=3)


# In[39]:


def invert(image):
    return 255-image


# In[40]:


def pencil_edge(image):
    return cv2.threshold(image,150,255, cv2.THRESH_BINARY)


# #### Creating a copy of original image and calling the above functions

# In[41]:


img_copy = np.copy(image)


# In[42]:


gray_img = gray(img_copy)
plt.imshow(gray_img, cmap = "gray")


# In[43]:


med_img = med_blur(gray_img)
plt.imshow(med_img, cmap = "gray")


# In[44]:


laplace_img = laplacian(med_img)
plt.imshow(laplace_img, cmap = "gray")


# In[45]:


invert_img = invert(laplace_img)
plt.imshow(invert_img, cmap = "gray")


# #### This is the final Pencil Edge on the image

# In[46]:


pencil_edge_img = pencil_edge(invert_img)
plt.imshow(pencil_edge_img[1], cmap = "gray")


# In[ ]:




