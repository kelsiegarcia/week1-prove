import time

greeting = ('Aloha! My name is Tutu.', 'Your sassy Hawaiian auntie.', 'It is nice to meet you.', 'Let"s get to know each other.')

for i in greeting:
   print (i) 
   time.sleep(2)

color = input('What is your favorite color?')
print (color.capitalize() + '?\nmine is rainbow!')

joke = input('I have a joke. Why did the unicorn cross the road? ')
print (joke.upper() + '   ... lol, really??')
    

sass = ['That is a pretty terrible answer!', 'The real answer is...' , 'It wanted to be with the chicken! ' , 'Bok.. bok.. Have a great day!']
for i in sass:   
    print (i)
    time.sleep(2)