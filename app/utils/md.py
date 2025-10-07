import os
import re
import pypandoc
from app.utils.db import add_document


def md_export(file_path: str, save_path: str):
    """
    导出 Markdown 文件并将图片链接替换为本地链接。

    1. 读取 Markdown 文件内容。
    2. 解析 Markdown 文件中的图片链接。
    3. 下载图片到本地并替换链接。
    4. 将处理后的内容保存到指定路径。

    :param file_path: Markdown 文件路径。
    :param save_path: 处理后文件保存的路径。
    """
    from app.utils.upload import MarkdownUpload, LocalFileUploader

    # 检查文件类型是否为 .md
    if not file_path.endswith('.md'):
        raise ValueError("The provided file is not a Markdown (.md) file.")

    file_dir = os.path.dirname(save_path)
    base_dir = os.path.normpath(os.path.join(file_dir, "mark_image"))
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    local = LocalFileUploader(base_dir)
    content = MarkdownUpload(file_path, local).handle()
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(content)


def md_to_pdf(input_file: str, output_file: str):
    """
    将 Markdown 文件转换为 PDF 文件。

    :param input_file: 输入的 Markdown 文件路径。
    :param output_file: 输出的 PDF 文件路径。
    """
    # 将 Markdown 转换为 PDF
    pypandoc.convert_file(input_file, 'pdf', outputfile=output_file)
    print(f"{output_file} 转换成功！")


def md_merge(source_directory: str, output_file: str):
    """
    合并指定目录下的所有 Markdown 文件。

    1. 遍历目录下的所有 Markdown 文件。
    2. 将每个文件的内容读取并合并到目标文件中。
    3. 在每个文件内容后添加换行符以分隔文件内容。

    :param source_directory: 包含 Markdown 文件的目录路径。
    :param output_file: 合并后的文件保存路径。
    """
    # 创建或打开目标文件进行写入
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # 遍历指定目录下的所有文件
        for root, dirs, files in os.walk(source_directory):
            for file in files:
                # 拼接文件的完整路径
                file_path = os.path.join(root, file)

                # 检查文件类型（例如只合并.txt文件，可以根据需求调整）
                if file.endswith('.md'):
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        # 将文件内容写入目标文件
                        pattern = "---"
                        text = re.sub(pattern, "", infile.read())
                        outfile.write(text)  # 写入内容
                        outfile.write('\n\n')  # 在每个文件内容后添加两个换行符


def md_list(root_dir):
    """
    获取指定目录下的所有 Markdown 文件路径。

    :param root_dir: 根目录路径。
    :return: 包含所有 Markdown 文件路径的列表。
    """
    return [
        os.path.join(root, file)
        for root, _, files in os.walk(root_dir)
        for file in files if file.endswith(".md")
    ]


def md_list_content(root_dir):
    """
    遍历指定目录下的所有 Markdown 文件并将其内容存储到数据库。

    1. 获取目录下的所有 Markdown 文件路径。
    2. 读取每个文件的内容。
    3. 将文件路径和内容存储到数据库。

    :param root_dir: 根目录路径。
    """
    md_files = md_list(root_dir)
    for md_file in md_files:
        print(md_file)
        with open(md_file, 'r', encoding='utf-8') as infile:
            content = infile.read()
            add_document(md_file, content)


def process_markdown(file_path: str, upload_func) -> str:
    """
    处理 Markdown 文件中的图片链接。

    1. 读取 Markdown 文件内容。
    2. 查找并解析图片链接。
    3. 使用上传函数上传图片并获取新链接。
    4. 替换 Markdown 文件中的图片链接为新链接。

    :param file_path: Markdown 文件路径。
    :param upload_func: 图片上传函数，接受文件路径和图片路径作为参数。
    :return: 处理后的 Markdown 文件内容。
    """
    with open(file_path, mode="r", encoding="utf-8") as f:
        text = f.read()

        pattern = r'!\[.*?\]\((.*?)\)'
        matches = re.findall(pattern, text)

        image_map = {}

        for image in matches:
            if not image.startswith("http://") and not image.startswith("https://"):
                image_path = os.path.abspath(image)
                if os.path.exists(image_path):
                    upload_url = upload_func(file_path, image_path)
                    if upload_url:
                        image_map[image] = upload_url

        for old, new in image_map.items():
            text = text.replace(old, new)

        return text


def process_markdown_file(file_path: str, upload_func):
    """
    处理 Markdown 文件并将修改后的内容写回文件。

    1. 读取 Markdown 文件内容。
    2. 调用 `process_markdown` 处理图片链接。
    3. 将处理后的内容写回原文件。

    :param file_path: Markdown 文件路径。
    :param upload_func: 图片上传函数，接受文件路径和图片路径作为参数。
    """
    with open(file_path, 'r+', encoding='utf-8') as file:
        content = file.read()
        content = process_markdown(file_path, upload_func)
        file.seek(0)
        file.truncate()
        file.write(content)



