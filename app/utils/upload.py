import os
import oss2
import logging
import shutil
from datetime import datetime
import random
from app.utils import md5, file_md5
from minio import Minio
from minio.error import S3Error
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 从环境变量中读取阿里云 OSS 配置信息
oss_endpoint = os.getenv('OSS_ENDPOINT')
oss_access_key = os.getenv('OSS_ACCESS_KEY')
oss_secret_key = os.getenv('OSS_SECRET_KEY')
oss_bucket_name = os.getenv('OSS_BUCKET_NAME')

# 从环境变量中读取 MinIO 配置信息
minio_endpoint = os.getenv('MINIO_ENDPOINT', "8.155.40.179:9000")
minio_access_key = os.getenv('MINIO_ACCESS_KEY', "huaqiwill")
minio_secret_key = os.getenv('MINIO_SECRET_KEY', "Bing2003")
minio_bucket_name = os.getenv('MINIO_BUCKET_NAME', "blog")
minio_secure = os.getenv('MINIO_SECURE', "False").lower() in ("true", "1", "t")

# 初始化 MinIO 客户端
minio_client = Minio(minio_endpoint, minio_access_key, minio_secret_key, secure=minio_secure)


def upload_to_local(file_path: str, image_path: str, base_dir: str = "D:\\Data\\Markdown\\") -> str:
    """
    上传图片到本地文件夹。

    :param file_path: Markdown 文件路径，用于生成唯一目录。
    :param image_path: 图片文件路径。
    :param base_dir: 本地存储的基础目录。
    :return: 图片在本地存储的路径。
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"文件 {image_path} 不存在")

    file_path = os.path.normpath(os.path.realpath(file_path))
    image_path = os.path.normpath(os.path.realpath(image_path))

    if file_path == image_path:
        return file_path

    file_path_md5 = md5(file_path)
    image_name = os.path.basename(image_path)
    path = os.path.normpath(os.path.join(base_dir, file_path_md5))

    if not os.path.exists(path):
        os.makedirs(path)

    save_path = os.path.normpath(os.path.join(path, image_name))

    if os.path.exists(save_path):
        src_image_md5 = file_md5(image_path)
        dst_img_md5 = file_md5(save_path)
        if src_image_md5 == dst_img_md5:
            return save_path

    shutil.copy(image_path, save_path)
    return save_path


def upload_to_oss(file_path: str, local_path: str) -> str | None:
    """
    上传文件到阿里云 OSS 并返回公开 URL。

    :param file_path: Markdown 文件路径。
    :param local_path: 本地文件路径。
    :return: 上传后的文件 URL。
    """
    try:
        auth = oss2.Auth(oss_access_key, oss_secret_key)
        bucket = oss2.Bucket(auth, oss_endpoint, oss_bucket_name)

        file_name = os.path.basename(local_path)
        oss_path = f"uploads/{datetime.now().strftime('%Y%m%d%H%M%S')}/{random.randint(1000, 9999)}_{file_name}"
        bucket.put_object_from_file(oss_path, local_path)
        url = f"{bucket._Bucket__endpoint}/{oss_path}"
        logging.info(f"Uploaded: {local_path} -> {url}")
        return url
    except Exception as e:
        logging.error(f"Failed to upload {local_path} to OSS: {e}")
        return None


def upload_to_minio(object_name: str, file_path: str):
    """
    上传文件到 MinIO 并返回公开 URL。

    :param object_name: MinIO 中的对象名称。
    :param file_path: 本地文件路径。
    :return: 上传后的文件 URL。
    """
    try:
        # 检查存储桶是否存在，如果不存在则创建
        if not minio_client.bucket_exists(minio_bucket_name):
            minio_client.make_bucket(minio_bucket_name)
            print(f"Bucket '{minio_bucket_name}' created.")

        # 设置元数据
        metadata = {
            "Content-Disposition": "inline",  # 设置为预览模式
            "Content-Type": "image/jpeg"  # 指定文件类型
        }

        # 上传图片并附加元数据
        minio_client.fput_object(
            minio_bucket_name, object_name, file_path, metadata=metadata)
        prefix = "https://" if minio_secure else "http://"
        url = f"{prefix}{minio_endpoint}/{minio_bucket_name}/{object_name}"
        print(
            f"Image '{file_path}' uploaded as '{object_name}' to bucket '{minio_bucket_name}' and url is '{url}'.")
        return url
    except S3Error as e:
        print(f"Error uploading image: {e}")
        return None
