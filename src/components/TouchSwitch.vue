<template>
  <g @click="$emit('press')" class="touch-switch">
    <circle
      :cx="x"
      :cy="y"
      r="10"
      class="switch-knob"
    />
  </g>
</template>

<script setup lang="ts">
defineProps<{
  x: number
  y: number
}>()

defineEmits<{
  (e: 'press'): void
}>()
</script>

<style scoped>
.switch-knob {
  fill: #ffeb3b;
  stroke: #fbc02d;
  stroke-width: 1;
  cursor: pointer;
  transition: fill 0.2s;
}
</style> 