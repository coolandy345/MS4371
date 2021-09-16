import sqlite3

Table_name="Test Pattern"

Base=0

名称=0
名称_name="名称"
名称_default="NULL"
名称_max="NULL"
名称_min="NULL"
名称_comment="8文字"

註記=1
註記_name="註記"
註記_default="NULL"
註記_max="NULL"
註記_min="NULL"
註記_comment="NULL"

パターン有効=2
パターン有効_name="パターン有効"
パターン有効_default=0
パターン有効_max=1
パターン有効_min=0
パターン有効_comment="0/1"


実行STEP数=3
実行STEP数_name="実行STEP数"
実行STEP数_default=0
実行STEP数_max=8
実行STEP数_min=0
実行STEP数_comment="NULL"

測定時間=4
測定時間_name="測定時間"
測定時間_default=0
測定時間_max=200
測定時間_min=1
測定時間_comment="NULL"

測定sampletime=5
測定sampletime_name="測定sampletime"
測定sampletime_default=0
測定sampletime_max=10
測定sampletime_min=0
測定sampletime_comment="NULL"

BG0測定時間=6
BG0測定時間_name="BG0測定時間"
BG0測定時間_default=0
BG0測定時間_max=200
BG0測定時間_min=0
BG0測定時間_comment="NULL"

BG測定時間=7
BG測定時間_name="BG測定時間"
BG測定時間_default=0
BG測定時間_max=200
BG測定時間_min=0
BG測定時間_comment="NULL"

BG測定sampletime=8
BG測定sampletime_name="BG測定sampletime"
BG測定sampletime_default=0
BG測定sampletime_max=10
BG測定sampletime_min=0
BG測定sampletime_comment="NULL"

電圧=9
電圧_name="電圧"
電圧_default=0
電圧_max=2000
電圧_min=-2000
電圧_comment="NULL"

STEP情報=10
STEP情報_name="STEP情報"
STEP情報_default=0
STEP情報_max=2
STEP情報_min=0
STEP情報_comment="NULL"



System_Registor_Database = sqlite3.connect('../Database and Profile/System Registor Structure Database.db')
cur = System_Registor_Database.cursor()

#Delete all table
cur.execute("DELETE FROM '{}'".format(Table_name))

for pattern_no in range(1,21):
    print("Starting process pattern NO.",pattern_no)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},'{}')".format(Table_name,Base+名称,pattern_no,名称_name,名称_min,名称_default,名称_max,名称_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},'{}')".format(Table_name,Base+註記,pattern_no,註記_name,註記_min,註記_default,註記_max,註記_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},'{}')".format(Table_name,Base+パターン有効,pattern_no,パターン有効_name,パターン有効_min,パターン有効_default,パターン有効_max,パターン有効_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},'{}')".format(Table_name,Base+実行STEP数,pattern_no,実行STEP数_name,実行STEP数_min,実行STEP数_default,実行STEP数_max,実行STEP数_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},'{}')".format(Table_name,Base+測定時間,pattern_no,測定時間_name,測定時間_min,測定時間_default,測定時間_max,測定時間_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},'{}')".format(Table_name,Base+測定sampletime,pattern_no,測定sampletime_name,測定sampletime_min,測定sampletime_default,測定sampletime_max,測定sampletime_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},'{}')".format(Table_name,Base+BG0測定時間,pattern_no,BG0測定時間_name,BG0測定時間_min,BG0測定時間_default,BG0測定時間_max,BG0測定時間_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},'{}')".format(Table_name,Base+BG測定時間,pattern_no,BG測定時間_name,BG測定時間_min,BG測定時間_default,BG測定時間_max,BG測定時間_comment)
    cur.execute(test)

    test="INSERT INTO '{}' values({}, 'PTNData_{}_{}',{},{},{},'{}')".format(Table_name,Base+BG測定sampletime,pattern_no,BG測定sampletime_name,BG測定sampletime_min,BG測定sampletime_default,BG測定sampletime_max,BG測定sampletime_comment)
    cur.execute(test)

    sub_base=0
    for step in range(1,9):
        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},'{}')".format(Table_name,Base+sub_base+電圧,pattern_no,step,電圧_name,電圧_min,電圧_default,電圧_max,電圧_comment)
        cur.execute(test)

        test="INSERT INTO '{}' values({}, 'PTNData_{}_STEP_{}_{}',{},{},{},'{}')".format(Table_name,Base+sub_base+STEP情報,pattern_no,step,STEP情報_name,STEP情報_min,STEP情報_default,STEP情報_max,STEP情報_comment)
        cur.execute(test)

        
        sub_base+=2

    Base+=25

System_Registor_Database.commit()