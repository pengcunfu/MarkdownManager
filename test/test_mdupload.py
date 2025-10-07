from mdupload import MdUpload, LocalFileUploader

MdUpload("./test/微信小程序基础.md", LocalFileUploader()
              ).build_remote_file_name("test.md")
