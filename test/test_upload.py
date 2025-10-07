from app.utils.upload_minio import upload_image_to_minio
import test

test.cwd()
object_name = "images/33.jpg"  # 对象名称（MinIO 中的文件名）
file_path = "./data/30.jpg"  # 本地图片路径

url = upload_image_to_minio(object_name, file_path)
print(url)
