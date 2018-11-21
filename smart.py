import africastalking
import RPi.GPIO as GPIO
print "testing"
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
GPIO.setup(17,GPIO.OUT)
# works with both python 2 and 3
from __future__ import print_function

import africastalking

class SMS:
    def __init__(self):
        # Set your app credentials
        self.username = "brighton"
        self.api_key = "18696560f647f921b072950f4ef9e5c24a76e583ec26b6ceb4f2ef6d34403daa"
        # Initialize the SDK
        africastalking.initialize(self.username,self.api_key)
        # Get the SMS service
        self.sms = africastalking.SMS

    def send_sms_sync(self,message):
        # Set the numbers you want to send to in international format
        recipients = ["+254728683438","+254783285164"]
        # Set your message

        # And send the SMS
        try:
			# That’s it, hit send and we’ll take care of the rest
            response = self.sms.send(message, recipients)
            print (response)
        except Exception as e:
            print ('Encountered an error while sending: %s' % str(e))
    def smart(self):
        input_value = GPIO.input(21)
        while True:
            if input_value==1:
                GPIO.output(17,GPIO.HIGH)
                SMS().send_sms_sync('moisture is not enough, turning on pump')

            else:
                GPIO.output(17,GPIO.LOW)
                SMS().send_sms_sync('moisture is enough turning off pump')

if __name__ == '__main__':
    SMS().smart()