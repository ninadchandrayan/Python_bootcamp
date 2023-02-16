#!/usr/bin/env python
# coding: utf-8

# In[6]:


#The New Line Character: \n

greet = "Hello\nWorld"
print(greet)

statement = "Hello whats your name?\nMy name is Rogers\nHello Mr.Roger"
print(statement)


# In[ ]:


#Assignment: Write a program that prompts for a file name, then opens that file and reads through the file, and print the 
############ contents of the file in upper case. Use the file words.txt to produce the output below. You can download the 
############ sample data at http://www.py4e.com/code3/words.txt

fname = input("Enter file name: ")
fh = open(fname)
fx = fh.read( )
fy = fx.upper( )
fz = fy.rstrip ( )
print(fz)


# In[ ]:


#Assignment: Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines 
############ of the form: X-DSPAM-Confidence:    0.8475. Count these lines and extract the floating point values from each of 
############ the lines and compute the average of those values and produce an output as shown below. Do not use the sum() 
############ function or a variable named sum in your solution. You can download the sample data at 
############ http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.


fname = input('Please enter file name')
ofile = open(fname)
rfile = ofile.read( )
count = 0
total = 0
for lines in ofile:
    if lines.startswith('X-DSPAM-Confidence:'):
        txt = lines.find('0')
        numbr = float(lines[txt:])
        count = count + 1
        total = total + numbr
        average = total/count
print('Average spam confidence:', average)


# In[ ]:





# In[ ]:




