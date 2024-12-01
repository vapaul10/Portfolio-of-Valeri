#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###Christmas Tree Using Turtle 2


# In[ ]:


import turtle


# In[ ]:


#This Turtle() sets up the turtle platform for drawing the tree
turtle.setup(800, 600)
turtle.title('Happy Holidays')
turtle.bgcolor('lightgreen')
turtle.shape('turtle')


# In[ ]:


#Draw the tree
turtle.fillcolor('forestgreen')


# In[ ]:


#Turtle Pen Up and Pen Down
turtle.penup()
turtle.goto(-180,-180)
turtle.pendown()


# In[ ]:


#Turtle tree criteria
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

