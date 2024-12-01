#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###Christmas Tree Using Turtle 2


# In[ ]:


import turtle


# In[ ]:


#This Turtle() sets up the turtl platform for drawiing the tree
turtle.setup(800, 600)
turtle.title('Happy Holidays')
turtle.bgcolor('lightgreen')
turtle.shape('turtle')


# In[ ]:


#draw the tree
turtle.fillcolor('forestgreen')


# In[ ]:


#define a function using def
turtle.penup()
turtle.goto(-180,-180)
turtle.pendown()


# In[ ]:


turtle.begin_fill()
turtle.goto(0, 220)
turtle.goto(180, -180)
turtle.goto(7, -180)
turtle.goto(7, -260)
turtle.goto(-7, -260)
turtle.goto(-7, -180)
turtle.goto(-180, -180)
turtle.end_fill()


# In[ ]:


# Draw the Star
turtle.color("yellow")

turtle.penup()
turtle.goto(0, 260)
turtle.pendown()

turtle.begin_fill()
turtle.goto(11, 230)
turtle.goto(40, 230)
turtle.goto(16, 211)
turtle.goto(26, 181)
turtle.goto(0, 200)
turtle.goto(-26, 181)
turtle.goto(-16, 211)
turtle.goto(-40, 230)
turtle.goto(-11, 230)
turtle.goto(0, 260)
turtle.end_fill()


# In[ ]:


# Keep the window open
turtle.done()

