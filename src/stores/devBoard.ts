import { defineStore } from 'pinia'

export const useDevBoardStore = defineStore('devBoard', {
  state: () => ({
    leds: Array(8).fill(false),
    switches: Array(8).fill(false),
    sevenSegment: {
      a: false, b: false, c: false,
      d: false, e: false, f: false, g: false
    },
    displayBuffer: new Array(400 * 300).fill(0)
  }),
  
  actions: {
    updateLED(index: number, status: boolean) {
      this.leds[index] = status
    },
    
    updateSwitch(index: number, status: boolean) {
      this.switches[index] = status
    },
    
    updateDisplay(buffer: number[]) {
      this.displayBuffer = [...buffer]
    }
  }
}) 