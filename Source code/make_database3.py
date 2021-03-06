import sqlite3



System_Registor_Database = sqlite3.connect('./Database and Profile/System Registor Structure Database.db')
cur = System_Registor_Database.cursor()

Table_name="System memory"
#Delete table
cur.execute("DELETE FROM '{}'".format(Table_name))

text="INSERT INTO '{}' values('年度','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)
text="INSERT INTO '{}' values('評価試験','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('依頼試験','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('依頼測定番号','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('依頼元','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('依頼者','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('試料名称','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('材料','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('主電極径(mm)','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('ガード電極の内径(mm)','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('試料の厚さ(mm)','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('Ethernet conneciton','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('GPIB USB conneciton','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('2635B GPIB address','{}','{}')".format(Table_name,24,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('2635B connection','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('2657A GPIB address','{}','{}')".format(Table_name,26,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('2657A connection','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('choose_Pattern','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('Main_FolderPath','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('Auto_Measurement_status','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('Manual_Measurement_Active','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('Manual_Measurement_Ready','{}','{}')".format(Table_name,"一回測定","NULL")
cur.execute(text)

text="INSERT INTO '{}' values('Manual_Measurement_Mode','{}','{}')".format(Table_name,"Single","NULL")
cur.execute(text)

text="INSERT INTO '{}' values('Manual_Measurement_Pattern_Number','{}','{}')".format(Table_name,"0","NULL")
cur.execute(text)

text="INSERT INTO '{}' values('Manual_Measurement_trigger','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('Manual_Measurement_Voltage','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('Manual_Measurement_Single_Mode','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('Noise_Measurement_Active','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('Noise_Measurement_Voltage','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('Noise_Measurement_Time','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

text="INSERT INTO '{}' values('Noise_Measurement_Current','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)    

text="INSERT INTO '{}' values('AvgHelper_Record_Enabled','{}','{}')".format(Table_name,0,"NULL")
cur.execute(text)

for index in range(1,9):
    text="INSERT INTO '{}' values('AvgHelper_Value_{}','{}','{}')".format(Table_name,index,0,"NULL")
    cur.execute(text)

for index in range(1,9):
    text="INSERT INTO '{}' values('AvgHelper_Enable_{}','{}','{}')".format(Table_name,index,0,"NULL")
    cur.execute(text)

System_Registor_Database.commit()