# Audio Reactive LED Strip
Real-time LED strip music visualization using Python and the ESP8266 or Raspberry Pi. This is a fork from Scott Lawson to see how to setup the hardware and learn more about overall functionality go over to the [git page](https://github.com/scottlawsonbc/audio-reactive-led-strip). This version will only focus on the RPI and adding more functionality.

# Installation

For majority of installation go over to the original git page. For installing the button the default pin is 17 which is physical pin 11. The button needs to be tied to ground and the pin, that's all. 

Start the program with 

`Sudo python run.py visualization.py`



To make the program run on startup 

`Sudo nano /etc/rc.local` 

Add these lines

`cd /home/pi`

`Sudo python run.py visualization.py`  



or to check for remote updates

`Sudo python update.py`

# Changes Made

- Added support for button to change visualization modes GPIO pin in config. Needs to be tied low to activate.
- The audio buffer overflows sometimes on the pi, not sure why yet but temporary solution is to kill the program when it does.
- Added run script that continually starts program if it stops running. This is used for audio buffer issue and any other random errors. This will allow you to run headless without having to restart the pi when it crashes
- Mode added that will cycle though the visualization modes every so many seconds
- Added remote update ability. Set the url of the zip and url of version file to automatically download and install a new version when available.

# TODO

- [ ] Ability to run multiple led strips with different visualizations
- [ ] Break up scripts and multithread them. Currently only runs on 1 core at about 75% usage on a RPI 3 B.
- [ ] Solve audio buffer issues
- [ ] Audio input via GPIO and ADC chip
- [ ] New GUI made for small touch screen. or buttons and oled setup
- [ ] MORE MODES
- [ ] Remote nodes running off ESP8266, using rpi as AP
- [ ] Custom board using RPI compute module (We'll see)

# License
This project was developed by Scott Lawson and modified by Jacob Lee and is released under the MIT License.
