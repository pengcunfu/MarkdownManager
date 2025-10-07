<template>
  <div class="py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Header -->
      <div class="text-center mb-16">
        <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">下载 Markdown Manager</h1>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          选择适合你操作系统的版本，开始高效的 Markdown 文档管理体验
        </p>
      </div>

      <!-- Version Info -->
      <div class="bg-primary-50 rounded-2xl p-8 mb-12 text-center">
        <div class="inline-flex items-center space-x-2 mb-4">
          <span class="bg-primary-600 text-white px-3 py-1 rounded-full text-sm font-semibold">最新版本</span>
          <span class="text-2xl font-bold text-gray-900">v1.0.0</span>
        </div>
        <p class="text-gray-600 mb-4">发布日期：2025年1月</p>
        <div class="flex flex-wrap justify-center gap-4 text-sm text-gray-600">
          <span class="flex items-center">
            <svg class="w-4 h-4 text-green-500 mr-1" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
            实时预览功能
          </span>
          <span class="flex items-center">
            <svg class="w-4 h-4 text-green-500 mr-1" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
            全文搜索优化
          </span>
          <span class="flex items-center">
            <svg class="w-4 h-4 text-green-500 mr-1" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
            云端同步支持
          </span>
        </div>
      </div>

      <!-- Download Options -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
        <!-- Windows -->
        <div class="bg-white rounded-2xl shadow-lg p-8 text-center hover:shadow-xl transition-shadow">
          <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-6">
            <svg class="w-8 h-8 text-blue-600" fill="currentColor" viewBox="0 0 24 24">
              <path d="M0 3.449L9.75 2.1v9.451H0m10.949-9.602L24 0v11.4H10.949M0 12.6h9.75v9.451L0 20.699M10.949 12.6H24V24l-13.051-1.351"/>
            </svg>
          </div>
          <h3 class="text-2xl font-bold text-gray-900 mb-4">Windows</h3>
          <p class="text-gray-600 mb-6">支持 Windows 10/11</p>
          <div class="space-y-3 mb-8">
            <div class="flex justify-between text-sm">
              <span class="text-gray-600">文件大小:</span>
              <span class="font-semibold">~50MB</span>
            </div>
            <div class="flex justify-between text-sm">
              <span class="text-gray-600">架构:</span>
              <span class="font-semibold">x64</span>
            </div>
          </div>
          <a 
            href="https://github.com/pengcunfu/MarkdownManager/releases/latest/download/MarkdownManager-Windows-x64.exe" 
            class="w-full bg-blue-600 hover:bg-blue-700 text-white py-3 px-6 rounded-lg font-semibold transition-colors inline-flex items-center justify-center"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            下载 .exe
          </a>
        </div>

        <!-- macOS -->
        <div class="bg-white rounded-2xl shadow-lg p-8 text-center hover:shadow-xl transition-shadow">
          <div class="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-6">
            <svg class="w-8 h-8 text-gray-600" fill="currentColor" viewBox="0 0 24 24">
              <path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/>
            </svg>
          </div>
          <h3 class="text-2xl font-bold text-gray-900 mb-4">macOS</h3>
          <p class="text-gray-600 mb-6">支持 macOS 11.0+</p>
          <div class="space-y-3 mb-8">
            <div class="flex justify-between text-sm">
              <span class="text-gray-600">文件大小:</span>
              <span class="font-semibold">~45MB</span>
            </div>
            <div class="flex justify-between text-sm">
              <span class="text-gray-600">架构:</span>
              <span class="font-semibold">Universal</span>
            </div>
          </div>
          <a 
            href="https://github.com/pengcunfu/MarkdownManager/releases/latest/download/MarkdownManager-macOS.dmg" 
            class="w-full bg-gray-600 hover:bg-gray-700 text-white py-3 px-6 rounded-lg font-semibold transition-colors inline-flex items-center justify-center"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            下载 .dmg
          </a>
        </div>

        <!-- Linux -->
        <div class="bg-white rounded-2xl shadow-lg p-8 text-center hover:shadow-xl transition-shadow">
          <div class="w-16 h-16 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-6">
            <svg class="w-8 h-8 text-orange-600" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12.504 0C5.678 0 .126 4.865.126 10.982c0 4.964 3.241 9.19 7.74 10.18-.113-.9-.21-2.28.044-3.26.232-.9 1.487-6.3 1.487-6.3s-.38-.76-.38-1.88c0-1.76 1.02-3.07 2.29-3.07 1.08 0 1.61.81 1.61 1.78 0 1.08-.69 2.7-1.04 4.2-.3 1.26.63 2.28 1.87 2.28 2.24 0 3.97-2.36 3.97-5.75 0-3.01-2.16-5.11-5.25-5.11-3.58 0-5.68 2.68-5.68 5.45 0 1.08.42 2.24.94 2.87.1.13.12.24.09.37-.1.4-.32 1.31-.37 1.49-.06.24-.2.29-.46.18-1.67-.78-2.71-3.22-2.71-5.18 0-4.23 3.07-8.11 8.86-8.11 4.65 0 8.27 3.31 8.27 7.74 0 4.62-2.91 8.33-6.96 8.33-1.36 0-2.64-.71-3.08-1.55 0 0-.67 2.55-.84 3.18-.3 1.17-1.12 2.64-1.67 3.54 1.26.39 2.59.6 3.98.6 6.83 0 12.38-4.87 12.38-10.98C24.88 4.865 19.34.001 12.504.001"/>
            </svg>
          </div>
          <h3 class="text-2xl font-bold text-gray-900 mb-4">Linux</h3>
          <p class="text-gray-600 mb-6">支持 Ubuntu 18.04+</p>
          <div class="space-y-3 mb-8">
            <div class="flex justify-between text-sm">
              <span class="text-gray-600">文件大小:</span>
              <span class="font-semibold">~40MB</span>
            </div>
            <div class="flex justify-between text-sm">
              <span class="text-gray-600">格式:</span>
              <span class="font-semibold">AppImage</span>
            </div>
          </div>
          <a 
            href="https://github.com/pengcunfu/MarkdownManager/releases/latest/download/MarkdownManager-Linux-x86_64.AppImage" 
            class="w-full bg-orange-600 hover:bg-orange-700 text-white py-3 px-6 rounded-lg font-semibold transition-colors inline-flex items-center justify-center"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            下载 AppImage
          </a>
        </div>
      </div>

      <!-- Installation Instructions -->
      <div class="bg-gray-50 rounded-2xl p-8 mb-12">
        <h2 class="text-2xl font-bold text-gray-900 mb-8 text-center">安装说明</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Windows Installation -->
          <div>
            <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
              <svg class="w-5 h-5 text-blue-600 mr-2" fill="currentColor" viewBox="0 0 24 24">
                <path d="M0 3.449L9.75 2.1v9.451H0m10.949-9.602L24 0v11.4H10.949M0 12.6h9.75v9.451L0 20.699M10.949 12.6H24V24l-13.051-1.351"/>
              </svg>
              Windows
            </h3>
            <ol class="text-sm text-gray-600 space-y-2">
              <li>1. 下载 .exe 安装文件</li>
              <li>2. 双击运行安装程序</li>
              <li>3. 按照向导完成安装</li>
              <li>4. 从开始菜单启动应用</li>
            </ol>
          </div>

          <!-- macOS Installation -->
          <div>
            <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
              <svg class="w-5 h-5 text-gray-600 mr-2" fill="currentColor" viewBox="0 0 24 24">
                <path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/>
              </svg>
              macOS
            </h3>
            <ol class="text-sm text-gray-600 space-y-2">
              <li>1. 下载 .dmg 文件</li>
              <li>2. 双击挂载磁盘镜像</li>
              <li>3. 拖拽应用到 Applications 文件夹</li>
              <li>4. 从 Launchpad 启动应用</li>
            </ol>
          </div>

          <!-- Linux Installation -->
          <div>
            <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
              <svg class="w-5 h-5 text-orange-600 mr-2" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12.504 0C5.678 0 .126 4.865.126 10.982c0 4.964 3.241 9.19 7.74 10.18-.113-.9-.21-2.28.044-3.26.232-.9 1.487-6.3 1.487-6.3s-.38-.76-.38-1.88c0-1.76 1.02-3.07 2.29-3.07 1.08 0 1.61.81 1.61 1.78 0 1.08-.69 2.7-1.04 4.2-.3 1.26.63 2.28 1.87 2.28 2.24 0 3.97-2.36 3.97-5.75 0-3.01-2.16-5.11-5.25-5.11-3.58 0-5.68 2.68-5.68 5.45 0 1.08.42 2.24.94 2.87.1.13.12.24.09.37-.1.4-.32 1.31-.37 1.49-.06.24-.2.29-.46.18-1.67-.78-2.71-3.22-2.71-5.18 0-4.23 3.07-8.11 8.86-8.11 4.65 0 8.27 3.31 8.27 7.74 0 4.62-2.91 8.33-6.96 8.33-1.36 0-2.64-.71-3.08-1.55 0 0-.67 2.55-.84 3.18-.3 1.17-1.12 2.64-1.67 3.54 1.26.39 2.59.6 3.98.6 6.83 0 12.38-4.87 12.38-10.98C24.88 4.865 19.34.001 12.504.001"/>
              </svg>
              Linux
            </h3>
            <ol class="text-sm text-gray-600 space-y-2">
              <li>1. 下载 .AppImage 文件</li>
              <li>2. 添加执行权限：<code>chmod +x *.AppImage</code></li>
              <li>3. 双击运行或命令行执行</li>
              <li>4. 可选：集成到系统菜单</li>
            </ol>
          </div>
        </div>
      </div>

      <!-- System Requirements -->
      <div class="bg-white rounded-2xl shadow-lg p-8 mb-12">
        <h2 class="text-2xl font-bold text-gray-900 mb-8 text-center">系统要求</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <h3 class="text-lg font-semibold text-gray-900 mb-4">最低要求</h3>
            <ul class="text-gray-600 space-y-2">
              <li>• RAM: 4GB</li>
              <li>• 存储空间: 200MB</li>
              <li>• Python 3.8+ (开发版)</li>
            </ul>
          </div>
          <div>
            <h3 class="text-lg font-semibold text-gray-900 mb-4">推荐配置</h3>
            <ul class="text-gray-600 space-y-2">
              <li>• RAM: 8GB+</li>
              <li>• 存储空间: 1GB+</li>
              <li>• SSD 硬盘</li>
            </ul>
          </div>
          <div>
            <h3 class="text-lg font-semibold text-gray-900 mb-4">支持的系统</h3>
            <ul class="text-gray-600 space-y-2">
              <li>• Windows 10/11</li>
              <li>• macOS 11.0+</li>
              <li>• Ubuntu 18.04+</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Alternative Downloads -->
      <div class="text-center">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">其他下载方式</h2>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <a 
            href="https://github.com/pengcunfu/MarkdownManager/releases" 
            target="_blank"
            class="bg-gray-900 hover:bg-gray-800 text-white px-6 py-3 rounded-lg font-semibold transition-colors inline-flex items-center"
          >
            <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
            GitHub Releases
          </a>
          <a 
            href="https://github.com/pengcunfu/MarkdownManager" 
            target="_blank"
            class="border-2 border-gray-300 hover:border-gray-400 text-gray-700 hover:text-gray-900 px-6 py-3 rounded-lg font-semibold transition-colors inline-flex items-center"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3M7 13l3 3 7-7" />
            </svg>
            源码编译
          </a>
        </div>
        <p class="text-gray-600 mt-4">
          遇到问题？查看 <router-link to="/docs" class="text-primary-600 hover:text-primary-700">使用文档</router-link> 或 
          <a href="https://github.com/pengcunfu/MarkdownManager/issues" target="_blank" class="text-primary-600 hover:text-primary-700">提交问题</a>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Download'
}
</script>
