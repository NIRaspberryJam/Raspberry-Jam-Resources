<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css">
   
# Micro:bit Nightlight
In this activity, you will create an automatic Micro:bit powered multicoloured nightlight!  

![](images/header.jpg)

### What you need   

![](images/needed-parts.png)

<div class="page-break"></div>

## Wiring
Once you have all your parts, we can start wiring up.  
1. Get your Neopixel RGB LED and split out the legs a bit. Careful not to bend them though to far in case they break   
2. Attach your crocodile clips like in the below diagram.    

<img src="images/wiring-diagram-1.png" width="300em"> 

3. Attach tape around each of the crocodile clip connectors where they attach to the LED legs. This stops the legs/crocodile clips by mistake touching each other.
<div class="page-break"></div>

## Code setup
The LED used in this project is no ordinary RGB (Red Green Blue) LED! Instead, it is what is called a Neopixel. A Neopixel is a special RGB LED with a built in chip, allowing you to send an exact colour to it. You can even chain more that one up together and control each of them individually!   
To use Neopixels though, we will need to enable the special package in MakeCode.
   
1. To get started coding, open up https://makecode.microbit.org.
2. Once loaded, click on ```Advanced``` and ```Add Package``` like in the diagram below.     

<img src="images/add-neopixel-1.png" width="200em"> 

3. Click on neopixel to add the Neopixel package to your project.    

<img src="images/add-neopixel-2.png" width="300em"> 

4. You should now see the Neopixel package has been added.     

<div class="page-break"></div>
   
## Lets get coding!   
### Using a Neopixel   
1. To use a Neopixel, we need to first create a Neopixel connection that we can use later on when we want to control the Neopixel. To do this, grab a ```Set Item to 0``` block from ```Variables``` and a ```Neopixel at pin P0 with...``` block. Slot them together like below.   

<img src="images/neopixel-block-1.png"> 

2. To set the Neopixel to a colour, get an ```item show colour``` block and pick the colour you want from the dropdown. This block includes the ```item show``` block built in, which we will need later on.      

<img src="images/neopixel-block-2.png">   

3. Now download your program to the Micro:bit and try it out!   

<div class="alert alert-info">
  <h4 align="center">Now try</h4>
  <ol>
  <li>Try changing the colours, which is your favourite?</li>
  <li>Why not try giving the <code>show rainbow from</code> block a go instead of <code>show colour</code>?</li>
  <li>Instead of using the colour dropdown block, why not try using the <code>red green blue </code> block in the more section. What does changing the numbers do?</li>
  </ol>
</div>

### Triggering the Neopixel when it is dark   
The last coding part of the project is we need to trigger the Neopixel when it gets dark. To do this, we will use the built in light sensor block.   
1. Grab an ```If Else``` block from the Logic section and place the ```show colour``` block in the ```if``` section. Put these both in the ```forever``` block and add a ```pause (ms)``` block from basic, as well to the bottom.    

2. Also from ```Logic```, grab a comparison block (see the diagram below). Then from the ```Input``` section, grab a ```light level``` block and slot it into the left hand side of the comparison block. Slot both of these into the ```if``` section from the section above.  

<img src="images/light-block-2.png"> 

3. Next, add what we want to happen when the room is light. Use an ```item clear``` block, along with an ```item show``` block to turn off the Neopixel.     

<img src="images/light-block-3.png"> 

4. And finally, we need to figure out what light level to trigger the nightlight to come on to. This will take some experimenting. Start at around 30 and adjust it to figure out what brightness the room is. If you need help with this, just ask.   

The final code should look something like this, remember you can use the ```red green blue``` block or perhaps a ```show rainbow from``` block instead of ```show colour``` if you want!   

<img src="images/light-block-4.png" width="380em">    
    
### Building your nightlight house   
The final step in the project is taking the flat paper house template, cutting it out and sticking it together.
1. Start by cutting only along the dotted line. For the micro:bit cutout, ask a volunteer to use a craft knife for that bit.   
2. Fold along the grey lines with your design facing outwards, then add glue to the following orange marked tabs and stick the house together.  

<img src="images/template-glue.png" width="320em"> 
   
3. Finally add your Micro:bit into its gap with the battery pack and LED inside and power it up. Remember you may need to tweak the light level trigger value in your code.  

*This activity and artwork is based off the fantastic BBC Live Lesson Bedside Lamp project, developed by Amy Mather for the BBC as part of their Hack Your Bedroom piece.*   
