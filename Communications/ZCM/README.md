# Building

Make sure you have cloned the zcm github repository: [repo](https://github.com/ZeroCM/zcm) and use the following commands to build in the main zcm directory:

	./waf configure --use-all
	./waf build
	sudo ./waf install

If this doesn't work install dependencies using:

	./scripts/install-deps.sh

## Examples

To build examples:

	source ./examples/env
	./waf configure
	./waf build_examples

Running an example:
	./build/examples/examples/cpp/sub

Open up another shell:

	./build/examples/examples/cpp/pub

## Notes

Make sure JAVA_HOME is set (eg. export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/)

If you get the following error: 

	./publish: error while loading shared libraries: libzcm.so: cannot open shared object file: No such file or directory

Set the LD_LIBRARY_PATH:

	export LD_LIBRARY_PATH=/usr/lib:/usr/local/lib

To use the zcm-spy tool on WSL, install XMing for displays: [download](https://sourceforge.net/projects/xming/)

## Creating new packets
Create a subdirectory with the same name as your packet.

Create a .zcm file for your packet and define your packet type meeting in the format defined [here](https://zerocm.github.io/zcm/docs/tutorial.html).

Compile your packet: `zcm-gen -c <packet_name>.zcm`

Create a ZCM subdirectory and symlink it to the zcm subdirectory of your ZCM install's location.
`ln -s /path/to/zcm/zcm /path/to/packet/dir/zcm`


Write publish and subscribe scripts in c in a manner that suits your application. See otp's pub.c and sub.c  as examples.


Compile your files into executables `cc -o publish -I. publish.c msg_t.c -lzcm`

`./publish`


You can use the following tool to see the current broadcasted packets and ensure your publisher is functioning: `zcm-spy --zcm-url ipc` (assuming you chose ipc as the protocol in your publisher)


## Communication Protocols
ZCM offers the following options in regards to protocols usable in its transport layer:
Local System Kernel Communications (Intra-device communication)
- Inter-Thread
- IPC (Inter-Process)
- Non-Blocking Interthread

Inter-device Communication
- UDP Multicast
- Serial


What should we use?
- We need inter-device communication
- It would be nice to have the ability to transmit the same packet to multiple recipients


For these reasons, we should use UDP to transport our packets throughout the computers on the pod. Should be able to use an ethernet cable to connect the two devices and broadcast from one network to the other"




## SETTING UP ZCM ON WINDOWS

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






