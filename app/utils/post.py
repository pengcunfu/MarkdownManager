import os
import re
from pathlib import Path
from app.utils.upload import upload_to_minio
from app.utils import file_md5


def resolve_path(image_path: str, md_file_path: str) -> str:
    """
    解析图片路径
    :param image_path: 图片路径（相对路径或绝对路径）
    :param md_file_path: Markdown 文件的路径
    :return: 解析后的绝对路径
    """
    if image_path.startswith("http://") or image_path.startswith("https://"):
        return image_path  # 如果是 URL，直接返回
    if not os.path.isabs(image_path):  # 如果是相对路径，则转换为绝对路径
        md_dir = os.path.dirname(md_file_path)
        image_path = os.path.join(md_dir, image_path)
    return os.path.abspath(image_path)


def get_object_name(md_file_path: str, image_path: str):
    return "images/" + file_md5(md_file_path) + "/" + os.path.basename(image_path)


def handle_md_file(read_file_path: str, write_file_path: str = None, log_callback=None) -> None:
    """
    处理 Markdown 文件，上传图片到 MinIO 并替换链接（路径模式）
    :param read_file_path: Markdown 文件的路径
    :param write_file_path: 输出文件的路径（可选）
    :param log_callback: 日志回调函数
    """
    try:
        with open(read_file_path, mode="r", encoding="utf-8") as file:
            content = file.read()

            # 查找所有图片路径
            pattern = r'!\[.*?\]\((.*?)\)'
            matches = re.findall(pattern, content)

            image_map = {}

            for image in matches:
                # 解析图片路径
                image_path = resolve_path(image, read_file_path)

                # 如果是本地文件，上传到 MinIO
                if os.path.exists(image_path):
                    object_name = get_object_name(read_file_path, image_path)  # 使用文件名作为 MinIO 中的对象名称
                    upload_url = upload_to_minio(object_name, image_path)
                    if upload_url:
                        image_map[image] = upload_url

            # 替换 Markdown 文件中的图片路径
            for old, new in image_map.items():
                content = content.replace(old, new)

            # 写入文件
            if write_file_path:
                with open(write_file_path, mode="w", encoding="utf-8") as output_file:
                    output_file.write(content)
                if log_callback:
                    log_callback(f"Markdown file saved to '{write_file_path}'.")
            else:
                with open(read_file_path, mode="w", encoding="utf-8") as file:
                    file.write(content)
                if log_callback:
                    log_callback(f"Markdown file '{read_file_path}' updated.")
    except Exception as e:
        if log_callback:
            log_callback(f"Error processing file '{read_file_path}': {e}")


def handle_md_dir(dir_path: str, out_dir: str, log_callback=None):
    """
    处理指定目录中的所有 Markdown 文件，上传图片到 MinIO 并替换链接
    :param dir_path: 需要遍历的目录路径
    :param out_dir: 输出目录路径
    :param log_callback: 日志回调函数
    """
    try:
        # 检查 dir_path 是否存在
        if not os.path.exists(dir_path):
            if log_callback:
                log_callback(f"错误：目录 '{dir_path}' 不存在。")
            return

        # 检查 out_dir 是否存在，如果不存在则创建
        if not os.path.exists(out_dir):
            if log_callback:
                log_callback(f"输出目录 '{out_dir}' 不存在，正在创建...")
            os.makedirs(out_dir, exist_ok=True)  # 递归创建目录

        # 获取所有 .md 文件
        md_files = list(Path(dir_path).rglob("*.md"))
        if not md_files:
            if log_callback:
                log_callback(f"目录 '{dir_path}' 中没有找到 Markdown 文件。")
            return

        # 处理每个 Markdown 文件
        for md_file in md_files:
            try:
                # 获取相对路径
                relative_path = md_file.relative_to(dir_path)
                # 构造输出文件路径，保持目录结构
                out_path = Path(out_dir, relative_path)
                # 确保输出目录存在
                out_path.parent.mkdir(parents=True, exist_ok=True)
                
                if log_callback:
                    log_callback(f"处理文件: {md_file} -> {out_path}")

                # 调用 handle_md_file 处理文件
                handle_md_file(str(md_file), str(out_path), log_callback)
            except Exception as e:
                if log_callback:
                    log_callback(f"Error processing file '{md_file}': {e}")
    except Exception as e:
        if log_callback:
            log_callback(f"Error processing directory '{dir_path}': {e}")
