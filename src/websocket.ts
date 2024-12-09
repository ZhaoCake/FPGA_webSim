import { io, Socket } from 'socket.io-client'

const socket: Socket = io('http://your-backend-url', {
  transports: ['websocket'],
  reconnection: true,
  reconnectionAttempts: 5,
  reconnectionDelay: 1000
})

socket.on('connect', () => {
  console.log('Connected to WebSocket server')
})

socket.on('disconnect', () => {
  console.log('Disconnected from WebSocket server')
})

export default socket 