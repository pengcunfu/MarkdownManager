<template>
  <div class="py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Header -->
      <div class="text-center mb-16">
        <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">使用文档</h1>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          详细的使用指南，帮助你快速上手 Markdown Manager 的各项功能
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-4 gap-8">
        <!-- 侧边栏导航 -->
        <div class="lg:col-span-1">
          <div class="bg-white rounded-lg shadow-lg p-6 sticky top-24">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">目录</h3>
            <nav class="space-y-2">
              <a href="#quick-start" class="block text-gray-600 hover:text-primary-600 py-1 transition-colors">快速开始</a>
              <a href="#basic-usage" class="block text-gray-600 hover:text-primary-600 py-1 transition-colors">基础使用</a>
              <a href="#advanced-features" class="block text-gray-600 hover:text-primary-600 py-1 transition-colors">高级功能</a>
              <a href="#configuration" class="block text-gray-600 hover:text-primary-600 py-1 transition-colors">配置说明</a>
              <a href="#cloud-sync" class="block text-gray-600 hover:text-primary-600 py-1 transition-colors">云端同步</a>
              <a href="#troubleshooting" class="block text-gray-600 hover:text-primary-600 py-1 transition-colors">故障排除</a>
              <a href="#faq" class="block text-gray-600 hover:text-primary-600 py-1 transition-colors">常见问题</a>
            </nav>
          </div>
        </div>

        <!-- 主要内容 -->
        <div class="lg:col-span-3">
          <div class="prose prose-lg max-w-none">
            <!-- 快速开始 -->
            <section id="quick-start" class="mb-12">
              <h2 class="text-3xl font-bold text-gray-900 mb-6">快速开始</h2>
              <div class="bg-blue-50 rounded-lg p-6 mb-6">
                <h3 class="text-xl font-semibold text-blue-900 mb-4">安装步骤</h3>
                <ol class="list-decimal list-inside space-y-2 text-blue-800">
                  <li>从 <router-link to="/download" class="text-blue-600 hover:text-blue-700 underline">下载页面</router-link> 获取适合你系统的安装包</li>
                  <li>按照安装向导完成安装</li>
                  <li>首次启动时，选择文档存储目录</li>
                  <li>开始创建和管理你的 Markdown 文档</li>
                </ol>
              </div>
              
              <h3 class="text-xl font-semibold text-gray-900 mb-4">首次配置</h3>
              <p class="text-gray-600 mb-4">
                启动应用后，你需要进行一些基本配置：
              </p>
              <ul class="list-disc list-inside space-y-2 text-gray-600 mb-6">
                <li><strong>文档目录：</strong>选择存储 Markdown 文件的本地目录</li>
                <li><strong>主题设置：</strong>选择明亮或暗黑主题</li>
                <li><strong>编辑器设置：</strong>配置字体大小、行号显示等</li>
                <li><strong>预览设置：</strong>选择预览样式和代码高亮主题</li>
              </ul>
            </section>

            <!-- 基础使用 -->
            <section id="basic-usage" class="mb-12">
              <h2 class="text-3xl font-bold text-gray-900 mb-6">基础使用</h2>
              
              <h3 class="text-xl font-semibold text-gray-900 mb-4">创建和编辑文档</h3>
              <div class="bg-gray-50 rounded-lg p-6 mb-6">
                <h4 class="font-semibold text-gray-900 mb-3">创建新文档</h4>
                <ul class="list-disc list-inside space-y-1 text-gray-600 mb-4">
                  <li>点击工具栏的"新建"按钮</li>
                  <li>使用快捷键 <code class="bg-gray-200 px-2 py-1 rounded">Ctrl+N</code> (Windows/Linux) 或 <code class="bg-gray-200 px-2 py-1 rounded">Cmd+N</code> (macOS)</li>
                  <li>在文件树中右键选择"新建文件"</li>
                </ul>
                
                <h4 class="font-semibold text-gray-900 mb-3">编辑文档</h4>
                <ul class="list-disc list-inside space-y-1 text-gray-600">
                  <li>在左侧编辑器中输入 Markdown 内容</li>
                  <li>右侧预览窗口会实时显示渲染结果</li>
                  <li>支持语法高亮和自动补全</li>
                  <li>使用 <code class="bg-gray-200 px-2 py-1 rounded">Ctrl+S</code> 保存文档</li>
                </ul>
              </div>

              <h3 class="text-xl font-semibold text-gray-900 mb-4">文件管理</h3>
              <p class="text-gray-600 mb-4">
                左侧文件树提供了完整的文件管理功能：
              </p>
              <ul class="list-disc list-inside space-y-2 text-gray-600 mb-6">
                <li><strong>浏览文件：</strong>点击文件名打开文档</li>
                <li><strong>创建文件夹：</strong>右键选择"新建文件夹"</li>
                <li><strong>重命名：</strong>右键文件或文件夹选择"重命名"</li>
                <li><strong>删除：</strong>右键选择"删除"（支持回收站恢复）</li>
                <li><strong>拖拽：</strong>支持拖拽移动文件和文件夹</li>
              </ul>
            </section>

            <!-- 高级功能 -->
            <section id="advanced-features" class="mb-12">
              <h2 class="text-3xl font-bold text-gray-900 mb-6">高级功能</h2>
              
              <h3 class="text-xl font-semibold text-gray-900 mb-4">全文搜索</h3>
              <div class="bg-green-50 rounded-lg p-6 mb-6">
                <p class="text-green-800 mb-4">
                  强大的搜索功能帮助你快速找到需要的内容：
                </p>
                <ul class="list-disc list-inside space-y-2 text-green-700">
                  <li>使用 <code class="bg-green-200 px-2 py-1 rounded">Ctrl+F</code> 打开搜索面板</li>
                  <li>支持关键词搜索和正则表达式</li>
                  <li>搜索结果高亮显示</li>
                  <li>支持替换功能</li>
                  <li>可以在指定文件夹内搜索</li>
                </ul>
              </div>

              <h3 class="text-xl font-semibold text-gray-900 mb-4">导出功能</h3>
              <p class="text-gray-600 mb-4">
                支持将 Markdown 文档导出为多种格式：
              </p>
              <ul class="list-disc list-inside space-y-2 text-gray-600 mb-6">
                <li><strong>HTML：</strong>保持样式的网页格式</li>
                <li><strong>PDF：</strong>适合打印和分享的文档格式</li>
                <li><strong>Word：</strong>Microsoft Word 兼容格式</li>
                <li><strong>图片：</strong>将文档渲染为图片</li>
              </ul>

              <h3 class="text-xl font-semibold text-gray-900 mb-4">插件系统</h3>
              <p class="text-gray-600 mb-4">
                通过插件扩展应用功能：
              </p>
              <ul class="list-disc list-inside space-y-2 text-gray-600 mb-6">
                <li>数学公式渲染 (MathJax)</li>
                <li>流程图支持 (Mermaid)</li>
                <li>代码高亮 (Highlight.js)</li>
                <li>表格增强功能</li>
                <li>自定义 CSS 样式</li>
              </ul>
            </section>

            <!-- 配置说明 -->
            <section id="configuration" class="mb-12">
              <h2 class="text-3xl font-bold text-gray-900 mb-6">配置说明</h2>
              
              <h3 class="text-xl font-semibold text-gray-900 mb-4">基本配置</h3>
              <p class="text-gray-600 mb-4">
                在"设置"菜单中可以配置各种选项：
              </p>
              
              <div class="bg-gray-50 rounded-lg p-6 mb-6">
                <h4 class="font-semibold text-gray-900 mb-3">编辑器设置</h4>
                <ul class="list-disc list-inside space-y-1 text-gray-600 mb-4">
                  <li>字体类型和大小</li>
                  <li>行号显示</li>
                  <li>自动换行</li>
                  <li>缩进设置</li>
                </ul>
                
                <h4 class="font-semibold text-gray-900 mb-3">预览设置</h4>
                <ul class="list-disc list-inside space-y-1 text-gray-600">
                  <li>预览主题选择</li>
                  <li>代码高亮样式</li>
                  <li>数学公式渲染</li>
                  <li>同步滚动开关</li>
                </ul>
              </div>

              <h3 class="text-xl font-semibold text-gray-900 mb-4">配置文件</h3>
              <p class="text-gray-600 mb-4">
                高级用户可以直接编辑配置文件：
              </p>
              <pre class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto mb-6">
