from channels.generic.websocket import AsyncWebsocketConsumer
from Users.views import UserName
import json
import time
from twilio.rest import Client
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

class DashConsumer(AsyncWebsocketConsumer):
    start_time=time.time()
    a=1

    async def connect(self):
        self.groupname = 'dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name,
        )
        pass

    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        id = datapoint['id']
        lat = datapoint['lat']
        lng = datapoint['lng']

        await self.channel_layer.group_send(
            self.groupname,
            {
                'type': 'deprocessing',
                'id': id,
                'lat': lat,
                'lng': lng,
            }
        )
        print('>>>>', text_data)
        pass

    async def deprocessing(self, event):
        v_id = event['id']
        v_lat = event['lat']
        v_lng = event['lng']

        b=DashConsumer.a+1



        DashConsumer.a=b
        if DashConsumer.a >= 10:
            try:
                user=UserName.UserName
                print(user)
                print('send')
                account_sid = 'ACd5c22e88b4381dcdc0b13269da13013b'
                auth_token = '09d003112cb2f1f76542e9e5fbe818ff'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                        from_='+18155818564',
                        # body=' Dear '+ str(user) +' Your Longitude:'+str(v_lng)+' and latitude '+ str(v_lat),
                        body ='Dear '+ str(user)+', http://www.google.com/maps/place/'+str(v_lat)+','+str(v_lng),
                        to='+919970869905'
                )

                subject = 'Two wheeler Location'
                print(user,v_lng,v_lat)
                # message = ' Dear '+ user +' Your Longitude:'+v_lng+' and latitude '+ v_lat
                message ='Dear '+ str(user)+', http://www.google.com/maps/place/'+str(v_lat)+','+str(v_lng)
                
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user]
                send_mail( subject, message, email_from, recipient_list, fail_silently=False )
                print('email sent', user)

                DashConsumer.a=1

            except :
                pass


        await self.send(text_data=json.dumps({'v_id': v_id, 'v_lat': v_lat, 'v_lng': v_lng}))
