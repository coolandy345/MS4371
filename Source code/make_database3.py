import sqlite3



System_Registor_Database = sqlite3.connect('./Database and Profile/System Registor Structure Database.db')
cur = System_Registor_Database.cursor()

Table_name="Measurement Profile"
#Delete table
cur.execute("DELETE FROM '{}'".format(Table_name))

test="INSERT INTO '{}' values('年度','{}','{}')".format(Table_name,1,"NULL")
cur.execute(test)
test="INSERT INTO '{}' values('評価試験','{}','{}')".format(Table_name,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values('依頼試験','{}','{}')".format(Table_name,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values('依頼測定番号','{}','{}')".format(Table_name,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values('依頼元','{}','{}')".format(Table_name,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values('依頼者','{}','{}')".format(Table_name,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values('試料名称','{}','{}')".format(Table_name,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values('材料','{}','{}')".format(Table_name,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values('主電極径(mm)','{}','{}')".format(Table_name,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values('ガード電極の内径(mm)','{}','{}')".format(Table_name,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values('試料の厚さ(mm)','{}','{}')".format(Table_name,1,"NULL")
cur.execute(test)

#pid=["P","I","D"]
#pidname=["ヒーター","マッフル"]

#for name in pidname:
#    for number in range(1,5):
#        for K in pid:
#            test="INSERT INTO '{}' values('{}_PID設定_{}_{}','{}','{}')".format(Table_name,name,number,K,1,"NULL")
#            cur.execute(test)



System_Registor_Database.commit()