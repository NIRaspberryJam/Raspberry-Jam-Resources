# Hack the Dazzling Raspbertree

<img src="Images/header.png" width="950px" align="centre"/>

### What will you be doing in this activity?

In this activity, you will be hacking the LED Christmas tree using Python through a computer network. A computer network is a big set of computers that are connected through a wire (or through Wi-Fi nowadays). Computer networks are everywhere. Schools and businesses would have all their computers wired together, and even your house is just one big personal computer network.

#### Opening and setting up Python

<img src="Images/desktop.jpg" width="750px" />

To open the Python 3 development environment (IDLE3) we will first need to click the terminal icon on the top bar (highlighted by the box in the picture above). Once terminal has opened type in `sudo idle3 &` and press enter. Python IDLE should now open.


<img src="Images/tip.png" width="750px" align="centre"/>

<div class="page-break"></div>

### Networking with Python

For us to network with python we will need to import the `network` package. We will import this package using the `import` function. Like so...


```python
import network
```

Then to talk to the tree, we will need to use network's `call` function to open a connection to the LED tree. The `call` function uses an IP address or hostname. Each device that's in a network will have its own unique IP address (or hostname), even the tree! In our script, we'll use tree.local which is the default hostname of the tree, or you can use its IP address.


```python
network.call("tree.local")
```

### Talking to the Christmas Tree

The Pi tree has a special way of controlling the LEDs. Each LED has three colour values, one for red, one for green and one for blue. On top of that, we will also need an ID to reference each individual LED. Each colour value goes from 0 to 255 (0 meaning off and 255 meaning full brightness). Each value is put together into a string. The following diagram also explains this.

<img src="Images/format.png" width="350px" />

In example below, we are going to set LED 1 to white and full brightness. We can do that using `network.say` command, along with our message itself in square brackets.

```python
network.say("[1,255,255,255]")
```

Now save your code, and run it using **F5**. You should see the LED you chose on the tree, light up. If it does then your code works and you can move on to the next task, if it doesn’t work then check your code and if it still doesn’t work then grab a volunteer.

_So far, this is what you should have…_

```python
import network
network.call("tree.local")
network.say(“[1,255,255,255]”)
```

Now try changing other LEDs to different colours and play about with them (why not try changing some of the colour's values to zero as well?)

### Making the LEDs randomly twinkle

Now that you are a master at controlling the tree’s LEDs, let’s take is a step further. In this section, we will learn how to make an LED flash at random moments. First of all, make a new script by going to **File > New file**.


We’ll start off by importing the `network` package again but we will also need to import two other libraries, them being the `random` package and the `sleep` function from the `time` package. We’ll import them all using,

```python
import network
import random
from time import sleep
```



And just like last time, we’ll call the tree using the network’s call function. 

```python
network.call("tree.local")
```

<div class="page-break"></div>

For us to make it randomly twinkle more than once, we will need to put the main bit of our code in a loop. In this case, we will put it into a `while` loop and set the condition to True. Everything that is tabbed in after the loop must be tabbed. **Indentation is extremely important with Python!** It uses it to figure out which code should be inside the loop and which should be before/after it.

```python
while True:
```

Next, you need to pick your first colour to send.   
```python
  network.say(“[1,100,175,85]”)
```

Now, we need to wait for a bit before switching to the other colour. To do this we use a `sleep` command. To make things a little random as well, we use `random.randint(1, 5)`. This will select a number of seconds between 1 and 5 each time.   
```python
  sleep(random.randint(1, 5))
```

Then, you will need to add the other colour followed finally by another `sleep` for random time. 

```python
  network.say(“[1,255,255,255]”)
  sleep(random.randint(1, 5))
```

<div class="page-break"></div>

_Now you should have_:

```python
import network
import random
from time import sleep

network.call("tree.local")

while True:
    network.say(“[1,100,175,85]”)
    sleep(random.randint(1, 5))
    network.say(“[1,255,255,255]”)
    sleep(random.randint(1, 5))
```

Now `save` and press `F5` to run the script and see your LED flash!

**Now Try** changing the random time values and running the script again! Can you add some more different colours so it flickers between even more than 2 colours?   

#### Controlling a Range of LEDs

Now let’s try to control a range of LEDs at the same time with a small snippet of code.

First, we are going to need to open up a new file, so go to **File > New File** to create a new file.

For us to network using python we will need to import the `network` package again, along with the sleep command from time. We will import this package using the `import` function. Like so...

```python
import network
from time import sleep
```

Then we will continue by stating our Christmas tree and making the initial call to it with the following.   



```python
network.call("tree.local")
```

Now we are going to use to use the `range` loop function of python to send the Christmas tree the led number but with incrementing our LED number each time for the range of LEDs we want to control.

When we set the message, we state the colour here, as an example, we have set each colour to 255 to make the led white. You can change each of these values to your own colour in the order that was shown before. Then in the message, we have `x` refer to the number that is set by the range.

we are using `str` to turn what is a list of number to string of numbers and symbol.

```python
for x in range(1, 4):
    network.say(str([x, 255, 255, 255]))
    sleep(0.5)
```

This code is saying to control LEDs 1-3 with the colour combination that we stated in the message. This is done by having the `network.say` repeat each time we increase the X number.

Now you should be able to run the code and control the multiple LEDs!

### What next?
Can you...
- Control 10 LEDs at once using an loop?
- Make an LED come up as a rainbow?
- Try having the colour of the twinkle become random every time a new twinkle happens.
