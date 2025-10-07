from app.utils.oss import MarkdownUpload, LocalFileUploader

# def test():
#     """
#     解析三个参数，指定 Markdown 文件路径和上传策略
#     """
#     logging.basicConfig(level=logging.INFO)
#
#     parser = argparse.ArgumentParser(
#         description="mdupload: 上传 Markdown 文件中的图片到阿里云 OSS")
#     parser.add_argument('markdown', help="指定要处理的 Markdown 文件路径")
#     args = parser.parse_args()
#
#     if not os.path.exists(args.markdown):
#         logging.error(f"Error: File not found - {args.markdown}")
#         sys.exit(1)
#
#     # 本地存储库路径
#     LOCAL_STORAGE = read_config("default", "LOCAL_STORAGE")
#     STRATEGY = read_config("default", "STRATEGY")
#
#     if STRATEGY.lower() == "local":
#         uploader = LocalFileUploader(LOCAL_STORAGE)
#     elif STRATEGY.lower() == "oss":
#         uploader = OssFileUploader()
#     else:
#         logging.error(f"Error: Invalid strategy - {STRATEGY}")
#         sys.exit(1)
#
#     # 开始处理
#     MarkdownUpload(args.markdown, uploader).handle_file()


file_path = r"D:\MyProjects\Tools\MarkdownManager\tests\resources\微信小程序基础.md"
m = MarkdownUpload(file_path, LocalFileUploader())
with open(file_path, mode="r", encoding="utf-8") as f:
    data = f.read()
    print(m.handle(data))
