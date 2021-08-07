import RPi.GPIO as GPIO
import dht11
import time
import datetime
import paho.mqtt.client as mqtt

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

###### Edit variables to your environment #######
broker_address = "test.mosquitto.org"     #MQTT broker_address
Topic = "ondo/h-maruyama-jp"

# read data using pin 12
instance = dht11.DHT11(pin=18)

try:
	while True:
	    result = instance.read()
	    if result.is_valid():
	        print("Last valid input: " + str(datetime.datetime.now()))

	        print("Temperature: %-3.1f C" % result.temperature)
	        print("Humidity: %-3.1f %%" % result.humidity)

	        # publish MQTT
	        print("creating new instance")
	        client = mqtt.Client("pub2") #create new instance

	        print("connecting to broker: %s" % broker_address)
	        client.connect(broker_address) #connect to broker

	        Msg = "Temperature" + str(result.temperature) + "C" + "  Humidity" + str(result.humidity) + "%"
	        print("Publishing message: %s to topic: %s" % (Msg, Topic))
	        client.publish(Topic,Msg)
	    time.sleep(10)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
