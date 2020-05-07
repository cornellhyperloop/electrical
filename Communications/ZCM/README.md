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






