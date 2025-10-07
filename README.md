# Markdown Manager 官方网站

这是 Markdown Manager 的官方网站源码，使用 Vue 3 + Tailwind CSS 构建。

## 🚀 快速开始

### 安装依赖
```bash
npm install
```

### 开发服务器
```bash
npm run dev
```

### 构建生产版本
```bash
npm run build
```

### 预览构建结果
```bash
npm run preview
```

### 部署到 GitHub Pages
```bash
npm run deploy
```

## 📁 项目结构

```
├── src/
│   ├── components/          # 组件
│   │   ├── Navbar.vue      # 导航栏
│   │   └── Footer.vue      # 页脚
│   ├── pages/              # 页面
│   │   ├── Home.vue        # 首页
│   │   ├── Features.vue    # 功能特性
│   │   ├── Download.vue    # 下载页面
│   │   └── Docs.vue        # 文档页面
│   ├── App.vue             # 根组件
│   ├── main.js             # 入口文件
│   └── style.css           # 全局样式
├── public/                 # 静态资源
├── index.html              # HTML 模板
├── package.json            # 项目配置
├── vite.config.js          # Vite 配置
├── tailwind.config.js      # Tailwind 配置
└── postcss.config.js       # PostCSS 配置
```

## 🛠️ 技术栈

- **框架**: Vue 3
- **构建工具**: Vite
- **样式**: Tailwind CSS
- **路由**: Vue Router
- **部署**: GitHub Pages

## 📝 开发说明

### 添加新页面
1. 在 `src/pages/` 目录下创建新的 Vue 组件
2. 在 `src/main.js` 中添加路由配置
3. 在导航栏中添加链接

### 修改样式
- 全局样式在 `src/style.css` 中定义
- 组件样式使用 Tailwind CSS 类名
- 自定义样式可以在 `tailwind.config.js` 中配置

### 部署流程
1. 提交代码到 gh-pages 分支
2. 运行 `npm run deploy` 自动构建并部署
3. 网站将在 `https://pengcunfu.github.io/MarkdownManager/` 可访问

## 🔗 相关链接

- [Markdown Manager 主项目](https://github.com/pengcunfu/MarkdownManager)
- [Vue 3 文档](https://vuejs.org/)
- [Tailwind CSS 文档](https://tailwindcss.com/)
- [Vite 文档](https://vitejs.dev/)

## 📄 许可证

MIT License
