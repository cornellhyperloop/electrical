### Communications ###

To maintain a highly efficient embedded system capable of sending real-time pod state and sensor information, an appropriately powerful communications protocol was needed.  The requirements were that the protocol be designed for low-latency, high-bandwidth applications, support the Ubuntu platform, and provide tools for logging.  The Zero Communications and Marshalling (ZCM) protocol demonstrated all these qualities along with a transport-agnostic messaging system, which allowed for flexibility in pod design.
The drawback of using ZCM is that it does not support the Windows or OSX operating systems unless a Windows user utilizes the Windows Subsystem for Linux.  Our team decided uniformity across the system was worth this encumbrance.
