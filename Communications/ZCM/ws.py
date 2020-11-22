# Untested

from zcm import ZCM
from pto import pto_t
from otp import otp_t

def handler(channel, msg):
    print "Received message on channel: " + channel
    assert msg.timestamp == 10

zcm = ZCM("udpm://10.0.0.4:7777?ttl=64")

if not zcm.good():
    print "Unable to initialize zcm"
    exit()

# declare a new msg and populate it
msg = pto_t()
msg.timestamp = 10

# set up a subscription on channel "TEST"
subs = zcm.subscribe("TEST", otp_t(), handler)

# publish a message
zcm.publish("TEST", msg)