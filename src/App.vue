<template>
  <div id="app" class="min-h-screen bg-white">
    <!-- 导航栏 -->
    <Navbar />
    
    <!-- 主要内容 -->
    <main>
      <router-view />
    </main>
    
    <!-- 页脚 -->
    <Footer />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    Navbar,
    Footer
  }
}
</script>
