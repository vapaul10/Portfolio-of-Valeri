#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Happy Thanksgiving in Python


# In[2]:


import turtle


# In[3]:


t = turtle.Turtle()
s = turtle.getscreen()


# In[4]:


def feather(r, angle, color):
    for i in range(2):
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(r, angle)
        turtle.left(180-angle)
        turtle.end_fill()
    return


# In[5]:


def brown_feathers(r = 300, angle = 90, n = 7):
    for i in range(n):
        feather(r, angle, "brown")
        turtle.left(15)
    return


# In[6]:


def orange_feathers(r= 200, angle = 90, n = 5):
    for i in range(n):
        feather(r, angle, "orange")
        turtle.left(15)
    return


# In[7]:


brown_feathers()
orange_feathers()


# In[8]:


#body
t.pen(pencolor='black', fillcolor = 'yellow', pensize = 5, speed = 9)
t.begin_fill()
t.circle(70)
t.end_fill()


# In[9]:


#head
t.up()
t.goto(0, 140)
t.down()


# In[10]:


t.pen(pencolor = 'black', fillcolor = 'yellow', pensize = 5, speed = 9)
t.begin_fill()
t.circle(40)
t.end_fill()


# In[11]:


#left eye
t.up()
t.goto(-10, 180)
t.down()


# In[12]:


t.pen(fillcolor = 'black', pensize = 1, speed = 9)
t.begin_fill()
t.circle(5)
t.end_fill()


# In[13]:


#right eye
t.up()
t.goto(10, 180)
t.down()


# In[14]:


t.pen(fillcolor = 'black', pensize = 1, speed = 9)
t.begin_fill()
t.circle(5)
t.end_fill()


# In[15]:


#right leg
t.up()
t.goto(10, 0)
t.down()
t.pen(fillcolor = 'black', pensize = 5, speed = 9)
t.right(90)
t.forward(40)


# In[16]:


#right toe
t.up()
t.goto(10, -40)
t.down()
t.left(45)
t.forward(10)


# In[17]:


#middle toe
t.up()
t.goto(10, -40)
t.down()
t.right(45)
t.forward(10)


# In[18]:


#left toe
t.up()
t.goto(-10, 0)
t.down()
t.pen(fillcolor = 'black', pensize = 5, speed = 9)
t.left(45)
t.forward(40)


# In[19]:


#left leg
t.up()
t.goto(-10, 0)
t.down()
t.pen(fillcolor = 'black', pensize = 5, speed = 9)
t.left(45)
t.forward(40)


# In[20]:


#right toe
t.up()
t.goto(-10, -40)
t.down()
t.left(45)
t.forward(10)


# In[21]:


#middle toe
t.up()
t.goto(-10, -40)
t.down()
t.right(45)
t.forward(10)


# In[22]:


#left toe
t.up()
t.goto(-10, -40)
t.down()
t.right(45)
t.forward(10)


# In[23]:


t.setheading(0)


# In[24]:


#hat
t.up()
t.goto(60, 220)
t.down()
t.backward(120)


# In[25]:


t.up()
t.goto(40, 220)
t.down()


# In[26]:


t.pen(pencolor = 'black', fillcolor = 'black', pensize = 1, speed = 9)
t.begin_fill()
t.left(90)
t.fd(40)
t.left(90)
t.fd(80)
t.left(90)
t.fd(40)
t.end_fill()


# In[ ]:




