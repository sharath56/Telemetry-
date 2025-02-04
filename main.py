import serial
import time
import thingspeak
import pyrebase
from twilio.rest import Client
#import firebase
channel_id = "XXXXXXXXXXXXXXXXXXXXXXXX"
read_key ="XXXXXXXXXXXXXXXXXXXXXXXX"
ser = serial.Serial('COM6',115200)
channel = thingspeak.Channel(id=channel_id, api_key=read_key)
config = {
  "apiKey": "XXXXXXXXXXXXXXXXXXXXXXXX",
  "authDomain": "XXXXXXXXXXXXXXXXXXXXXXXX",
  "databaseURL": "XXXXXXXXXXXXXXXXXXXXXXXX",
  "storageBucket": "XXXXXXXXXXXXXXXXXXXXXXXX"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
account_sid = 'CXXXXXXXXXXXXXXXX' 
auth_token = 'XXXXXXXXXXXXXXXXXX'
client = Client(account_sid, auth_token) 
while 1:
     data= ser.readline().rstrip()
     print(" heart rate :"+ str(data))
     response = channel.update({'field1':data})
     data1={"heart_rate":str(data)}
     db.child("real time data").child("1-set").set(data1)
     message = client.messages.create( 
                              from_='whatsapp:+XXXXXXXXX',  
                              body=("heart_pluse of patient :"+str(data)),      
                              to='whatsapp:+91XXXXXXXXX' 
                          )                   
     print(message.sid)
