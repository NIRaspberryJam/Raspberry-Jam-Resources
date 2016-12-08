# Getting started with Pi-Stop Traffic Light

<img src="Images/MainPhoto.jpg" width="750px" />

## What is the Pi-Stop?

The Pi-Stop is a mini traffic light that uses four pins to interact with the Pi, three of which are inputs for the 3 different LEDs (red, amber and green) and the fourth is for ground to complete the circuit.

## What are we doing in this worksheet?

In this worksheet we are going to learn how to control the Pi-Stop using the Raspberry Pi and Scratch. As well as grasping how to use basic blocks like `broadcast` , `wait` and the different types of `loops`.

<div class="page-break"></div>


## Attaching the Pi stop

<img src="Images/RaspberryPiAttach.png" width="420px" />

Firstly ensure that your Pi is **powered off and unplugged**, this is very important. Make sure when attaching the Pi-Stop that the LEDs are **facing away** from your Pi. The diagram above shows the pins that you attach the Pi-Stop to, as well as which direction it should be facing.

**TIP** : There should be **7** pins **to the left** of the Pi-Stop so you could count seven pins across and then insert one end of the Pi-Stop on the eighth pin.

After you have attached the Pi-Stop the LEDs should light up dimly when you open `ScratchGPIO7`.


### Opening and setting up Scratch

<img src="Images/ScratchGPIO7.png" align="left"/>

Go to the Pi's desktop and open `ScratchGPIO7`, if it isn't there try and click the `Install ScratchGPIO7` icon, after a moment `ScratchGPIO7` should appear on the desktop. When you open Scratch, a pop-up window should say `Remote sensor connections enabled`.

## How to use the Pi-Stop

In Scratch we will be using the `broadcast` function which tells the GPIO pins to turn the power off or on, to the pins which the Pi-Stop's LEDs are using.

<div class="page-break"></div>

### Turning one LED on and off

First, we'll focus on the red LED. For the red pin you broadcast `pin26on`, this makes pin 26 output power to the red LED, turning it on. To then turn the red pin off we use `pin26off`. To do this will use a broadcast block (in the control tab) and add a new value and we name it `pin26on`. We will need to repeat this for each new function we need to create.

Broadcast function for red LED

<img src="Images/RedBroadcast.gif" width="300px" />

Now lets try and turn the other two coloured LEDs on and off.

#### GPIO Pin key for LEDs

To help, here is a table with all of the lights with matching pin numbers.

| Light | Pin   |
| :---- | :---- |
| Red   | 26    |
| Amber | 24    |
| Green | 22    |

To light up the different LEDs we will repeat the broadcast method another four times, two to turn on the LEDs and two to turn off the LEDs.

The other two LEDs work the same way as the red LED's broadcast value, just with different pin numbers. Go ahead and make the other two broadcast functions for the amber and green LEDs

## Making the LEDs Loop

So now that we can turn the LEDs on and off, let's try to make them run by themselves. So to do this we are going to use a `repeat` block (located in the control tab). This allows us to repeat our code a set amount of times.

<img src="Images/RepeatBlock.png" width="120px">

<div class="page-break"></div>

We will also need to use the `wait` function (located in the control tab). The block lets you be able to pause the running code for a set amount of time in seconds.

<img src="Images/WaitBlock.png" width="120px">

Next when the green flag is clicked, we will make the LEDs flash on and off ten times. The LEDs must pause when they turn on and pause again when they turn off.

So lets focus on the red LED first...

To tell the LED to turn on, we again use `pin26on` as mentioned in the last section. Then we will make it wait for five seconds before turning it off and waiting for another five seconds. This entire section will then loop ten times. This is then what we get.

<img src="Images/RedLoop.gif" width="150px" />

## Making the Pi-Stop into a traffic light

What can we do with the Pi-Stop now? Why not make it act like a real traffic light?

Now that we know the basics, can we get the Pi Stop to work like a traffic light?

**TIP** : You can also make it loop forever by using a `forever loop`.

Now when you click on the green flag, your code should run and make the Pi-Stop light up like a traffic light! **Make sure your previous code is deleted, or it may causes some problems with the new code!**

#### What now?
- Why not try and make a traffic light sprite on Scratch that acts the same way as the Pi-Stop?
- Code different ways to turn Pi-Stop on and off? (eg. touch, PIR sensor)
- Make a game with a car that the user controls and has to stop when the Pi-Stop is red?
