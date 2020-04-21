# Communications
Communications protocols for passing information between the modules in the Hyperloop pod

## LCM (Lightweight Communications and Marshalling)
Set of libraries and tools for passing messages and marshalling data, in systems where high-bandwidth and low latency is essential.

### Benefits of LCM
* Simple C-like syntax that allows for sending packets of information
* Can be used with ZCM across Arduino serial lines as well as other embedded systems
* Little overhead and flexible with module types

### LCM Logging
* The LCM package also supports logging functionality that records LCM traffic through a network
* Can be used to perform diagnostics after flight runs

### Usage
* Relay information between Pilot Computer and Flight computer(Odroid C2) through LCM tunnel

### Supported Platforms
* Platforms
  * GNU/Linux
  * OS X
  * Windows
  * Any POSIX-1.2001 system (e.g., Cygwin, Solaris, BSD, etc.)
* Languages
  * C
  * C++
  * C#
  * Go
  * Java
  * Lua
  * MATLAB
  * Python

### Additional Packages
* libbot2
  * set of libraries, tools, and algorithms that are designed to facilitate robotics research
  * LCM utility programs including LCM tunnelling (lcm-utils)
  * Visualization of data with OpenGL and GTK2 (vis)
  * Process management tools for controlling many processes (procman)

### Links
* [LCM downloads](https://github.com/lcm-proj/lcm/releases)
* [Website and documentation](http://lcm-proj.github.io)
* [libbot2] (https://github.com/libbot2/libbot2)



## ZCM (Zero Communications and Marshalling)
Use to send information within Arduino serial lines. Mostly compatible with LCM

### Supported Platforms
* Platforms
  * GNU/Linux
  * Web browsers supporting the Websocket API
  * Any C89 capable embedded system
* Languages
  * C (89 and greater)
  * C++
  * Java
  * MATLAB (Using Java)
  * NodeJS and Client-side Javascript
  * Python
  * Julia (both v1.0.3 and v0.6.4)



### Links
* [ZCM website](http://zerocm.github.io/zcm/)



