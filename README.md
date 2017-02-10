micropython-freebsd
=========

Here is a collection of tools to make using micropython on a ESP8266 device connected to a USB port easier.

Its possible to flash firmware, transfer files via USB, configure wifi, or access the REPL via the USB serial manually, this just automates and wraps and verifies configurations and other good stuff.

./flash is a shell script that installs MicroPython firmware while very carefully troubleshooting and explaining how to fix the problems found.  Flash tries to install the highest numbered micropython firmware, if it gets confused just make sure theres only one firmware in the directory.

./ampy is a shell script wrapper generated every time flash is run, that transfers files over the CLI serial port.  If you interface settings for flash work, ampy should work.
See the comments in the generated ampy file about disabling debug messages in boot.py
This is quite a handy script for uploading a new boot.py file, which could connect to a wifi
and enable the WebREPL interface.  For a help page try ampy --help
Typically you would develop code in a loop of using ./ampy --no-output run somefile.py until it works, at which point you would do a final upload to the board in the form of ./ampy put somefile.py /main.py and then the /main.py file will auto run on boot.

minirc.esp8266 is another file generated every time flash runs, if you follow the instructions provided by flash and symlink it correctly, you can access the serial port CLI REPL by simply running "minicom esp8266" and all the connection details are taken care of for you.


