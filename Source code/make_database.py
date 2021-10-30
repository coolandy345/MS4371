import sqlite3




Table_name="Modbus Registor Pool - Registor"

Base=0

名称_0=0
名称_0_name="名称_0"
名称_0_default=0
名称_0_max=65535
名称_0_min=0
名称_0_comment="2文字 ascii"

名称_1=1
名称_1_name="名称_1"
名称_1_default=0
名称_1_max=65535
名称_1_min=0
名称_1_comment="2文字 ascii"

名称_2=2
名称_2_name="名称_2"
名称_2_default=0
名称_2_max=65535
名称_2_min=0
名称_2_comment="2文字 ascii"

名称_3=3
名称_3_name="名称_3"
名称_3_default=0
名称_3_max=65535
名称_3_min=0
名称_3_comment="2文字 ascii"






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

運転総時間=11
運転総時間_name="運転総時間"
運転総時間_default=0
運転総時間_max="NULL"
運転総時間_min="NULL"
運転総時間_comment="Hour"

実行STEP数=12
実行STEP数_name="実行STEP数"
実行STEP数_default=0
実行STEP数_max=20
実行STEP数_min=0
実行STEP数_comment="NULL"

測定雰囲気=13
測定雰囲気_name="測定雰囲気"
測定雰囲気_default=0
測定雰囲気_max=4
測定雰囲気_min=0
測定雰囲気_comment="b0:大気 b1:真空 b2:N2置換"

RT計測=14
RT計測_name="RT計測"
RT計測_default=0
RT計測_max=1
RT計測_min=0
RT計測_comment="0/1"

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

ステップ所要時間=114
ステップ所要時間_name="ステップ所要時間"
ステップ所要時間_default=0
ステップ所要時間_max="NULL"
ステップ所要時間_min="NULL"
ステップ所要時間_comment="Hour"

ステップ累計時間=115
ステップ累計時間_name="ステップ累計時間"
ステップ累計時間_default=0
ステップ累計時間_max="NULL"
ステップ累計時間_min="NULL"
ステップ累計時間_comment="Hour"

STEP種類=118
STEP種類_name="STEP種類"
STEP種類_default=0
STEP種類_max=2
STEP種類_min=0
STEP種類_comment="0:測定外 1:END 2:測定有 END時測定無"

STEP情報=119
STEP情報_name="STEP情報"
STEP情報_default=0
STEP情報_max=2
STEP情報_min=0
STEP情報_comment="0:測定外 1:END 2:測定有 END時測定無"

