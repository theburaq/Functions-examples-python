#creating function - defining & naming it:
def say_hello():
  print('hellllooooo')

say_hello()

#if we want to repeatedly print a code, then instead of coding it multiple times, we can use a function to call it that many times.
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def show_tree():
  for row in picture:
    for pixel in row:
      if pixel == 1:
        print('*', end='')
      else:
        print(' ', end='')
    print('')

show_tree() 
show_tree()
show_tree()  #can call it as amny times as we want

#using Parameters & Arguments
def my_function(fname):
  print(fname + ' khan')

my_function("Sana")
my_function("Sher")

def say_hello(name, emoji):             #variables inside () are parameters
  print(f'hellllooooo {name} {emoji}')

say_hello('muneera',':-)')

def name_function(fname, lname):        #values inside () are arguments
  print(fname + " " + lname)

name_function('Muneera', 'Mahjabeen')

#postional arguments: positions matter
def say_hello(name, emoji):             
  print(f'hellllooooo {name} {emoji}')

say_hello(':-)','Muneera')
say_hello('Arif',':-)')
say_hello('Andrei',':-)')

#keyword arguments: positions dont matter
def say_hello(name, emoji):             
  print(f'hellllooooo {name} {emoji}')

say_hello(emoji=':-)',name='Muneera')
say_hello(name='Arif',emoji=':-)')

#default arguments: add default values
def say_hello(name='darth vader', emoji=':-)'):             
  print(f'hellllooooo {name} {emoji}')

say_hello('Muneera',':-)')
say_hello()
say_hello('Arif')