<code>[default]
LOCAL_STORAGE = /path/to/your/documents
STRATEGY = local

[editor]
FONT_SIZE = 14
SHOW_LINE_NUMBERS = true
WORD_WRAP = true

[preview]
THEME = github
CODE_HIGHLIGHT = true
MATH_RENDERING = true</code>
              </pre>
            </section>

            <!-- 云端同步 -->
            <section id="cloud-sync" class="mb-12">
              <h2 class="text-3xl font-bold text-gray-900 mb-6">云端同步</h2>
              
              <div class="bg-yellow-50 rounded-lg p-6 mb-6">
                <h3 class="text-xl font-semibold text-yellow-900 mb-4">⚠️ 安全提醒</h3>
                <p class="text-yellow-800 mb-4">
                  配置云端同步前，请确保：
                </p>
                <ul class="list-disc list-inside space-y-1 text-yellow-700">
                  <li>妥善保管你的访问密钥</li>
                  <li>不要在公共场所或不安全的网络环境下配置</li>
                  <li>定期更换访问密钥以确保安全</li>
                </ul>
              </div>

              <h3 class="text-xl font-semibold text-gray-900 mb-4">阿里云 OSS 配置</h3>
              <ol class="list-decimal list-inside space-y-2 text-gray-600 mb-6">
                <li>在阿里云控制台创建 OSS 存储桶</li>
                <li>获取 AccessKey ID 和 AccessKey Secret</li>
                <li>在应用设置中配置 OSS 信息</li>
                <li>测试连接并开始同步</li>
              </ol>

              <h3 class="text-xl font-semibold text-gray-900 mb-4">飞书集成</h3>
              <p class="text-gray-600 mb-4">
                支持将文档同步到飞书文档：
              </p>
              <ul class="list-disc list-inside space-y-2 text-gray-600 mb-6">
                <li>配置飞书 API 凭证</li>
                <li>选择目标文件夹</li>
                <li>自动转换格式并上传</li>
                <li>支持团队协作和评论</li>
              </ul>
            </section>

            <!-- 故障排除 -->
            <section id="troubleshooting" class="mb-12">
              <h2 class="text-3xl font-bold text-gray-900 mb-6">故障排除</h2>
              
              <div class="space-y-6">
                <div class="bg-red-50 rounded-lg p-6">
                  <h3 class="text-lg font-semibold text-red-900 mb-3">应用无法启动</h3>
                  <ul class="list-disc list-inside space-y-1 text-red-700">
                    <li>检查系统是否满足最低要求</li>
                    <li>尝试以管理员权限运行</li>
                    <li>检查防火墙和杀毒软件设置</li>
                    <li>重新安装应用程序</li>
                  </ul>
                </div>

                <div class="bg-orange-50 rounded-lg p-6">
                  <h3 class="text-lg font-semibold text-orange-900 mb-3">预览不显示</h3>
                  <ul class="list-disc list-inside space-y-1 text-orange-700">
                    <li>检查 Markdown 语法是否正确</li>
                    <li>尝试刷新预览窗口</li>
                    <li>检查预览主题设置</li>
                    <li>重启应用程序</li>
                  </ul>
                </div>

                <div class="bg-blue-50 rounded-lg p-6">
                  <h3 class="text-lg font-semibold text-blue-900 mb-3">云端同步失败</h3>
                  <ul class="list-disc list-inside space-y-1 text-blue-700">
                    <li>检查网络连接</li>
                    <li>验证访问密钥是否正确</li>
                    <li>检查存储桶权限设置</li>
                    <li>查看错误日志获取详细信息</li>
                  </ul>
                </div>
              </div>
            </section>

            <!-- 常见问题 -->
            <section id="faq" class="mb-12">
              <h2 class="text-3xl font-bold text-gray-900 mb-6">常见问题</h2>
              
              <div class="space-y-6">
                <div class="border-l-4 border-primary-500 pl-6">
                  <h3 class="text-lg font-semibold text-gray-900 mb-2">Q: 支持哪些 Markdown 语法？</h3>
                  <p class="text-gray-600">
                    A: 支持标准 Markdown 语法以及 GitHub Flavored Markdown (GFM) 扩展，包括表格、任务列表、代码高亮等。
                  </p>
                </div>

                <div class="border-l-4 border-primary-500 pl-6">
                  <h3 class="text-lg font-semibold text-gray-900 mb-2">Q: 可以导入现有的 Markdown 文件吗？</h3>
                  <p class="text-gray-600">
                    A: 可以。将现有的 .md 文件复制到文档目录中，应用会自动识别并显示在文件树中。
                  </p>
                </div>

                <div class="border-l-4 border-primary-500 pl-6">
                  <h3 class="text-lg font-semibold text-gray-900 mb-2">Q: 如何备份我的文档？</h3>
                  <p class="text-gray-600">
                    A: 建议定期备份文档目录，或者使用云端同步功能自动备份到云存储服务。
                  </p>
                </div>

                <div class="border-l-4 border-primary-500 pl-6">
                  <h3 class="text-lg font-semibold text-gray-900 mb-2">Q: 支持团队协作吗？</h3>
                  <p class="text-gray-600">
                    A: 通过飞书集成可以实现团队协作，支持多人编辑和评论功能。
                  </p>
                </div>

                <div class="border-l-4 border-primary-500 pl-6">
                  <h3 class="text-lg font-semibold text-gray-900 mb-2">Q: 如何获取技术支持？</h3>
                  <p class="text-gray-600">
                    A: 可以通过 <a href="https://github.com/pengcunfu/MarkdownManager/issues" target="_blank" class="text-primary-600 hover:text-primary-700 underline">GitHub Issues</a> 提交问题，或者参与 <a href="https://github.com/pengcunfu/MarkdownManager/discussions" target="_blank" class="text-primary-600 hover:text-primary-700 underline">社区讨论</a>。
                  </p>
                </div>
              </div>
            </section>

            <!-- 联系支持 -->
            <div class="bg-primary-50 rounded-2xl p-8 text-center">
              <h2 class="text-2xl font-bold text-primary-900 mb-4">需要更多帮助？</h2>
              <p class="text-primary-700 mb-6">
                如果文档没有解决你的问题，欢迎联系我们获取支持
              </p>
              <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a 
                  href="https://github.com/pengcunfu/MarkdownManager/issues" 
                  target="_blank"
                  class="bg-primary-600 hover:bg-primary-700 text-white px-6 py-3 rounded-lg font-semibold transition-colors inline-flex items-center justify-center"
                >
                  <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                  </svg>
                  提交问题
                </a>
                <a 
                  href="https://github.com/pengcunfu/MarkdownManager/discussions" 
                  target="_blank"
                  class="border-2 border-primary-600 text-primary-600 hover:bg-primary-600 hover:text-white px-6 py-3 rounded-lg font-semibold transition-colors inline-flex items-center justify-center"
                >
                  <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a2 2 0 01-2-2v-6a2 2 0 012-2h8z" />
                  </svg>
                  社区讨论
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Docs'
}
</script>

<style scoped>
/* 平滑滚动到锚点 */
html {
  scroll-behavior: smooth;
}

/* 代码块样式 */
code {
  @apply bg-gray-200 text-gray-800 px-2 py-1 rounded text-sm;
}

pre code {
  @apply bg-transparent text-gray-100 p-0;
}
</style>
