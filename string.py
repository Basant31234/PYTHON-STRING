

#_____________________________indexing_______________________________________________

#to get the letter of string

t="helLo worLd "
print(t[0])

# the output: h

print(t[4])
# the output: o


#_____________________________slicing_______________________________________________


# to get range of letters in string

t="helLo worLd "
print(t[:10])
# the output:helLo worL

print(t[::2])
# the output:hlowrd

print(t[2:10:2])
# the output:lowr

print(t[3::2])
# the output:L oL



#_____________________________strip -rstrip -lstrip_______________________________________________
# replacing element by another in string 

u="     helLo worLd     "
print(u.strip())

# the output:helLo worLd

u="####helLo worLd####"
print(u.strip("#"))

# the output:helLo worLd

u="####helLo worLd####"
print(u.rstrip("#"))

# the output:####helLo worLd

u="####helLo worLd####"
print(u.lstrip("#"))

# the output:helLo worLd####


#_____________________________title_______________________________________________


# To make the start letter of each word capital even there is a letter after a number 


a="helLo worLd 35n"
print(a.title())

# the output: Hello World 35N


#_____________________________capitalize_______________________________________________



# same as title but for the first letter only.


b="helLo worLd 35n"
print(b.capitalize())

# the output:Hello world 35n


#_____________________________zfill_______________________________________________
#to make all numbers at the same size

z,x,v="1","11","111"
print(z.zfill(3))
print(x.zfill(3))
print(v.zfill(3))

# the output:001
	       # 011
		   # 111	


#_____________________________upper_______________________________________________

#convert all the sting to upper case

c="HelLo worLd"
print (c.upper())

# the output: HELLO WORLD


#_____________________________lower_______________________________________________

#convert all the sting to lowercase


d="HelLo worLd"
print (d.lower())

# the output: hello world


#_____________________________split-rsplit_______________________________________________

#to split the string to elements in list
#rsplit do the same but start from the right side
h="HelLo worLd welcome to ITI"
print (h.split())

# the output: ['HelLo', 'worLd', 'welcome', 'to', 'ITI']


h="HelLo-worLd-welcome-to-ITI"
print (h.split("-",2))

# the output: ['HelLo', 'worLd', 'welcome-to-ITI']


h="HelLo-worLd-welcome-to-ITI"
print (h.rsplit("-",2))

# the output: ['HelLo-worLd-welcome', 'to', 'ITI']



#____________________________center_______________________________________________

#make the word in the center 

e="HelLo worLd"
print (e.center(19,'#'))

# the output: ####HelLo worLd####



#____________________________count_______________________________________________

# count the repatation of the word

r="HelLo worLd HelLo HelLo "
print (r.count("HelLo"))
# the output:3

# can control the range of the string to search in it
print (r.count("HelLo",0,18))

# the output:2

#____________________________swapcase_______________________________________________

#swapping betweeen the lowercase and upper case in the string

q="HelLo worLd HelLo HelLo "
print (q.swapcase())

# the output:hELlO WORlD hELlO hELlO




#____________________________startswith_______________________________________________
# To check the starting letter ine text and the answer is true or false

t="HelLo worLd HelLo HelLo "
print (t.startswith("H"))

# the output:True

print (t.startswith("H",6,9))

# the output:False


#____________________________endswith_______________________________________________
# To check the ending letter ine text and the answer is true or false

t="HelLo worLd HelLo HelLo"
print (t.endswith("o"))

# the output:False

print (t.endswith("H",6,9))

# the output:False
