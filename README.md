# flux

## Parts
For convenience, the majority of links are from Adafruit. Most parts are sold by DigiKey and various other sellers however.

- [Raspberry Pi 0 W](https://www.adafruit.com/product/3708)
- [Micro USB to barrel jack adapter](https://www.adafruit.com/product/2727)
- [NeoPixel LED strip](https://www.adafruit.com/product/2841)
- [Switchable power supply](https://www.adafruit.com/product/1448)
- [MicroSD Card](https://www.amazon.com/gp/product/B07WW1H346/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

## Tools
- Soldering tools
- 3D printer or a 3D printing service
- Laser cutter or laser cutting service

## Code
The code is hosted on my [Github](https://github.com/User-r00/flux) and can be setup using the next steps.

### Setup the Raspberry Pi
Image your Raspberry Pi 0 W using the [instructions from Raspberry Pi](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md).

### Connect the Pi to Wi-Fi
Setup Wi-Fi using the [instructions from Raspberry Pi](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md).

### Setup SSH
Setup SSH using the [instructions from Raspberry Pi](https://www.raspberrypi.org/documentation/remote-access/ssh/). Once configured, SSH into the Pi.

### Download the code to the Pi
Navigate to where you want the code to live and run.

`git clone https://github.com/User-r00/flux.git`

### Configure the script
In main.py, change spaceboyr00 to your TikTok username.

`USERNAME = 'spaceboyr00'`

### Set the script to run at boot.
Add the following code to /etc/rc.local at the end before exit 0.

`su - pi -c "/usr/bin/screen -dmS flux bash -c 'python3 /home/pi/main.py; exec bash'"`

## Enclosure
The enclosure is made of three 3D printed pieces; The main body, a front lid, and a stand to keep it all upright. The STLs are available here in the repo under the 3D Files folder. If you do not have a 3D printer, check your local hackerspace or public library. If these are not an option, there are a number of 3D printing services online as well.

## Diffusion Panel
The diffusion panel is a sheet of frosted acrylic that spreads out the light from the NeoPixel strip. I used a local laser service to cut a 3mm sheet of frosted white acrylic. I have included logo_laser.eps for you to use on a laser. If you do not have access to a laser, use the logo_print.jpg file and cut it out of acrylic by hand.

## Wire it up
See Fritzing/flux_fritzing.jpg for an overview. 5V and gnd from the Pi to the respective spots on the NeoPixel strip. Data from the NeoPixel DI pin to pin 26 on the Pi. The Micro USB to DC barrel adapter connects to the USB port on the Pi.

## Final Assembly
The Pi gets screwed into the two bosses on the inside of the enclosure body. The NeoPixel strip gets mounted around the inside lip of the lid. The acrylic gets attached from the back of the lid. Finally, the barrel adapter seats into the hole on the enclosure.

Set the power supply to 3V and plug it into both the wall and the lamp. Post TikTok, gain followers, and bask in your lamp’s glow.
