#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Looping and counting

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


# In[6]:


#Slicing Strings

name ='Rogers Python'
print(name[0:5]) #as the slicing string follow "upto but not including" rule, slicing will start from first alphabet and end at 4

#print(name[2:4])


# In[14]:


#Using 'in' as a logical operator

fruit = 'banana'

if 'n' in fruit:
    print('Found it')
if 'ban'in fruit:
    print('Found it')
if 'ana' in fruit:
    print('Found it')
if 'nan' in fruit:
    print('Gotcha')


# In[19]:


#String lirary for converting to lower case:

greet = 'Hello Roger'
example = greet.lower()
print(example)


# In[24]:


#String library for converting to upper case:

greet = 'hallo lieber roger'

example = greet.upper()
print(example)


# In[26]:


#Search and replace

greet = 'Hello Rogers'

example = greet.replace('Rogers', 'Blue') 
print(example)


# In[36]:


#Stripping Whitespaces/spaces

greet = '   Hello Rogers   '
print(greet)  #Whitespaces detected

example = greet.strip()
print(example) #Whitespaces removed successfully


# In[35]:


#stripping whitespaces for left side

greet = '     Hello Rogers'
print(greet)  #whitespaces on left side detected

example = greet.lstrip()
print(example) #whitespaces on left side removed successfully 


# In[39]:


#stripping whitespaces for right side

greet = 'Hello Rogers              '
print(greet)  #whitespaces on left side detected

example = greet.rstrip()
print(example) #whitespaces on left side removed successfully 


# In[11]:


#Parsing and Extracting

#From blue.rogers@aalto.uni.fi Tue Oct  5 09:14:16 2020

data = 'From blue.rogers@aalto.uni.fi Tue Oct  5 09:14:16 2020'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1 : sppos]  #atpost+1 as the 'a' positioned on 17 in aalto starts after '@' positioned at 16
print(host)


# In[42]:


#PracticeQuiz


#What does the following Python Program print out?
str1 = "Hello"
str2 = 'There'
bob = str1 + str2
print(bob)

#What does the following Python program print out?
x = '40'
y = int(x) + 2
print(y)


#How would you use the index operator [] to print out the letter q from the following string?
x = 'From marquard@uct.ac.za'
print(x[8])


#How would you use string slicing [:] to print out 'uct' from the following string?

x = 'From marquard@uct.ac.za'
print(x[14:17])


#What does the following Python code print out?

print(len('banana')*7)


#How would you print out the following variable in all upper case in Python?

greet = 'Hello Bob'
print(greet.upper())


#What will the following Python code print out?

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])


# In[73]:


#Ex1: Write code using find() and string slicing to extract the number at the end of the line below. 
######Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
colpos = text.find(':')
#print(colpos)

flnum = text[colpos+5: ]
#print(flnum)

value = float(flnum)
print(value)


# In[ ]:





# In[ ]:




