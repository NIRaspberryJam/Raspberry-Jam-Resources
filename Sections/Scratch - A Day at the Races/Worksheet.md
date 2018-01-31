# A Day at the Races

<img src="images\jamjan2.png" align="centre"/>

## What will we be doing in this worksheet?

In this activity you will be learning to code with Scratch! To demonstrate this, you will be coding a car to round a racetrack, and you will be coding the car to slow down if it goes off the track.

<br/>
<img src="images\Pi-Stop.png" width="30px" align="left"/>
<br/> <br/>

**A Pi-Stop is necessary for this activity and doing the "Getting started with the Pi-Stop" activity is recommended but not necessary.**

<div class="page-break"></div>

## Attaching the Pi-stop

Firstly ensure that your Pi is **powered off** and unplugged, this is very important. Make sure when attaching the Pi-Stop that the LEDs are **facing away** from your Pi. The diagram above shows the pins that you attach the Pi-Stop to, and which direction it should be facing.

<img src="images\RaspberryPiAttach.png" width="250px‰"/>

<img src="images\Tip.png" style="padding: 2mm 2mm" />

After you have attached the Pi-Stop the LEDs should light up dimly.

## Opening scratch

<img src="images\ScratchGPIO7.png" width="35%" align="right" />

Go to the Pi's desktop and open `ScratchGPIO7`, if it isn't there, try and click the ``“Install ScratchGPIO7”`` icon. After a moment `ScratchGPIO7` should appear on the desktop. When you open Scratch GPIO, a pop-up window should say ``“Remote sensor connections enabled”``. Open a new project, this will be where all our code goes to make our mini-game.

<div class="page-break"></div>

## Creating the race track

To start, we need to make our race track and car, and to make the background we need to go into `Backgrounds`, which you can find by clicking on the stage icon at the left side below the stage with the cat in it. Then at the top there will be three tabs, and open the `Background` tab as shown in picture 1. Then press `Edit` and make your track. Be sure to add a starting line!

We also need a sprite that can be used to race, like a car. First double click on the cat in the stage area so that it opens up the sprite menu then delete the default cat. Go to `‘Pick a sprite’` and choose a car from the ready to pick sprites in the transportation folder like in picture 2. Double click on it to select it and we can start to create our race.

<img src="images\2.png" width="45%" align="right" style="padding-top: 2mm;"/>
<img src="images\1.png" width="45%" align="left" style="padding-top: 2mm"/>

<a style="padding-top:3mm" />

## Moving the Car

We need to decide on a good starting point for our race, and make sure that when we start the race, our car is sitting. First we have to select the `when flag is clicked` block and drag it into the script area to start our program. This block is in the control section.

<img src="images\1.5.png" width="160mm" />

Then select the `go to x: y:` block in the motion section. This moves our car to whatever location we want when the flag is pressed.

<img src="images\3.png" />

<img src="images\4.png" width="30%" align="right" />

To find the x and y values, move your mouse to the starting line and the values at the **bottom right corner** of the scene (as indicated by the diagram) are your x and y values.

<div class="page-break"></div>

We also need to set the direction in which we want the car to go. To do this we select the `Point in direction` block and set it so that your car is facing in the correct direction.

<img src="images\5.png" />

Now that we have our car at the starting line we need to get it to move. We need to create a `forever loop` in the control tab, so that it repeats the instructions that we put in it… forever.

<img src="images\6.png" />

We then need 4 `if/then` blocks that are going to be put into the forever loop. An if/then block is a block that checks if a condition is met, and then if it has been met it will run the code that is put under it. If not, then it will skip the following code that is put under it and move onto the next block that isn’t part of the if/then block.

<img src="images\7.png" />

For this worksheet we will be checking if a certain key has been pressed. We can do this by using the blue `key _ pressed?` diamond block which is a condition block. We will put this block into the diamond slot in the if statement and set the key to the up arrow. Repeat this for the other three arrow keys. Down, left and right. The code inside the if block will either be a `move _ steps` block or a `turn _ degrees` block, both of which can be found in the motion tab. We will use the `move _ steps` in the up and down arrows for moving forwards and backwards. The left and right arrows will need to turn the car, we will use the `turn _ degrees block` for this Set each block so that it moves in sets of 5 or turns 5 degrees...

<img src="images\Bunchofifs.png" width="200mm" align="right" />

 _**Watch out!**_
*There are two different `turn _ degrees` blocks, one that turns left and one that turns right. Make sure that you use the correct one with the matching key.*

When up is pressed, it should move your sprite 5 steps forward, right should move your sprite 5 degrees to the right, and left should move your sprite 5 steps to the left.

<div class="page-break"></div>

## Ready, Set, Go!

Now that we have a track and a car that moves, we can now make it a race. To make a race we need traffic lights to tell us when to start. You can slot this into your code, right under the `go to x: y:` block. Separate the rest of your code and put it to one side, you will need to reattach it later.

<img src="images\9.png" align="right" />

Start with a `wait _ second` block and put in a 1, so that it waits 1 second before your forever loop starts. Then select a broadcast block and enter `‘pin26on’`. This will turn on the red LED on the Pi-Stop. We then want it to wait another second before turning off. To turn the LED off again, use another `broadcast block` and set it to `‘pin26off’`.

To change the colour we need another couple `broadcasts`. The LEDs are assigned to different pins, and this table shows which pin matches which LED. So, to turn on and off the different LED, just change the pin number in the broadcast block to the pin you want to turn on or off.

|Light |Pin |
|------|----|
|Red   |26  |
|Amber |24  |
|Green |22  |


Now just connect all of the code back together!

## Changing the speed

Now that we have gotten our car to move, we can make it slow down when it touches the grass. First, we'll make a variable by going to the variables tab and clicking on "Make a variable". We'll call it `speed`. Then we'll change the `move 5 steps` block to `move speed block` by using the new orange speed block that we created by making the variable.

<img src="images\10.png" />

<div class="page-break"></div>

Now that we have made and set the variable, we will now change the speed variable based on what colour the car is touching. To do this drag an `if/then` block inside of the forever loop. Go into sensing and drag the `touching colour` block into the diamond of the if/then block that you just created.

<img src="images\11.png" style="padding-bottom:2mm" />

Once you have done that, click on the square and then click on the grass, the square should turn green.

Now inside this if/then block, set the variable speed to 3. This is done by going into variables, dragging the `set speed to` block into the if/then block and then changing the number to 3. Drag another if/then block into the forever loop.

<img src="images\CanYou.png" />

The car now slows down when it touches the grass and speed back up again when you go back onto the road!

## Challenges

1. Use a timer to figure out your lap time and make it display at the end!
2. Why not have a race with your friends? Create another sprite and then code up 3 buttons like W, A and D as your controls.
3. Make more race tracks or try other Jammers' race tracks and get your fastest time!
