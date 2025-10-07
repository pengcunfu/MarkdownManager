import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import './style.css'

// 导入页面组件
import Home from './pages/Home.vue'
import Features from './pages/Features.vue'
import Download from './pages/Download.vue'
import Docs from './pages/Docs.vue'

// 配置路由
const routes = [
  { path: '/', component: Home },
  { path: '/features', component: Features },
  { path: '/download', component: Download },
  { path: '/docs', component: Docs }
]

const router = createRouter({
  history: createWebHistory('/MarkdownManager/'),
  routes
})

const app = createApp(App)
app.use(router)
app.mount('#app')
