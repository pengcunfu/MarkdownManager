<template>
  <footer class="bg-gray-900 text-white">
    <div class="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <!-- 产品信息 -->
        <div class="col-span-1 md:col-span-2">
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-8 h-8 bg-primary-600 rounded-lg flex items-center justify-center">
              <span class="text-white font-bold text-lg">M</span>
            </div>
            <span class="text-xl font-bold">Markdown Manager</span>
          </div>
          <p class="text-gray-400 mb-4 max-w-md">
            强大的 Markdown 文档管理工具，支持实时预览、全文搜索、云端同步等功能。让你的文档管理更加高效便捷。
          </p>
          <div class="flex space-x-4">
            <a href="https://github.com/pengcunfu/MarkdownManager" target="_blank" class="text-gray-400 hover:text-white transition-colors">
              <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
              </svg>
            </a>
          </div>
        </div>
        
        <!-- 快速链接 -->
        <div>
          <h3 class="text-lg font-semibold mb-4">快速链接</h3>
          <ul class="space-y-2">
            <li><router-link to="/" class="text-gray-400 hover:text-white transition-colors">首页</router-link></li>
            <li><router-link to="/features" class="text-gray-400 hover:text-white transition-colors">功能特性</router-link></li>
            <li><router-link to="/download" class="text-gray-400 hover:text-white transition-colors">下载</router-link></li>
            <li><router-link to="/docs" class="text-gray-400 hover:text-white transition-colors">使用文档</router-link></li>
          </ul>
        </div>
        
        <!-- 支持 -->
        <div>
          <h3 class="text-lg font-semibold mb-4">支持</h3>
          <ul class="space-y-2">
            <li><a href="https://github.com/pengcunfu/MarkdownManager/issues" target="_blank" class="text-gray-400 hover:text-white transition-colors">问题反馈</a></li>
            <li><a href="https://github.com/pengcunfu/MarkdownManager/discussions" target="_blank" class="text-gray-400 hover:text-white transition-colors">社区讨论</a></li>
            <li><a href="https://github.com/pengcunfu/MarkdownManager/releases" target="_blank" class="text-gray-400 hover:text-white transition-colors">更新日志</a></li>
          </ul>
        </div>
      </div>
      
      <!-- 版权信息 -->
      <div class="mt-8 pt-8 border-t border-gray-800 text-center">
        <p class="text-gray-400">
          © {{ currentYear }} Huaqiwill. All rights reserved. | 
          <a href="https://github.com/pengcunfu/MarkdownManager" target="_blank" class="hover:text-white transition-colors">开源项目</a>
        </p>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer',
  computed: {
    currentYear() {
      return new Date().getFullYear()
    }
  }
}
</script>
