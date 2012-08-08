import sqlite3
import re

textname = "V1_YES_CONVERT_HEXSTRING.SAT.txt"
database = "sa_translate.db"
regexpform = "3c746578743a(.*?)2c(.*?)2c(.*?)2c(.*?)2c(.*?)3e0d0a(.*?)0d0a"
query_drop = '''
drop table if exists "text";
'''
query_create = '''
create table if not exists "text" 
(
    id int primary key not null,
    textnumber int not null,
    textpos int not null,
    textpt int not null,
    unknown1 int not null,
    unknown2 int not null
);
'''

dbconn = sqlite3.connect(database)
cursor = dbconn.cursor()
cursor.execute(query_drop)
cursor.execute(query_create)

dbconn.commit()


#---------------------------------------------------------#
fp = open(textname, "r")
buffer = fp.read()
p = re.compile(regexpform)
list = p.findall(buffer)

for a in range(len(list)):
    t =  (list[a][0].decode("hex"), list[a][1].decode("hex"), list[a][2].decode("hex"), list[a][3].decode("hex"), list[a][4].decode("hex"), list[a][5])
    cursor.execute('''insert into text values(?,?,?,?,?,?)''', t)
dbconn.commit()
#---------------------------------------------------------#


