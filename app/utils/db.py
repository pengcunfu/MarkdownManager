from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker

# 创建 SQLite 数据库连接
DATABASE_URL = "sqlite:///data.db"
engine = create_engine(DATABASE_URL, echo=True)

# 创建 ORM 基类
Base = declarative_base()


# 定义数据库表（模型）
class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, autoincrement=True)
    path = Column(Text, nullable=False)
    text = Column(Text, nullable=False)


# 创建表
Base.metadata.create_all(engine)

# 创建会话
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


# 插入数据
def add_document(path, text):
    document = Document(path=path, text=text)
    session.add(document)
    session.commit()


# 查询数据
def get_documents():
    documents = session.query(Document).all()
    return documents


# 查询包含文件内容
def get_documents_by_content(content):
    documents = session.query(Document).filter(Document.text.contains(content)).all()
    return documents


# 更新数据
def update_document(document_id, new_text, new_path):
    user = session.query(Document).filter(Document.id == document_id).first()
    if user:
        user.path = new_path
        user.text = new_text
        session.commit()


# 删除数据
def delete_document(document_id):
    document = session.query(Document).filter(Document.id == document_id).first()
    if document:
        session.delete(document)
        session.commit()
