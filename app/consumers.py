
from channels.consumer import SyncConsumer,AsyncConsumer,StopConsumer

class EchoConsumer(SyncConsumer):

    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        self.send({
            "type": "websocket.send",
            "text": event["text"],
        })




class MySocket(SyncConsumer):
    def websocket_connect(self,event):
        self.send({
            'type':'websocket.accept'

        })

#final 


class SajalSocket(SyncConsumer):

    def websocket_connect(self, event):
        print("Websocket is start Connecting ----")
        self.send({
            "type": "websocket.accept",
        })




    def websocket_receive(self, event):
        print("Message Received from Clinet -----------")
        print(event['text'])
        self.send({
            "type": "websocket.send",
            "text"  : "Message Send BY Client"
        })

    def websocket_disconnect(self,event):
        print("Band Ho gaya")
        raise StopConsumer()






import  asyncio 
import json
class Asynconnect(AsyncConsumer):

    async def websocket_connect(self, event):
        print("Websocket is start Connecting ----", event)
        await self.send({
            "type": "websocket.accept",
        })

    '''
    simple data 
    
    async def websocket_receive(self, event):
        print("Message Received from Clinet -----------", event)
        print(event['text'])
        for i in range(1000000000000):
            await self.send({
                "type": "websocket.send",
                "text"  : str(i)
            })

            await asyncio.sleep(3)'''



   #send dic 
    async def websocket_receive(self, event):
        print("Message Received from Clinet -----------", event)
        print(event['text'])
        for i in range(1000000000000):
            await self.send({
                "type": "websocket.send",
                "text"  : json.dumps({'count': i })       #send dict values                             #str(i)
            })

            await asyncio.sleep(3)




    async def websocket_disconnect(self,event):
        print("Band Ho gaya")
        raise StopConsumer()




