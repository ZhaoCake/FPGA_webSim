<template>
  <g class="seven-segment">
    <!-- 段 a -->
    <path
      :d="`M ${x + 5},${y} L${x + 35},${y} L${x + 30},${y + 5} L${x + 10},${y + 5} Z`"
      :class="['segment', { 'segment-on': segments.a }]"
    />
    <!-- 段 b -->
    <path
      :d="`M ${x + 35},${y + 2} L${x + 40},${y + 30} L${x + 35},${y + 35} L${x + 30},${y + 7} Z`"
      :class="['segment', { 'segment-on': segments.b }]"
    />
    <!-- 段 c -->
    <path
      :d="`M ${x + 35},${y + 37} L${x + 40},${y + 65} L${x + 35},${y + 70} L${x + 30},${y + 42} Z`"
      :class="['segment', { 'segment-on': segments.c }]"
    />
    <!-- 段 d -->
    <path
      :d="`M ${x + 5},${y + 70} L${x + 35},${y + 70} L${x + 30},${y + 65} L${x + 10},${y + 65} Z`"
      :class="['segment', { 'segment-on': segments.d }]"
    />
    <!-- 段 e -->
    <path
      :d="`M ${x},${y + 37} L${x + 5},${y + 65} L${x + 10},${y + 62} L${x + 5},${y + 42} Z`"
      :class="['segment', { 'segment-on': segments.e }]"
    />
    <!-- 段 f -->
    <path
      :d="`M ${x},${y + 2} L${x + 5},${y + 30} L${x + 10},${y + 27} L${x + 5},${y + 7} Z`"
      :class="['segment', { 'segment-on': segments.f }]"
    />
    <!-- 段 g -->
    <path
      :d="`M ${x + 5},${y + 35} L${x + 35},${y + 35} L${x + 30},${y + 30} L${x + 10},${y + 30} Z`"
      :class="['segment', { 'segment-on': segments.g }]"
    />
  </g>
</template>

<script setup lang="ts">
interface SegmentState {
  a: boolean
  b: boolean
  c: boolean
  d: boolean
  e: boolean
  f: boolean
  g: boolean
}

defineProps<{
  x: number
  y: number
  segments: SegmentState
}>()
</script>

<style scoped>
.segment {
  fill: #2c3e50;
  transition: fill 0.2s;
}

.segment-on {
  fill: #ff0000;
}
</style> 