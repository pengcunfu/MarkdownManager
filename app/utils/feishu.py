import os
import requests
from typing import Dict, List


def sync_feishu_cloud(local_data: Dict, feishu_api_token: str, feishu_folder_id: str) -> bool:
    """
    将本地数据同步到飞书云端 
    :param local_data: 本地数据（字典形式，包含文件路径和内容）
    :param feishu_api_token: 飞书 API 访问令牌 
    :param feishu_folder_id: 飞书云端文件夹 ID 
    :return: 同步是否成功 
    """
    try:
        # 飞书 API 上传文件的 URL 
        upload_url = "https://open.feishu.cn/open-apis/drive/v1/files/upload_all"

        # 遍历本地数据，逐个上传到飞书云端 
        for file_name, file_content in local_data.items():
            # 构建请求体 
            payload = {
                "file_name": file_name,
                "parent_type": "explorer",
                "parent_node": feishu_folder_id,
                "file": (file_name, file_content)
            }

            # 发送请求 
            headers = {"Authorization": f"Bearer {feishu_api_token}"}
            response = requests.post(upload_url, headers=headers, files=payload)

            # 检查响应状态 
            if response.status_code != 200:
                print(f"Failed to upload {file_name}: {response.json()}")
                return False

        print("Sync to Feishu Cloud: Success!")
        return True
    except Exception as e:
        print(f"Error during sync to Feishu Cloud: {e}")
        return False


def sync_feishu_local(feishu_api_token: str, feishu_folder_id: str, local_folder: str) -> bool:
    """
    将飞书云端数据同步到本地
    :param feishu_api_token: 飞书 API 访问令牌
    :param feishu_folder_id: 飞书云端文件夹 ID
    :param local_folder: 本地文件夹路径
    :return: 同步是否成功
    """
    try:
        # 飞书 API 获取文件列表的 URL
        list_url = f"https://open.feishu.cn/open-apis/drive/v1/files?parent_node={feishu_folder_id}"

        # 获取云端文件列表
        headers = {"Authorization": f"Bearer {feishu_api_token}"}
        response = requests.get(list_url, headers=headers)

        # 检查响应状态
        if response.status_code != 200:
            print(f"Failed to fetch file list: {response.json()}")
            return False

            # 解析文件列表
        file_list = response.json().get("data", {}).get("files", [])
        if not file_list:
            print("No files found in Feishu Cloud.")
            return False

            # 遍历云端文件，逐个下载到本地
        for file_info in file_list:
            file_id = file_info.get("file_id")
            file_name = file_info.get("name")
            download_url = f"https://open.feishu.cn/open-apis/drive/v1/files/{file_id}/download"

            # 下载文件
            response = requests.get(download_url, headers=headers)
            if response.status_code != 200:
                print(f"Failed to download {file_name}: {response.json()}")
                continue

                # 保存到本地
            local_path = os.path.join(local_folder, file_name)
            with open(local_path, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {file_name} to {local_path}")

        print("Sync to Local: Success!")
        return True
    except Exception as e:
        print(f"Error during sync to Local: {e}")
        return False
