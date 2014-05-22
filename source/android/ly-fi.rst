LY-F1 Android Tablet
====================
I recently purchased this little beauty on Amazon, sold by www.tabtronics.co.uk
and branded as the "A10 M009S".  The specs are nothing stellar, but for the
price (£109) this is a great little device.

The specs as listed are:

Original LY-F1 A10 Android Tablet - The new, A10 processor offers 1.2GHz
frequency and a 400MHz dedicated graphics processor to provide seamless play
in, even the most intensive, 3D games or allows more apps to be run
concurrently without the inevitable cpu slowdown experienced in lesser tablets.

CPU : A10 1.2 GHz
Graphics Processor : Mali 400 MHz
Touchscreen : 5 point multi touch capacitive
resolution 800 x 480
Operating System : Android 2.3 GINGERBREAD
Memory : 512mb DDR II / 8gb NAND
Flash - upgradeable by Micro SD memory card (max 16GB) WiFi : 802.11 b/g/n
Connectivity : 1 x Micro SD slot, 1 x AC Jack, 1 x 3.5mm Earphone Jack, 1 x Mini USB, 1 x HDMI out
Battery : 4000 mAh 
Camera : 0.3mp Front facing
Android Market : YES
G Sensor : YES
3G : Requires HUAWEI E1750 Dongle available separately
Dimensions : 198 x 117 x 9.8mm
Weight : 365g

The specs say Gingerbread, but mine arrived pre-flashed with Android 4.0 ICS.

A few comments on my experiences with the device:

The ICS build I recieved was rooted by default; however it was not
pre-installed with the SuperUser or Busybox apps from the Play store. I don't
recommend installation of busybox from the Play store unless you know what you
are doing (more below) but I heavily recommend installing Superuser.

Superuser is a replacement for a system binary named 'su' (traditionally short
for substitute user, rather than superuser).  In the default install on the
LY-F1 tablet the su binary will allow any application to gain root access
without any confirmation from the user.  This has obvious security concerns.
The Superuser app replaces this binary and will only allow apps that you
approve to escalate their priviledges, and notify you every time an app gains
root. Once you have installed it you will need to go into the settings menu and
scroll down to the "su binary" line.  If you tap this you can then replace your
system su binary with the one that ships with Superuser.
