<template>
  <g class="display-screen">
    <rect
      :x="x"
      :y="y"
      :width="width"
      :height="height"
      class="screen-border"
    />
    <canvas
      ref="canvas"
      :width="width"
      :height="height"
      :style="{ transform: `translate(${x}px, ${y}px)` }"
    />
  </g>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'

const props = defineProps<{
  x: number
  y: number
  width: number
  height: number
  pixels: number[]
}>()

const canvas = ref<HTMLCanvasElement | null>(null)

const updateDisplay = () => {
  if (!canvas.value) return
  const ctx = canvas.value.getContext('2d')
  if (!ctx) return

  // 更新显示内容
  const imageData = ctx.createImageData(props.width, props.height)
  props.pixels.forEach((pixel, i) => {
    imageData.data[i * 4] = pixel     // R
    imageData.data[i * 4 + 1] = pixel // G
    imageData.data[i * 4 + 2] = pixel // B
    imageData.data[i * 4 + 3] = 255   // A
  })
  ctx.putImageData(imageData, 0, 0)
}

watch(() => props.pixels, updateDisplay)

onMounted(updateDisplay)
</script> 