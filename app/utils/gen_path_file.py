from pathlib import Path


def out_put(dic_text):
    data_str = ""
    for key in dic_text.keys():
        data_str += f'{key}: "{dic_text.get(key)}",'
    data_str = "{" + data_str + "},"
    print(data_str)
    return data_str


def list_dir_md_and_out_put(dir_path: str, prefix: str, log_callback=None):
    try:
        md_files = list(Path(dir_path).rglob("*.md"))  # 修改 glob 为 rglob 以递归查找
        all_str = ""
        for md_file in md_files:
            text = {"text": md_file.name,
                    "link": f'{prefix}\\{md_file.name}'.replace('\\', '/')}
            data_str = out_put(text)
            all_str += data_str + '\n'
        if log_callback:
            log_callback(all_str)
        return all_str
    except Exception as e:
        if log_callback:
            log_callback(f"Error: {e}")
        raise
