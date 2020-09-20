from channels.generic.websocket import AsyncWebsocketConsumer
import json


class DashConsumer(AsyncWebsocketConsumer):

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
        await self.send(text_data=json.dumps({'v_id': v_id, 'v_lat': v_lat, 'v_lng': v_lng}))