PID_P=0
PID_P_default=1
PID_P_max=32000
PID_P_min=1
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

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+名称_0,pattern_no,名称_0_name,名称_0_min,名称_0_default,名称_0_max,名称_0_default,0,名称_0_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+名称_1,pattern_no,名称_1_name,名称_1_min,名称_1_default,名称_1_max,名称_1_default,0,名称_1_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+名称_2,pattern_no,名称_2_name,名称_2_min,名称_2_default,名称_2_max,名称_2_default,0,名称_2_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+名称_3,pattern_no,名称_3_name,名称_3_min,名称_3_default,名称_3_max,名称_3_default,0,名称_3_comment)
    cur.execute(test)

    

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+パターン有効,pattern_no,パターン有効_name,パターン有効_min,パターン有効_default,パターン有効_max,パターン有効_default,0,パターン有効_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+実行STEP数,pattern_no,実行STEP数_name,実行STEP数_min,実行STEP数_default,実行STEP数_max,実行STEP数_default,0,実行STEP数_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+測定雰囲気,pattern_no,測定雰囲気_name,測定雰囲気_min,測定雰囲気_default,測定雰囲気_max,測定雰囲気_default,0,測定雰囲気_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+RT計測,pattern_no,RT計測_name,RT計測_min,RT計測_default,RT計測_max,RT計測_default,0,RT計測_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+註記,pattern_no,註記_name,註記_min,註記_default,註記_max,註記_default,0,註記_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+運転総時間,pattern_no,運転総時間_name,運転総時間_min,運転総時間_default,運転総時間_max,運転総時間_default,0,運転総時間_comment)
    cur.execute(test)

    sub_base=0
    for step in range(1,21):
        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+sub_base+SV値,pattern_no,step,SV値_name,SV値_min,SV値_default,SV値_max,SV値_default,0,SV値_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+sub_base+時間_時,pattern_no,step,時間_時_name,時間_時_min,時間_時_default,時間_時_max,時間_時_default,0,時間_時_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+sub_base+時間_分,pattern_no,step,時間_分_name,時間_分_min,時間_分_default,時間_分_max,時間_分_default,0,時間_分_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+sub_base+ｷｰﾌﾟ時間,pattern_no,step,ｷｰﾌﾟ時間_name,ｷｰﾌﾟ時間_min,ｷｰﾌﾟ時間_default,ｷｰﾌﾟ時間_max,ｷｰﾌﾟ時間_default,0,ｷｰﾌﾟ時間_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+sub_base+N2流量,pattern_no,step,N2流量_name,N2流量_min,N2流量_default,N2流量_max,N2流量_default,0,N2流量_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+sub_base+マッフル_PID_No,pattern_no,step,マッフル_PID_No_name,マッフル_PID_No_min,マッフル_PID_No_default,マッフル_PID_No_max,マッフル_PID_No_default,0,マッフル_PID_No_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+sub_base+ヒーター_PID_No,pattern_no,step,ヒーター_PID_No_name,ヒーター_PID_No_min,ヒーター_PID_No_default,ヒーター_PID_No_max,ヒーター_PID_No_default,0,ヒーター_PID_No_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+sub_base+測定有,pattern_no,step,測定有_name,測定有_min,測定有_default,測定有_max,測定有_default,0,測定有_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+sub_base+測定パターン,pattern_no,step,測定パターン_name,測定パターン_min,測定パターン_default,測定パターン_max,測定パターン_default,0,測定パターン_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+sub_base+ステップ所要時間,pattern_no,step,ステップ所要時間_name,ステップ所要時間_min,ステップ所要時間_default,ステップ所要時間_max,ステップ所要時間_default,0,ステップ所要時間_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+sub_base+ステップ累計時間,pattern_no,step,ステップ累計時間_name,ステップ累計時間_min,ステップ累計時間_default,ステップ累計時間_max,ステップ累計時間_default,0,ステップ累計時間_comment)
        cur.execute(test)




        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+sub_base+STEP種類,pattern_no,step,STEP種類_name,STEP種類_min,STEP種類_default,STEP種類_max,STEP種類_default,0,STEP種類_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},{},{},'{}')".format(Table_name,Base+sub_base+STEP情報,pattern_no,step,STEP情報_name,STEP情報_min,STEP情報_default,STEP情報_max,STEP情報_default,0,STEP情報_comment)
        cur.execute(test)

        sub_base+=20

    Base+=500


Base=10000
for pid_no in range(0,5):

    test="INSERT INTO '{}' values({}, 'PID_No_{}_P',{},{},{},{},{},'{}')".format(Table_name,Base+PID_P,pid_no,PID_P_min,PID_P_default,PID_P_max,PID_P_default,0,PID_P_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PID_No_{}_I',{},{},{},{},{},'{}')".format(Table_name,Base+PID_I,pid_no,PID_I_min,PID_I_default,PID_I_max,PID_I_default,0,PID_I_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PID_No_{}_D',{},{},{},{},{},'{}')".format(Table_name,Base+PID_D,pid_no,PID_D_min,PID_D_default,PID_D_max,PID_D_default,0,PID_D_comment)
    cur.execute(test)

    Base+=3

