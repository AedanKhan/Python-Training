# So we have seen how to print, but what if we wanted to enter some data?

print("What is your name?") # Here we see it simply printed.

# But now we want the user to actually give an answer to this.

#input("What is your name?") # So this logic entails that we want the user to enter an input into the console

print("Hello {input}") # So this is kind of the logic but not quite

print("Hello " + input("What is your name?"))

#----------------# 
# Now let's add an exclamation mark to line 11 #

print("Hello " + input("What is your name?") + "!")