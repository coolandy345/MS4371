import sqlite3




Table_name="Modbus Registor Pool - Registor"

Base=1

名称_Up=0
名称_Up_name="名称_Up"
名称_Up_default="NULL"
名称_Up_max="NULL"
名称_Up_min="NULL"
名称_Up_comment="4文字 ascii"

名称_Down=1
名称_Down_name="名称_Down"
名称_Down_default="NULL"
名称_Down_max="NULL"
名称_Down_min="NULL"
名称_Down_comment="4文字 ascii"






実行STEP数=6
実行STEP数_name="実行STEP数"
実行STEP数_default=0
実行STEP数_max=20
実行STEP数_min=0
実行STEP数_comment="NULL"

測定雰囲気=7
測定雰囲気_name="測定雰囲気"
測定雰囲気_default=0
測定雰囲気_max=4
測定雰囲気_min=0
測定雰囲気_comment="b0:大気 b1:真空 b2:N2置換"

RT計測=8
RT計測_name="RT計測"
RT計測_default=0
RT計測_max=1
RT計測_min=0
RT計測_comment="0/1"

パターン有効=9
パターン有効_name="パターン有効"
パターン有効_default=0
パターン有効_max=1
パターン有効_min=0
パターン有効_comment="0/1"

註記=10
註記_name="註記"
註記_default="NULL"
註記_max="NULL"
註記_min="NULL"
註記_comment="NULL"

SV値=100
SV値_name="SV値"
SV値_default=0
SV値_max=800
SV値_min=0
SV値_comment="NULL"

時間_時=102
時間_時_name="時間_時"
時間_時_default=0
時間_時_max=999
時間_時_min=0
時間_時_comment="NULL"

時間_分=103
時間_分_name="時間_分"
時間_分_default=0
時間_分_max=59
時間_分_min=0
時間_分_comment="NULL"

ｷｰﾌﾟ時間=104
ｷｰﾌﾟ時間_name="キープ時間"
ｷｰﾌﾟ時間_default=0
ｷｰﾌﾟ時間_max=120
ｷｰﾌﾟ時間_min=0
ｷｰﾌﾟ時間_comment="NULL"

N2流量=105
N2流量_name="N2流量"
N2流量_default=0
N2流量_max=20
N2流量_min=0
N2流量_comment="真空時0"

マッフル_PID_No=106
マッフル_PID_No_name="マッフル_PID_No"
マッフル_PID_No_default=0
マッフル_PID_No_max=4
マッフル_PID_No_min=0
マッフル_PID_No_comment="NULL"

ヒーター_PID_No=107
ヒーター_PID_No_name="ヒーター_PID_No"
ヒーター_PID_No_default=0
ヒーター_PID_No_max=4
ヒーター_PID_No_min=0
ヒーター_PID_No_comment="NULL"

測定有=110
測定有_name="測定有"
測定有_default=0
測定有_max=1
測定有_min=0
測定有_comment="有時温度変化なし"

測定パターン=112
測定パターン_name="測定パターン"
測定パターン_default=0
測定パターン_max=20
測定パターン_min=0
測定パターン_comment="NULL"

STEP情報=119
STEP情報_name="STEP情報"
STEP情報_default=0
STEP情報_max=2
STEP情報_min=0
STEP情報_comment="0:測定外 1:END 2:測定有　END時測定無"

PID_P=0
PID_P_default=0.1
PID_P_max=3200
PID_P_min=0.1
PID_P_comment="NULL"

PID_I=1
PID_I_default=0
PID_I_max=32000
PID_I_min=0
PID_I_comment="NULL"

PID_D=2
PID_D_default=0
PID_D_max=32000
PID_D_min=0
PID_D_comment="NULL"



System_Registor_Database = sqlite3.connect('./Database and Profile/System Registor Structure Database.db')
cur = System_Registor_Database.cursor()

#Delete all table
cur.execute("DELETE FROM '{}'".format(Table_name))

