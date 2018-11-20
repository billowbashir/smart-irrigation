import africastalking
import RPi.GPIO as GPIO
print "testing"
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
GPIO.setup(17,GPIO.OUT)


# class SMS:
#     def __init__(self):
# 		# Set your app credentials
# 	    self.username = "YOUR_USERNAME"
#         self.api_key = "YOUR_API_KEY"
# 		# Initialize the SDK
#         africastalking.initialize(self.username, self.api_key)
# 		# Get the SMS service
#         self.sms = africastalking.SMS

#     def send_sms_sync(self):
#         # Set the numbers you want to send to in international format
#         recipients = ["+254713YYYZZZ", "+254733YYYZZZ"]
#         # Set your message
#         message = "I'm a lumberjack and it's ok, I sleep all night and I work all day";
#         # And send the SMS
#         try:
# 			# That’s it, hit send and we’ll take care of the rest
#             response = self.sms.send(message, recipients)
#             print (response)
#         except Exception as e:
#             print ('Encountered an error while sending: %s' % str(e))
while True:
   input_value = GPIO.input(21)
   print input_value
    if input_value==1:
        GPIO.output(17,GPIO.HIGH)
        # low moisture,watering
    else:
        GPIO.output(17,GPIO.LOW)
        # enough moisture ,not watering






# if __name__ == '__main__':
#     SMS().send_sms_sync()       