test="INSERT INTO '{}' values({}, '現在電圧値',{},{},{},{},{},'{}')".format(Table_name,10016,"NULL",0,"NULL",0,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '現在電流値',{},{},{},{},{},'{}')".format(Table_name,10017,"NULL",0,"NULL",0,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '現在抵抗値',{},{},{},{},{},'{}')".format(Table_name,10018,"NULL",0,"NULL",0,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '温度PV値',{},{},{},{},{},'{}')".format(Table_name,10019,"NULL",0,"NULL",0,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '実行PTN No.',{},{},{},{},{},'{}')".format(Table_name,10020,1,1,20,1,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '実行STEP No.',{},{},{},{},{},'{}')".format(Table_name,10021,1,1,20,1,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, 'STEP実行経過時間（L)',{},{},{},{},{},'{}')".format(Table_name,10022,0,0,65535,0,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, 'STEP実行経過時間（H)',{},{},{},{},{},'{}')".format(Table_name,10023,0,0,65535,0,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '有効PTN総数',{},{},{},{},{},'{}')".format(Table_name,10024,0,0,20,0,0,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, 'フォーカスPTN番号',{},{},{},{},{},'{}')".format(Table_name,10025,0,0,20,0,0,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, 'PLC Boot',{},{},{},{},{},'{}')".format(Table_name,10100,0,0,1,0,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '運転可',{},{},{},{},{},'{}')".format(Table_name,10101,0,0,1,0,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '停止中',{},{},{},{},{},'{}')".format(Table_name,10102,0,0,1,0,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '真空置換中',{},{},{},{},{},'{}')".format(Table_name,10103,0,0,1,0,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '昇温中',{},{},{},{},{},'{}')".format(Table_name,10104,0,0,1,0,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '温度ｷｰﾌﾟ中',{},{},{},{},{},'{}')".format(Table_name,10105,0,0,1,0,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '測定中',{},{},{},{},{},'{}')".format(Table_name,10106,0,0,1,0,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '運転終了',{},{},{},{},{},'{}')".format(Table_name,10107,0,0,1,0,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, 'PLC警報',{},{},{},{},{},'{}')".format(Table_name,10108,0,0,1,0,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '測定可',{},{},{},{},{},'{}')".format(Table_name,10109,0,0,1,0,1,"放電による測定禁止エリアがあるため")
cur.execute(test)

test="INSERT INTO '{}' values({}, '測定開始',{},{},{},{},{},'{}')".format(Table_name,10120,0,0,1,0,1,"エッジ(PC側でRST)")
cur.execute(test)

test="INSERT INTO '{}' values({}, 'PC Boot',{},{},{},{},{},'{}')".format(Table_name,10150,0,0,1,0,1,"PC側常に1にする")
cur.execute(test)

test="INSERT INTO '{}' values({}, 'リモート',{},{},{},{},{},'{}')".format(Table_name,10151,0,0,1,0,1,"リモートモードに入ると1にする")
cur.execute(test)

test="INSERT INTO '{}' values({}, 'PC警報',{},{},{},{},{},'{}')".format(Table_name,10152,0,0,1,0,1,"NULL")
cur.execute(test)

test="INSERT INTO '{}' values({}, '変更連絡',{},{},{},{},{},'{}')".format(Table_name,10160,0,0,1,0,1,"エッジ(PLC側でRST) PC側でデータ変更した場合ONさせる")
cur.execute(test)

test="INSERT INTO '{}' values({}, '運転開始',{},{},{},{},{},'{}')".format(Table_name,10170,0,0,1,0,1,"エッジ(PLC側でRST)")
cur.execute(test)

test="INSERT INTO '{}' values({}, '測定終了',{},{},{},{},{},'{}')".format(Table_name,10171,0,0,1,0,1,"エッジ(PLC側でRST)")
cur.execute(test)

test="INSERT INTO '{}' values({}, '実行PTN No.変更',{},{},{},{},{},'{}')".format(Table_name,10172,0,0,1,0,1,"エッジ(PLC側でRST)")
cur.execute(test)

test="INSERT INTO '{}' values({}, '大気圧',{},{},{},{},{},'{}')".format(Table_name,10173,0,0,1,0,1,"エッジ(PLC側でRST)")
cur.execute(test)



#test="INSERT INTO '{}' values({}, '変更レジスター番号',{},{},{},{},{},'{}')".format(Table_name,10191,0,0,65535,0,1,"変更したレジスター番号はここ記入")
#cur.execute(test)


System_Registor_Database.commit()
System_Registor_Database.close()