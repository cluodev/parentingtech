# Introduction
This project contains small programs that I use to manage my son's screentime such as on MacBook, smart phone, Windows PC, etc

# Applications

## Roblox Blocker

I have found ScreenTime on MacBook (>=os x.y.z ) can not detect the Roblox Desktop app hence can not control its use. Therefore I wrote a python program to change permissions applied to the Roblox.app so as to block the access. 

### How to 

_roblox_blocker.py_

- Download the roblox_blocker.py e.g. save the file to `/Users/your_username/parentingtech/`
- make change in the file accordingly

*Launch Agent Definition File*

- update the plist file `com.roblox.blocker.plist`
- copy the plist file to `~/Library/LaunchAgents`

*No password for sudoer*

- `sudo visudo`
- append the following line in the file `sudo`

yourusername ALL=(ALL) NOPASSWD: /bin/chmod -R 000 /Users/yourusername/dev/tools/*, /bin/chmod -R 755 /Users/yourusername/dev/tools/*

*Load and Unload*

launchctl load ~/Library/LaunchAgents/com.roblox.blocker.plist
launchctl unload ~/Library/LaunchAgents/com.roblox.blocker.plist

