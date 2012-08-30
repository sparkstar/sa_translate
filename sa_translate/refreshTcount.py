import sqlite3
import re

database = "sa_translate.db"

dbconn = sqlite3.connect(database)
cursor = dbconn.cursor()
#cursor.execute(query_drop)
#cursor.execute(query_create)

#dbconn.commit()

#---------------------------------------------------------#

for a in range(1,1686):
    queryStr = "select count(*) from viewjp_translateText where textNumber = " + str(a)
    cursor.execute(queryStr)
    b = cursor.fetchone()
    print b[0]
    
    queryStr = "update viewjp_text set numofText=" + str(b[0]) + " where textNumber =" + str(a)
    cursor.execute(queryStr)
    
dbconn.commit()
#---------------------------------------------------------#
