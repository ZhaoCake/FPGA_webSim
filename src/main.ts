import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'

// 创建 Pinia 实例
const pinia = createPinia()

// 创建 Vue 应用实例
const app = createApp(App)

// 使用 Pinia
app.use(pinia)

// 挂载应用
app.mount('#app')
