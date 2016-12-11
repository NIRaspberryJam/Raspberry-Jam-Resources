# Hack the Dazzling Raspbertree

<img src="Images/header.png" width="950px" align="centre"/>

A simple yellow level difficulty activity using a strip of Neopixels and [David Whale's](https://twitter.com/whaleygeek) excellent [network.py](https://raw.githubusercontent.com/raspberrypilearning/networking-lessons/master/lesson-1/code/network.py) library to let kids hack a Raspbertree!    
    
You will need a strip of Neopixels, something to wrap them around (like a Christmas tree) and a Raspberry Pi to act as the server.   
1. Connect up your Neopixels to the server Raspberry Pi (using BCM pin 18).
2. Add ```blacklist snd_bcm2835``` into ```/etc/modprobe.d/snd-blacklist.conf``` and reboot the Pi.
3. Run the tree_server.py file in code directory.
4. Make sure the [network.py](https://raw.githubusercontent.com/raspberrypilearning/networking-lessons/master/lesson-1/code/network.py) file is on the client Raspberry Pi as a library (or in same directory as their scripts are in).   

### Activity documents
   
- [Activity PDF](Hack-the-Dazzling-Raspbertree.pdf?raw=true)   
- [Activity Markdown file](Hack-the-Dazzling-Raspbertree.md)    
- [Required library](https://raw.githubusercontent.com/raspberrypilearning/networking-lessons/master/lesson-1/code/network.py)   
- [Example server code](Code/tree_server.py)   
   
![](Images/tree.jpg)
