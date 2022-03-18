
from sqlite3 import connect
from shutil import copyfile
from os.path import exists,abspath

database_path=abspath('../../Database and Profile/System Registor Structure Database.db')
backup_database_path=abspath('../../Database and Profile/System Registor Structure Database backup.db')

file_exists = exists(database_path)

print("MS4371 高温抵抗測定用電気炉　データベース更新工具")
print("Version 1.0")


print("")
print("データベースを検索します．．．",end="")

if not file_exists:
    print("[失敗]")
    print("データベース存在しません、プログラムを再インストールをお願いします。")

else:
    print("[成功]")
    print("")
    print("データベース検査開始,お待ちください．．．")


    Table_name="System memory"
    System_Registor_Database = connect(database_path)
    cur = System_Registor_Database.cursor()

    text="SELECT * FROM '{}' WHERE Registor_Name = '測定異常コード'".format(Table_name)
    return_message=cur.execute(text)

    already_have_target=False
    for item in return_message:
        already_have_target=True

    dialog_error=False

    if already_have_target:
        print("このデータベースは修正不要です。")
    else:
        user_message=input("このデータベースは修正必要です。修正開始しますか？ \"yes\" or \"no\"を入力ください。")
        print("")

        if user_message.lower()=="yes":

            user_message=input("修正開始前、データベースをバックアップしますか？\"yes\" or \"no\"を入力ください。")
            print("")
            if user_message.lower()=="yes":
                print("データベースをバックアップします．．．",end="")

                copyfile(database_path,backup_database_path)

                print("[成功]")
                print("バックアップは完成です。")

            elif user_message.lower()=="no":
                print("バックアップ動作は実行しません。")

            else:
                print("\"yes\" , \"no\"以外の指令は入力されました。")
                dialog_error=True

            if not dialog_error:
                print("修正開始します．．．",end="")

                text="INSERT INTO '{}' values('測定異常コード','{}','{}')".format(Table_name,0,"NULL")
                cur.execute(text)
                System_Registor_Database.commit()

                print("[成功]")


        elif user_message.lower()=="no":
            pass
        else:
            print("\"yes\" \"no\" 以外の指令は入力されました。")

    System_Registor_Database.close()


print("この工具は終了します。")
input("修正工具を終了する為に、\"ENTERキー\"を押してください．．．")