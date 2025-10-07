from app.utils import generate_outline

if __name__ == '__main__':

    # 示例 Markdown 文本
    md_text = """
    # 一级标题
    ## 二级标题 A
    ### 三级标题 A1
    ## 二级标题 B
    ### 三级标题 B1
    #### 四级标题 B1.1
    """

    # 生成大纲
    outline = generate_outline(md_text)
    for level, title in outline:
        print("  " * (level - 1) + f"- {title}")
