"""
A simple setup script to create an executable using PyQt5. This also
demonstrates the method for creating a Windows executable that does not have
an associated console.

Run the build process by running the command 'python setup_tool.py build'

If everything works well you should find a subdirectory in the build
subdirectory that contains the files needed to run the application
"""
import os
import shutil
from cx_Freeze import setup, Executable
#
executables = [Executable("change_database.py",icon="icon.ico",target_name="MS4371 高温抵抗測定用電気炉 データベース更新修正工具",copyright="Copyright © 2021 MOTOYAMA. All rights reserved.",shortcut_name="MS4371 高温抵抗測定用電気炉 データベース更新修正工具")]

build_exe_options={
                    "optimize": 1,
                    "silent_level":1,
                    'build_exe': './tools/database_tool'
                }

setup(
    name="MS4371 高温抵抗測定用電気炉 データベース更新修正工具",

    version="1.0",
    description="データベース更新修正工具",
    long_description="2021/12 株式会社モトヤマ 設計",
    options = {"build_exe": build_exe_options},
    executables=executables,
)


