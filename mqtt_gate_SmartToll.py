#importing the paho mqtt library
#You can install it using sudo pip install paho-mqtt
#For more information watch https://www.youtube.com/watch?v=Pb3FLznsdwI
import paho.mqtt.client as mqtt

#Get the GPIO pins
import RPi.GPIO as GPIO
import time

#Get json library
import json


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Set the trigger and echo pins
TRIG = 23
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)


#This are the station information, for different stations you can change the info below
my_station="A"
my_gate="3"


def distance():
	"""This function calculates the distance using ultrasonic sensor and returns data in cm."""
	print "Triggered Ultrasonic"

	GPIO.output(TRIG, False)

	time.sleep(0.5)

	GPIO.output(TRIG, True)

	time.sleep(0.00001)

	GPIO.output(TRIG, False)

	pulse_start=time.time()
	pulse_end=time.time()
	while GPIO.input(ECHO)==0:

	  	pulse_start = time.time()

	while GPIO.input(ECHO)==1:

  		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	return (( pulse_duration * 34300) / 2)





# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("smartToll")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    	print(msg.topic+" "+str(msg.payload))
    	data=json.loads(msg.payload)
	#We get the data transmitted over the channel
    	cur_station=data["station"]
	cur_gate=data["gate"]
	#Match if the request is for the current station
	if((cur_station==my_station) and (cur_gate==my_gate)):
		print ("\n Gate Open")
		while True:
            		dist = distance()
            		print ("\nMeasured Distance = %.1f cm" % dist)
            		time.sleep(1)
			#Check is someone passed through the gates
			if(dist<10):
				print ("Gate closed")
				break


# Create an MQTT client and attach our routines to it.
# Use your authentication details for MQTT
client = mqtt.Client()


#client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message

#client.connect("test.mosquitto.org", 1883, 60)



# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions
client.loop_forever()
