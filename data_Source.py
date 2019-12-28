
# import serial
import time
import string
import pynmea2
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.exceptions import PubNubException

pnChannel = "raspi-tracker";

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-a4e55bfc-297b-11ea-a5fd-f6d34a0dd71d"
pnconfig.publish_key = "pub-c-88519531-5c86-40ba-a87e-87d67fc1f056"
pnconfig.ssl = False
 
pubnub = PubNub(pnconfig)
pubnub.subscribe().channels(pnChannel).execute()
i =0
while True:
    # port="/dev/ttyAMA0"
    # ser=serial.Serial(port, baudrate=9600, timeout=0.5)
    # dataout = pynmea2.NMEAStreamReader()
    # newdata=ser.readline()

    # if newdata[0:6] == "$GPRMC":
    #     newmsg=pynmea2.parse(newdata)
    #     lat=newmsg.latitude
    #     lng=newmsg.longitude

    lat=[19.134064,19.133969 ,19.133941 ,19.133893 ,19.133647, 19.132987] 
    lng=[72.910860,72.911104,72.911190,72.911300,72.911878,72.913835 ]  
    try:
        envelope = pubnub.publish().channel(pnChannel).message({
        'lat':lat[i],
        'lng':lng[i]
        }).sync()
        print("publish timetoken: %d" % envelope.result.timetoken)
    except PubNubException as e:
        handle_exception(e)
    i = (i+1)%6
    time.sleep(1)


             
   