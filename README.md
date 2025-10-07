# Markdown文档管理工具

MarkdownTools



功能：

预览md文件，并且添加全文检索功能。



添加一个功能：

* 从html中解析出表格，并且转换成md所支持的表格格式。
* 





## Markdown管理工具







# mdupload

`mdupload` 是一个用于处理 Markdown 文件中图片路径的工具，可以将本地图片或网络图片上传到阿里云 OSS，并自动替换 Markdown 文件中的图片路径为 OSS 的公开 URL。

## 功能特点

- 自动解析 Markdown 文件中的图片路径。
- 支持本地图片和网络图片的上传。
- 自动替换 Markdown 文件中的图片路径为 OSS URL。
- 支持下载网络图片到本地临时目录。
- 自动清理上传后的本地图片文件。

## 环境依赖

- Python 3.x
- 必要的第三方库：
  - `oss2`
  - `requests`

## 安装

1. 克隆项目到本地：

   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

### 运行脚本

```bash
python mdupload.py <markdown_file>
```

### 参数说明

- `<markdown_file>`：指定需要处理的 Markdown 文件路径。

## 示例

假设有一个名为 `example.md` 的 Markdown 文件，内容如下：

```markdown
![本地图片](images/local_image.png)
![网络图片](https://example.com/image.png)
```

运行以下命令：

```bash
python mdupload.py example.md
```

执行后：

- 本地图片 `images/local_image.png` 将被上传到阿里云 OSS，并替换为公开 URL。
- 网络图片 `https://example.com/image.png` 将被下载到本地临时目录，上传到 OSS 后同样替换为公开 URL。

更新后的 `example.md` 文件示例：

```markdown
![本地图片](https://oss-cn-beijing.aliyuncs.com/uploads/local_image.png)
![网络图片](https://oss-cn-beijing.aliyuncs.com/uploads/image.png)
```

## 配置信息

### 配置文件设置

1. 复制配置模板文件：
   ```bash
   cp resources/config.ini.example resources/config.ini
   ```

2. 编辑 `resources/config.ini` 文件，填入你的阿里云 OSS 配置信息：
   ```ini
   [default]
   LOCAL_STORAGE = D:/Data/Markdown
   STRATEGY = local
   [oss]
   ACCESS_KEY_ID = your_access_key_id_here
   ACCESS_KEY_SECRET = your_access_key_secret_here
   ENDPOINT = https://oss-cn-beijing.aliyuncs.com
   BUCKET_NAME = your_bucket_name_here
   ```

### 安全注意事项

⚠️ **重要提醒**：
- `resources/config.ini` 文件已被添加到 `.gitignore` 中，不会被提交到版本控制系统
- 请勿在代码中硬编码敏感信息（如 ACCESS_KEY_ID 和 ACCESS_KEY_SECRET）
- 建议定期更换访问密钥以确保安全性

## 功能函数说明

- `is_url(path)`：判断路径是否为 URL。
- `download_image(url, download_path)`：下载网络图片到本地。
- `upload_to_oss(local_path, oss_path)`：上传文件到阿里云 OSS 并返回公开 URL。
- `resolve_path(md_file, image_path)`：解析相对路径和绝对路径。
- `process_markdown(md_file)`：解析 Markdown 文件并处理图片路径。

## 注意事项

1. 确保 OSS 配置正确并有上传权限。
2. 本工具会清理本地临时图片文件，请在执行前备份重要文件。
3. 脚本会直接修改传入的 Markdown 文件，建议提前备份。

## 许可证

本项目基于 MIT 许可证发布。

---

感谢使用 mdupload！如有问题，请提交 issue 或联系开发者。



# mdfeishu

我的Md文件可以上传到飞书，后续如果大家有需要可以到其他平台，支持协作，本地的模式。





