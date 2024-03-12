#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


import shutil


# In[3]:


# Define the source and destination directories
source_dir = r"C:\Users\Jerry\Documents\python"
destination_dir = r"C:\Users\Jerry\Documents\python"


# In[4]:


# Create a dictionary mapping file types to colors
file_types_colors = {
    "png": "red",
    "docx": "blue",
    "jpg": "green",
    "doc": "yellow",
    "csv": "black"
}


# In[5]:


# Function to organize files based on color tags
def organize_files_by_color():
    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            file_extension = filename.split(".")[-1]
            color = file_types_colors.get(file_extension, "uncategorized")
            color_dir = os.path.join(destination_dir, color)
            os.makedirs(color_dir, exist_ok=True)
            shutil.move(os.path.join(source_dir, filename), os.path.join(color_dir, filename))


# In[ ]:


# Call the function to organize files
organize_files_by_color()

