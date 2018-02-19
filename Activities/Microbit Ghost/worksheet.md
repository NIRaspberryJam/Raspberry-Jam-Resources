# Microbit ghost game!

<img src="images/cover-ghost.png"/>

## Introduction
In this activity you will be learning how to create a really fun game on the microbit using Python using the LEDS (Light Emitting Diodes) on the Microbit! We will be using LEDs and we will also be using the buttons on the Microbit to make a game where your goal is to avoid a ghost that may appear.

#### You will need:
- BBC Microbit
- USB Cable

## Opening MU

<img src="images/mu.png" align="left" width="70"/>
<img src="images/Mu_new.png" align="right" width="15%"/>

For this activity we're going to use a Micro:bit with MicroPython. We will be writing our code in a program called Mu, which allows us to easily upload it to the Microbit. Before we get started coding, open Mu by pressing the start button in the top left and go into Programming > mu.
Then create a new script for the Microbit by pressing new.


## Let’s start coding!

First we need to import the libraries we are going to need.The first one being the Microbit library which will allow us to access all the special Microbit functions. As we will use it later, we also need to import the random library.

```python
from microbit import *
import random
```

Now we are going to make the images that display the ghost, along with the 2 doors that we are going to use to signal to the player if they are safe or if they’ve lost because they’ve revealed a ghost. Finally we are going to make a blank image to allows use to clear the LEDs on the Microbit.

We makes these images by choosing how bright we want each individual LED to be from 0-9, 0 being off and 9 at its brightest.

Here are some examples of ghosts and doors. You should make your own for game though!

```Python
ghost = Image("09990:"
             "99999:"
             "95959:"
             "99999:"
             "09090")

door1 = Image("00900:"
             "09990:"
             "09590:"
             "09590:"
             "09590")

door2 = Image("00900:"
             "09590:"
             "09590:"
             "09590:"
             "09590")
```
*code continued on next page*

<div class="page-break"></div>

```python
blank = Image("00000:"
             "00000:"
             "00000:"
             "00000:"
             "00000")
```


Now we will place the 3 images we want into a list, these are the ‘ghost’, the  ‘door1’ and ‘door2’. This allows us to randomly pick later. We’ll also create a new variable called score and set it to 0 to start with. “score = 0”.

```Python
all_pics = [ghost, door1, door2]
score = 0
```

Now we need to create the loop to keep the Microbit checking if a button is pressed and to then trigger the rest of the code when the ‘A button’ is pressed. The 'while True:' piece of code will tell the microbit to loop this part of the code so it will repeat it again and again until it detects a change.

```Python
while True:
   if button_a.is_pressed():
```

Next we need to randomly pick an option from our all_pics list.

```python
to_show = random.choice(all_pics)
```

After we do that, we are going to create an if statement to decide what to do if each of the options is picked. We will start with if the ghost is picked. We will tell the player they lost and display their score.

```python
      if to_show == ghost:
           display.show(ghost)
           sleep(1000)
           display.scroll('You lost!')
           display.scroll('Your Score is: ', score)
           score = 0
```

<div class="page-break"></div>

If the ghost isn’t selected, then they it must be a door selected so let’s add a point to their score.

```python
       else:
           display.show(to_show)
           sleep(1000)
           display.show(blank)
           score = score + 1
```

**Now try**

- Can you add more different types of ghosts? Or more kinds of door shapes?
- What about replacing the button input with using a shake?
- What if different doors resulted in different score increases?

Your code should probably look something like this below.

```python
from microbit import *
import random

ghost = Image("09990:"             
              "99999:"
              "95959:"
              "99999:"
              "09090")

door1 = Image("00900:"
              "09990:"
              "09590:"
              "09590:"
              "09590")

door2 = Image("00900:"
              "09590:"
              "09590:"
              "09590:"
              "09590")
```
*code continued on next page*

<div class="page-break"></div>

```python
blank = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")

all_pics = [ghost, door1, door2]
score = 0

while True:
   if button_a.is_pressed():
       to_show = random.choice(all_pics)
       if to_show == ghost:
           display.show(ghost)
           sleep(1000)
           display.scroll('You lost!')
           display.scroll('Your Score is: ', score)
           score = 0
       else:
           display.show(to_show)
           sleep(1000)
           display.show(blank)
           score = score + 1
```

<img src="images/Mu_Flash.png" align="left" width="15%"/>

Then plug your microbit into the Pi and then in Mu you click on the flash button to upload the code onto you Microbit.

The to play your game press on the A button, the aim of the game is to try and avoid getting a ghost appearing on the microbit. The score you get is how many normal doors appear before you get a ghost.
