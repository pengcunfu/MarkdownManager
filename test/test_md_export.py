import sys

if __name__ == "__main__":
    """
    从命令行参数中获取md文件的路径并处理图片
    """
    if len(sys.argv) < 3:
        print("Usage: python script.py <markdown_file_path> <copy_to>")
        sys.exit(1)

    file_path = sys.argv[1]
    copy_to = sys.argv[2]
    try:
        md_export = MdExport(file_path)
        md_export.handle(copy_to=copy_to)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
