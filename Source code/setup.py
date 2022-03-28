"""
A simple setup script to create an executable using PyQt5. This also
demonstrates the method for creating a Windows executable that does not have
an associated console.

Run the build process by running the command 'python setup.py build'

If everything works well you should find a subdirectory in the build
subdirectory that contains the files needed to run the application
"""
import os
import shutil
from cx_Freeze import setup, Executable
#
executables = [Executable(  "change_database.py",
                            icon="icon.ico",
                            target_name="MS4371 高温抵抗測定用電気炉 データベース更新修正工具",
                            copyright="Copyright © 2022 MOTOYAMA. All rights reserved.",
                            shortcut_name="MS4371 高温抵抗測定用電気炉 データベース更新修正工具"
                        )
                    ]

build_exe_options={
                    "optimize": 1,
                    "silent_level":1,
                    'build_exe': './tools/database_tool'
                }

setup(
    name="MS4371 高温抵抗測定用電気炉 データベース更新修正工具",

    version="1.0",
    description="データベース更新修正工具",
    long_description="2022/03 株式会社モトヤマ 設計",
    options = {"build_exe": build_exe_options},
    executables=executables,
)



executables = [Executable("main.py",icon="icon.ico",base = "Win32GUI",target_name="MS4371 高温抵抗測定用電気炉",copyright="Copyright © 2022 MOTOYAMA. All rights reserved.",shortcut_name="MS4371 高温抵抗測定用電気炉")]

includefiles = ['error.ico', 'icon.ico', 'warning.ico', 'libusb-1.0.dll', 'gui_main','Database and Profile','tools','取説資料',"README.md"]

build_exe_options={
                    "optimize": 1,
                    "include_files":includefiles,
                    "silent_level":1,
                    'build_exe': '../Application/execute file'
                }

setup(
    name="MS4371 高温抵抗測定用電気炉",

    version="1.7.1",
    description="MVC210100464 - 高温抵抗測定用電気炉",
    long_description="2022/03 株式会社モトヤマ 設計",
    options = {"build_exe": build_exe_options},
    executables=executables,
)

delete_folder_path=[
    "../Application/execute file\gui_main\.vs",
    "../Application/execute file\gui_main\__pycache__",
    "../Application/execute file\gui_main\.gitignore",
]

for path in delete_folder_path:
    try:
        shutil.rmtree(path)
    except:
        pass


main_dir = "../Application/execute file\gui_main"
folders = os.listdir(main_dir)

for (dirname, dirs, files) in os.walk(main_dir):

    for file in files:
        path = os.path.join(dirname,file)
        if file.endswith('.py'):
            os.remove(path)

        if file.endswith('.ui'):
            os.remove(path)

for times in range(0,10):
    for (dirname, dirs, files) in os.walk(main_dir):
        if len(os.listdir(dirname)) == 0: # Check if the folder is empty
            shutil.rmtree(dirname) # If so, delete it


