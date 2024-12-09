<template>
  <div class="dev-board">
    <svg
      :width="boardWidth"
      :height="boardHeight"
      class="board-svg"
    >
      <!-- 开发板底板 -->
      <rect
        x="0"
        y="0"
        :width="boardWidth"
        :height="boardHeight"
        class="board-base"
      />
      
      <!-- LED 灯 -->
      <LEDComponent
        v-for="(led, index) in leds"
        :key="led.id"
        :x="50 + index * 30"
        y="50"
        :status="led.status"
        @click="toggleLED(led.id)"
      />

      <!-- 切换开关 -->
      <ToggleSwitch
        v-for="(toggleSwitch, index) in switches"
        :key="toggleSwitch.id"
        :x="50 + index * 30"
        y="100"
        :status="toggleSwitch.status"
        @toggle="toggleSwitchState(toggleSwitch.id)"
      />

      <!-- 触摸开关 -->
      <TouchSwitch
        v-for="(touchSwitch, index) in touchSwitches"
        :key="touchSwitch.id"
        :x="touchSwitch.x"
        :y="touchSwitch.y"
        @press="pressTouchSwitch(touchSwitch.id)"
      />

      <!-- 七段数码管 -->
      <g transform="translate(50, 150)">
        <SevenSegment
          v-for="(segment, index) in sevenSegments"
          :key="index"
          :x="index * 60"
          :y="0"
          :segments="segment"
        />
      </g>

      <!-- 显示屏 -->
      <DisplayScreen
        x="50"
        y="250"
        :width="400"
        :height="300"
        :pixels="displayData"
      />
    </svg>
  </div>
</template>

<script setup lang="ts">
import { reactive, onMounted, onUnmounted } from 'vue'
import socket from '../websocket'
import LEDComponent from './LEDComponent.vue'
import ToggleSwitch from './ToggleSwitch.vue'
import TouchSwitch from './TouchSwitch.vue'
import SevenSegment from './SevenSegment.vue'
import DisplayScreen from './DisplayScreen.vue'

// 开发板尺寸
const boardWidth = 800
const boardHeight = 600

// LED状态管理
const leds = reactive([
  { id: 1, status: false },
  { id: 2, status: false },
  { id: 3, status: false },
  { id: 4, status: false },
  { id: 5, status: false },
  { id: 6, status: false },
  { id: 7, status: false },
  { id: 8, status: false }
])

// 开关状态管理
const switches = reactive([
  { id: 1, status: false },
  { id: 2, status: false },
  { id: 3, status: false },
  { id: 4, status: false },
  { id: 5, status: false },
  { id: 6, status: false },
  { id: 7, status: false },
  { id: 8, status: false }
])

// 触摸开关位置
const touchSwitches = reactive([
  { id: 1, x: 200, y: 200 },
  { id: 2, x: 200, y: 240 },
  { id: 3, x: 160, y: 220 },
  { id: 4, x: 240, y: 220 },
  { id: 5, x: 200, y: 220 }
])

// 七段数码管状态
const sevenSegments = reactive([
  {
    a: true, b: true, c: true, d: true, e: true, f: true, g: false  // 显示数字 0
  },
  {
    a: false, b: true, c: true, d: false, e: false, f: false, g: false  // 显示数字 1
  },
  {
    a: false, b: false, c: false, d: false, e: false, f: false, g: false  // 全灭
  },
  {
    a: false, b: false, c: false, d: false, e: false, f: false, g: false  // 全灭
  },
  {
    a: false, b: false, c: false, d: false, e: false, f: false, g: false  // 全灭
  },
  {
    a: false, b: false, c: false, d: false, e: false, f: false, g: false  // 全灭
  },
  {
    a: false, b: false, c: false, d: false, e: false, f: false, g: false  // 全灭
  }
])

// 显示屏数据
const displayData = reactive(new Array(400 * 300).fill(0))

// WebSocket 事件处理
onMounted(() => {
  socket.on('updateLED', (data: { id: number, status: boolean }) => {
    const led = leds.find(l => l.id === data.id)
    if (led) led.status = data.status
  })

  socket.on('updateSwitch', (data: { id: number, status: boolean }) => {
    const sw = switches.find(s => s.id === data.id)
    if (sw) sw.status = data.status
  })

  socket.on('updateSevenSegment', (data: { index: number, value: number }) => {
    updateSevenSegment(data.index, data.value)
  })

  socket.on('updateDisplay', (data: { pixels: number[] }) => {
    displayData.splice(0, displayData.length, ...data.pixels)
  })
})

onUnmounted(() => {
  socket.off('updateLED')
  socket.off('updateSwitch')
  socket.off('updateSevenSegment')
  socket.off('updateDisplay')
})

// 发送状态到后端
const toggleLED = (id: number) => {
  const led = leds.find(l => l.id === id)
  if (led) {
    led.status = !led.status
    socket.emit('setLED', { id, status: led.status })
  }
}

const toggleSwitchState = (id: number) => {
  const sw = switches.find(s => s.id === id)
  if (sw) {
    sw.status = !sw.status
    socket.emit('setSwitch', { id, status: sw.status })
  }
}

const pressTouchSwitch = (id: number) => {
  console.log(`Touch switch ${id} pressed`)
  socket.emit('pressTouchSwitch', { id })
}

// 添加一个更新七段数码管显示的函数
const updateSevenSegment = (index: number, value: number) => {
  // 数字 0-9 的段显示配置
  const numberPatterns = [
    { a: true,  b: true,  c: true,  d: true,  e: true,  f: true,  g: false }, // 0
    { a: false, b: true,  c: true,  d: false, e: false, f: false, g: false }, // 1
    { a: true,  b: true,  c: false, d: true,  e: true,  f: false, g: true  }, // 2
    { a: true,  b: true,  c: true,  d: true,  e: false, f: false, g: true  }, // 3
    { a: false, b: true,  c: true,  d: false, e: false, f: true,  g: true  }, // 4
    { a: true,  b: false, c: true,  d: true,  e: false, f: true,  g: true  }, // 5
    { a: true,  b: false, c: true,  d: true,  e: true,  f: true,  g: true  }, // 6
    { a: true,  b: true,  c: true,  d: false, e: false, f: false, g: false }, // 7
    { a: true,  b: true,  c: true,  d: true,  e: true,  f: true,  g: true  }, // 8
    { a: true,  b: true,  c: true,  d: true,  e: false, f: true,  g: true  }  // 9
  ]
  
  if (index >= 0 && index < sevenSegments.length && value >= 0 && value <= 9) {
    sevenSegments[index] = { ...numberPatterns[value] }
  }
}

// 在第一个位置显示数字5
updateSevenSegment(0, 5)
</script>

<style scoped>
.dev-board {
  margin: 20px;
}

.board-base {
  fill: #4caf50; /* 绿色开发板 */
  stroke: #34495e;
  stroke-width: 2;
}
</style> 