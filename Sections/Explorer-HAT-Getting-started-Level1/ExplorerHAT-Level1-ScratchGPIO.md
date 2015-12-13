# Level 1 -  Explorer HAT Introduction - Scratch
The Explorer HAT from Pimoroni is an easy to use, general purpose addon board (HAT) for the Raspberry Pi.   
This activity includes an introduction to using its built in inputs (x8 capacitive touch inputs) and outputs (x4 coloured LEDs).

## What you will need
 - x1 Explorer Pro HAT (Hardware Attachment on Top).
 - x4 crocodile clips.
 - Some tinfoil or other conductive material (fruit, playdough etc).

### Attaching your Explorer HAT
If your Explorer HAT isn't already attached, nab a volunteer to give you a hand to attach it as it can be a fiddle.   
![](images/ExplorerAttached.jpg)    

### Opening up Scratch   
Now your explorer HAT is attached and ready to go, we need to fire up Scratch. On the Raspberry Pi there are a few versions of Scratch. It is very important we pick the correct one!
You should see 3 different versions
- Scratch   
- ScratchGPIO7   
- ScratchGPIO7Plus (We want this one)   

The difference between them is quite simple, Scratch is just bog standard Scratch, ScratchGPIO7 adds electronics while ScratchGPIO7Plus adds support for addon boards, like the Explorer HAT!   
**Note** - You may instead have ScratchGPIO7Dev and ScratchGPIO7PlusDev.

# Lets get coding!
### Code setup
Now we are ready to write some code in Scratch! The first bit though we must do at the start of every program (this is essential) is tell Scratch what the name of the addon board is, in this case ```ExplorerHAT```.   
1. Create a variable from the variables section, call it ```AddOn``` and make sure it is ```For all sprites```.
2. Using the ```set``` block, set the ```AddOn``` variable to ```ExplorerHAT```.
3. Add a ```when place key pressed``` block from the control section to the top and hit the space bar.       
![](images/Setup.gif) 
<div class="page-break"></div>
     
## LEDs
The Explorer HAT includes 4 coloured LEDs! We can play with these super easily.   
To send commands to the Explorer HAT, we use the Broadcast command. In this case, ```broadcast GreenOn```   
![](images/LEDs1.gif)   

### LED Challenges
1. Can you turn each LED on and off one after each other?
2. Can you create a random light show using the LEDs, so the LEDs come on in a different order each time?

## Inputs
The Explorer HAT also has 8 capacitive touch inputs. Capacitive touch is the same technology used in most touch screens.   
It allows you to simply touch the pads, instead of having to physically press in a button.  
The 8 capacitive touch inputs are split into 2 sections.   
- 1-4 are for pressing directly with your fingers.
- 5-8 are for attaching to other "stuff" using crocodile clips, for example fruit, playdough or tinfoil.   
  
![](images/explorerdiagram.png)    
Lets try using pad number 1. To use it, in Scratch we have 2 options. The simplest way is using what is called "Event Driven mode", basically it keeps an eye in the background to see if the button is pressed, and if it does it triggers an event, in the case of ScratchGPIO, it sends a broadcast. The cool bit is, you can be waiting for that broadcast and set off your own code when it is triggered!   
To do so, grab a ```When I receive``` block and set it to ```Touch1```. Make sure you have the ```set AddOn``` somewhere in your program or else ```Touch1``` may not be available!   
It is also important to add a ```broadcast TouchReset1``` after you have detected the touch press to reset it back to be used again.     
![](images/Touch1.gif)   
Remember, you can change the code in between the ```when I receive touch1``` and ```broadcast TouchReset1``` to anything you want!   
### Input Challenges  
1. Can you trigger an LED to come on when touch pad 2 is touched?   
2. Can you connect some tinfoil to the Explorer HAT to crocodile pad 5 and use it as a button?   

## Final Challenge   
So now you know how to use the inputs and outputs on the Explorer HATs, lets see if we can use them for a slightly bigger project.    
-  Can you build a game in Scratch where to move the character around, you use touch pad inputs 5-8 with tinfoil/playdough/fruit? The game could perhaps include a simple maze or another character you have to run away from or avoid.   

## What's next?
Now you have a basic understanding of using the built in inputs and outputs of the Explorer HAT, you are ready to move onto Level 2 Explorer HAT Scratch activities!
