import configparser
import hashlib
import mistune
from bs4 import BeautifulSoup

import requests


def read_config(section: str, key: str):
    """获取配置文件"""
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config[section][key]


def save_config(section: str, key: str, value: str):
    """
    保存配置文件
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    config.set(section, key, value)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def download_image(url: str, save_path: str) -> bool:
    """
    下载网络图片到本地，并且返回是否成功
    :param url: 网络图片地址
    :param save_path: 保存路径
    """
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def md5(data: str) -> str:
    """
    计算字符串的md5
    :param data:
    :return:
    """
    md5_hash = hashlib.md5()  # 创建 md5 哈希对象
    md5_hash.update(data.encode('utf-8'))  # 更新哈希对象，数据需为字节类型
    return md5_hash.hexdigest()  # 返回16进制的MD5结果


def file_md5(file: str) -> str:
    with open(file, 'rb') as f:
        md5_hash = hashlib.md5()  # 创建 md5 哈希对象
        md5_hash.update(f.read())  # 更新哈希对象，数据需为字节类型
        return md5_hash.hexdigest()  # 返回16进制的MD5结果


def generate_outline(md_text: str):
    """ 解析 Markdown 并提取大纲（标题）"""
    # 解析 Markdown 为 HTML
    markdown_parser = mistune.create_markdown(renderer=mistune.HTMLRenderer())
    html_content = markdown_parser(md_text)

    # 用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, "html.parser")
    outline = []

    # 遍历 h1 - h6 标题
    for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        level = int(tag.name[1])  # h1 -> 1, h2 -> 2, ...
        outline.append((level, tag.text.strip()))  # 记录 (标题级别, 标题文本)

    return outline
