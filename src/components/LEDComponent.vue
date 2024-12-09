<template>
  <g @click="$emit('click')" class="led-component">
    <circle
      :cx="x"
      :cy="y"
      r="8"
      :class="['led', { 'led-on': status }]"
    />
  </g>
</template>

<script setup lang="ts">
defineProps<{
  x: number
  y: number
  status: boolean
}>()

defineEmits<{
  (e: 'click'): void
}>()
</script>

<style scoped>
.led {
  fill: #444;
  stroke: #333;
  stroke-width: 1;
  cursor: pointer;
  transition: fill 0.2s;
}

.led-on {
  fill: #f00;
  filter: drop-shadow(0 0 5px #f00);
}
</style> 