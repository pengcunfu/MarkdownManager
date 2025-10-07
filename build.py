import os
import sys

from app.config import VERSION, YEAR, AUTHOR, COMPANY_NAME,PRODUCT_NAME

if sys.platform == "win32":
    args = [
        'nuitka',
        '--standalone',
        '--windows-console-mode=disable',
        '--plugin-enable=pyside6',
        '--assume-yes-for-downloads',
        # '--msvc=latest',              # Use MSVC
        '--mingw64',                    # Use MinGW
        '--show-memory',
        '--show-progress',
        '--windows-icon-from-ico=resources/logo.ico',
        f'--company-name={COMPANY_NAME}',
        f'--product-name="{PRODUCT_NAME}"',
        f'--file-version={VERSION}',
        f'--product-version={VERSION}',
        f'--file-description="{PRODUCT_NAME}',
        f'--copyright="Copyright(C) {YEAR} {AUTHOR}"',
        '--output-dir=dist',
        'main.py',
    ]
elif sys.platform == "darwin":
    args = [
        'python3 -m nuitka',
        '--standalone',
        '--plugin-enable=pyside6',
        '--show-memory',
        '--show-progress',
        "--macos-create-app-bundle",
        "--assume-yes-for-download",
        "--macos-app-mode=gui",
        f"--macos-app-version={VERSION}",
        f'--macos-app-name="{PRODUCT_NAME}"',
        "--macos-app-icon=resources/logo.icns",
        f'--copyright="Copyright(C) {YEAR} {AUTHOR}"',
        '--output-dir=dist',
        '--macos-signed-app-name=com.huaqiwill.markdownmanager',
        'main.py',
    ]
else:
    args = [
        'nuitka',
        '--standalone',
        '--plugin-enable=pyside6',
        '--include-qt-plugins=platforms',
        '--assume-yes-for-downloads',
        '--show-memory',
        '--show-progress',
        '--linux-icon=resources/logo.ico',
        '--output-dir=dist',
        'main.py',
    ]


os.system(' '.join(args))
