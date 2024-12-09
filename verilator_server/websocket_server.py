import asyncio
import websockets
import json
from simulator_interface import SimulatorInterface  # C++ 接口封装

class FPGASimulatorServer:
    def __init__(self):
        self.simulator = SimulatorInterface()
        self.clients = set()
        
    async def register(self, websocket):
        self.clients.add(websocket)
        
    async def unregister(self, websocket):
        self.clients.remove(websocket)
        
    async def distribute(self, message):
        if self.clients:
            await asyncio.gather(
                *[client.send(json.dumps(message)) for client in self.clients]
            )
            
    async def handle_message(self, websocket, message):
        data = json.loads(message)
        cmd_type = data.get('type')
        
        if cmd_type == 'setLED':
            # 调用 C++ 模拟器接口
            self.simulator.set_led(data['id'], data['status'])
            # 广播更新
            await self.distribute({
                'type': 'updateLED',
                'id': data['id'],
                'status': data['status']
            })
            
        elif cmd_type == 'setSwitch':
            self.simulator.set_switch(data['id'], data['status'])
            await self.distribute({
                'type': 'updateSwitch',
                'id': data['id'],
                'status': data['status']
            })
            
    async def simulation_loop(self):
        while True:
            # 获取模拟器状态
            display_data = self.simulator.get_display_data()
            seven_seg_data = self.simulator.get_seven_segment_data()
            
            # 发送更新
            await self.distribute({
                'type': 'updateDisplay',
                'pixels': display_data
            })
            await self.distribute({
                'type': 'updateSevenSegment',
                'segments': seven_seg_data
            })
            
            await asyncio.sleep(0.016)  # ~60fps
            
    async def handler(self, websocket, path):
        await self.register(websocket)
        try:
            self.simulator.start()
            asyncio.create_task(self.simulation_loop())
            
            async for message in websocket:
                await self.handle_message(websocket, message)
        finally:
            await self.unregister(websocket)
            if not self.clients:
                self.simulator.stop()

server = FPGASimulatorServer()

async def main():
    async with websockets.serve(server.handler, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main()) 