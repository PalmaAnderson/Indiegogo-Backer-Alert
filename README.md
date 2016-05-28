# Indiegogo-Backer-Alert<br>

####Get notified about new backers and trigger external commands
<p>Works with **Python 3!**
<p>Just need to modify one variable to make this program work:
<p>"CAMPAIGN_ID=your id here"
<p>Or install **pySerial** if you want it to comunicate with **arduino**
<br>

####Files:
<p>**IndiegogoBackerAlertWindows.py** (Windows with beep)
<p>serialArduino/**IndiegogoBackerAlertLinuxSerial.py** (Linux with Serial support)
<p>serialArduino/**IndiegogoBackerAlertWindowsSerial.py** (Windows with Serial support)
<p>serialArduino/**serialArduino.ino** (sample arduino code)
<p>Coming soon: linux with beep
<br>

####How do I install and set this up?
<br>1 - download python
<br>2 - install/run pip to get pySerial module (IndiegogoBackerAlertWindows.py doesn't need this step)
<br>3 - beetween line 20~25 find **CAMPAIGN_ID=1757572** and replace with your onw ID (coming soon a tutorial for it)
<br>4 - RUN!
<br>

####About the Code:
we**UseCamelCase** and **no_undercore** for variables
<p>Will try as much possible keep it one .py file only needed to run occording to your system or needs <br>(+ .ino if you use arduino)
<p>No import other than **defaut python instalation** or pySerial
<p>**#** Lots of comments, understand whats happening and edit the code even if you dont understand python
<br>
<p>

| file                          | Function                                               |
|-------------------------------|--------------------------------------------------------|
| (Windows with beep)           | **IndiegogoBackerAlertWindows**.py                     |
| (Windows with beep)           | coming soon                                            |
| (Linux with Serial support)   | serialArduino/**IndiegogoBackerAlertLinuxSerial**.py   |
| (Windows with Serial support) | serialArduino/**IndiegogoBackerAlertWindowsSerial**.py |
| (sample **arduino** code)     | serialArduino/serialArduino.ino                        |
