<template>
  <g @click="$emit('toggle')" class="toggle-switch">
    <rect
      :x="x"
      :y="y"
      width="20"
      height="10"
      :class="['switch-body', { 'switch-on': status }]"
    />
    <circle
      :cx="x + (status ? 15 : 5)"
      :cy="y + 5"
      r="5"
      class="switch-knob"
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
  (e: 'toggle'): void
}>()
</script>

<style scoped>
.switch-body {
  fill: #ccc;
  stroke: #999;
  stroke-width: 1;
  cursor: pointer;
  transition: fill 0.2s;
}

.switch-on {
  fill: #4caf50;
}

.switch-knob {
  fill: #fff;
  stroke: #999;
  stroke-width: 1;
  transition: cx 0.2s;
}
</style> 