for pattern_no in range(1,21):
    print("Starting process pattern NO.",pattern_no)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},'{}')".format(Table_name,Base+名称_Up,pattern_no,名称_Up_name,名称_Up_min,名称_Up_default,名称_Up_max,名称_Up_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},'{}')".format(Table_name,Base+名称_Down,pattern_no,名称_Down_name,名称_Down_min,名称_Down_default,名称_Down_max,名称_Down_comment)
    cur.execute(test)



    

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},'{}')".format(Table_name,Base+註記,pattern_no,註記_name,註記_min,註記_default,註記_max,註記_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},'{}')".format(Table_name,Base+パターン有効,pattern_no,パターン有効_name,パターン有効_min,パターン有効_default,パターン有効_max,パターン有効_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},'{}')".format(Table_name,Base+実行STEP数,pattern_no,実行STEP数_name,実行STEP数_min,実行STEP数_default,実行STEP数_max,実行STEP数_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},'{}')".format(Table_name,Base+測定雰囲気,pattern_no,測定雰囲気_name,測定雰囲気_min,測定雰囲気_default,測定雰囲気_max,測定雰囲気_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},'{}')".format(Table_name,Base+RT計測,pattern_no,RT計測_name,RT計測_min,RT計測_default,RT計測_max,RT計測_comment)
    cur.execute(test)

    sub_base=0
    for step in range(1,21):
        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},'{}')".format(Table_name,Base+sub_base+SV値,pattern_no,step,SV値_name,SV値_min,SV値_default,SV値_max,SV値_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},'{}')".format(Table_name,Base+sub_base+時間_時,pattern_no,step,時間_時_name,時間_時_min,時間_時_default,時間_時_max,時間_時_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},'{}')".format(Table_name,Base+sub_base+時間_分,pattern_no,step,時間_分_name,時間_分_min,時間_分_default,時間_分_max,時間_分_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},'{}')".format(Table_name,Base+sub_base+ｷｰﾌﾟ時間,pattern_no,step,ｷｰﾌﾟ時間_name,ｷｰﾌﾟ時間_min,ｷｰﾌﾟ時間_default,ｷｰﾌﾟ時間_max,ｷｰﾌﾟ時間_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},'{}')".format(Table_name,Base+sub_base+N2流量,pattern_no,step,N2流量_name,N2流量_min,N2流量_default,N2流量_max,N2流量_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},'{}')".format(Table_name,Base+sub_base+マッフル_PID_No,pattern_no,step,マッフル_PID_No_name,マッフル_PID_No_min,マッフル_PID_No_default,マッフル_PID_No_max,マッフル_PID_No_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},'{}')".format(Table_name,Base+sub_base+ヒーター_PID_No,pattern_no,step,ヒーター_PID_No_name,ヒーター_PID_No_min,ヒーター_PID_No_default,ヒーター_PID_No_max,ヒーター_PID_No_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},'{}')".format(Table_name,Base+sub_base+測定有,pattern_no,step,測定有_name,測定有_min,測定有_default,測定有_max,測定有_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},'{}')".format(Table_name,Base+sub_base+測定パターン,pattern_no,step,測定パターン_name,測定パターン_min,測定パターン_default,測定パターン_max,測定パターン_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},'{}')".format(Table_name,Base+sub_base+STEP情報,pattern_no,step,STEP情報_name,STEP情報_min,STEP情報_default,STEP情報_max,STEP情報_comment)
        cur.execute(test)

        sub_base+=20

    Base+=500

Base=10000
for pid_no in range(0,5):

    test="INSERT INTO '{}' values({}, 'PID_No_{}_P',{},{},{},'{}')".format(Table_name,Base+PID_P,pid_no,PID_P_min,PID_P_default,PID_P_max,PID_P_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PID_No_{}_I',{},{},{},'{}')".format(Table_name,Base+PID_I,pid_no,PID_I_min,PID_I_default,PID_I_max,PID_I_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PID_No_{}_D',{},{},{},'{}')".format(Table_name,Base+PID_D,pid_no,PID_D_min,PID_D_default,PID_D_max,PID_D_comment)
    cur.execute(test)

    Base+=3

test="INSERT INTO '{}' values({}, '温度PV値',{},{},{},'{}')".format(Table_name,10019,-100,0,999,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '実行PTN　No.',{},{},{},'{}')".format(Table_name,10020,1,1,20,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '実行STEP　No.',{},{},{},'{}')".format(Table_name,10021,1,1,20,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, 'STEP実行経過時間（L)',{},{},{},'{}')".format(Table_name,10022,"NULL","NULL","NULL","NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, 'STEP実行経過時間（H)',{},{},{},'{}')".format(Table_name,10023,"NULL","NULL","NULL","NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '有効PTN総数',{},{},{},'{}')".format(Table_name,10024,0,0,20,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, 'フォーカスPTN番号',{},{},{},'{}')".format(Table_name,10025,0,0,20,"NULL")
cur.execute(test)


System_Registor_Database.commit()

System_Registor_Database.close()