# Untested

from zcm import ZCM
from pto import pto_t
from otp import otp_t
import threading


class PubThread(threading.Thread):

   def run(self):
      zcm.publish("TEST", msg)


class SubThread(threading.Thread):

   def run(self):
      zcm.handle()


def handler(channel, msg):
    print "Received message on channel: " + channel
    assert msg.pod == "Cornell"


# create UDP zcm
zcm = ZCM("udpm://10.0.0.4:7777?ttl=64")

if not zcm.good():
    print "Unable to initialize zcm"
    exit()

# declare a new msg and populate it
msg = pto_t()
msg.state = 0

# set up a subscription on channel "TEST"
subs = zcm.subscribe("TEST", otp_t(), handler)

# create pub and sub threads
sub = subThread()
pub = pubThread()

# start pub and sub threads
sub.start()
pub.start()

zcm.unsubscribe()
