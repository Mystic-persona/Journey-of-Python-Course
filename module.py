#Module 1
#pip install pyjokes in the terminal
import pyjokes


#This prints a random joke 
joke = pyjokes.get_joke()
print(joke)

#This is a single line comment
'''This code is about 
comments,module and pip 
This is another line with multiline comment'''

#another module
# pip install emoji in the terminal
import emoji

#This make coding more enjoyable with emoji
greet = emoji.emojize("Hello:grinning:, World! :earth_asia:",language="alias" )
print(greet)

code_fun = emoji.emojize("Coding is fun! :laptop: Let's do it! :rocket:",language="alias")
print(code_fun)

wish = emoji.emojize("Good luck! :thumbsup:",language="alias")
print(wish)