### SETTING UP ZCM ON WINDOWS

It appears that ZCM can be run under the Windows Subsystem for Linux (WSL), and the instructions under this section assume you are using Ubuntu on the WSL.  There are currently bugs with using ZCM on a dual-booted Ubuntu operating system, which will have to be corrected by ZCM developers.\
The Zero Communication and Marshalling protocol can be found at [this](http://zerocm.github.io/zcm/index.html) link.  Click the “Download.zip” button on the home screen, then unzip the protocol in your desired directory.  Run these commands, and if they don’t work see NOTES.
```
./waf configure --use-all --python=python3
./waf build
./waf install
```
---
### NOTES:
-	Don’t forget to restart Ubuntu after changing the ~/.bashrc

-	You may need to install dependencies.  In the base folder of the ZCM, run this command:\
`./scripts/install-deps.sh`\
In the output of this bash script there may be a red highlighted text area saying “You must add the following to your ~/.bashrc:”   Copy what appears on the next line of output and do so.

-	If you receive the error about your JAVA_HOME variable not being set, insert this code into your ~/.bashrc:\
`JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export JAVA_HOME`

-	If you get the following error:\
`: error while loading shared libraries: libzcm.so: cannot open shared object file: No such file or directory`\
then add this to your ~/.bashrc:\
`export LD_LIBRARY_PATH=/usr/lib:/user/local/lib`

-	If you wish to run `zcm-spy --zcm-url ipc` and nothing views:\
Add this to your ~/.bashrc:\
`export DISPLAY=:0`\
Now, download [XMing](https://sourceforge.net/projects/xming/), install with default settings, and open it.  Make sure you’ve restarted your terminal before running `zcm-spy` again.

For those developing with ZeroCM, following [this](http://zerocm.github.io/zcm/docs/tutorial.html) tutorial will introduce you to the fundamentals.
