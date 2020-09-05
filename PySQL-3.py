import mysql.connector
import pandas as pd

con = mysql.connector.connect(host='localhost', user='root', password='nido', database='togepi',autocommit=True)

try:
    print(con.connection_id,"OK")

except:
    print("Connection Failure")

df1 = pd.read_csv('cricket_1.csv')
df2 = pd.read_csv('cricket_2.csv')

#print(df1)
#print(df2)

#Instatiation of Cursor object
curobj = con.cursor()

#************CREATE OPERATIONS************************
#Database creation
#q1 = "create database togepi"
#curobj.execute(q1)

#Table1 creation
#q2 = 'create table Cricket1(PlayerID varchar(20), PlayerName varchar(20), Runs integer, Popularity integer)'
#q2 = 'drop table Cricket1'
#curobj.execute(q2)


#Table2 creation
#q2 = 'create table Cricket2(PlayerID varchar(20), PlayerName varchar(20), Runs integer, Charisma integer)'
#q2 = 'drop table Cricket2'
#curobj.execute(q2)



'*************FOR TABLE 1***************************************'
'''
q3 = 'insert into Cricket1 values(%s,%s,%s,%s)'
i=0
while i<len(df1):
    rec=[col[i] for col in  (df1['Player_Id'],df1['Player_Name'],df1['Runs'],df1['Popularity'])]
    a=int(rec[2])
    b=int(rec[3])
    rec.append(a)
    rec.append(b)
    c=int(rec[2])
    d=int(rec[3])
    rec.remove(c)
    rec.remove(d)
    curobj.execute(q3, rec)
    print("Inserted",rec)
    i+=1
'''
'*************FOR TABLE 2***************************************'
'''
q3 = 'insert into Cricket2 values(%s,%s,%s,%s)'
i=0
while i<len(df2):
    rec=[col[i] for col in  (df2['Player_Id'],df2['Player_Name'],df2['Runs'],df2['Charisma'])]
    a=int(rec[2])
    b=int(rec[3])
    rec.append(a)
    rec.append(b)
    c=int(rec[2])
    d=int(rec[3])
    rec.remove(c)
    rec.remove(d)
    curobj.execute(q3, rec)
    print("Inserted",rec)
    i+=1
'''
'***********FIND ALL PLAYERS WHO WERE PRESENT IN TEST MATCH 1 OR MATCH 2****************'
'''
q4='select PlayerName from cricket1 union select PlayerName from cricket2'
curobj.execute(q4)
res = curobj.fetchall()
print(res)
'''
'***********FIND ALL PLAYERS FROM TEST MATCH 1 HAVING POPULARITY HIGHER THAN THE AVG POPULARITY****************'
'''
q4 = 'select PlayerName, Popularity from cricket1 where Popularity>(select avg(Popularity)from cricket1)'
curobj.execute(q4)
res = curobj.fetchall()
print(res)
'''

'**************DERIVE PLAYER ID, RUNS AND PLAYER NAME FROM TABLE 1 WHERE RUNS ARE GREATER THAN 50**********'
'''
q4='select PlayerID,PlayerName,Runs from cricket1 where Runs>50'
curobj.execute(q4)
res = curobj.fetchall()
print(res)
'''

"EXTRACT ALL COLS FROM CRICKET 1 WHERE PLAYER NAME DOES NOT END WITH 'T' (SQL WILDCARDS)"

q4="select * from cricket1 where PlayerName not like '%t'"
curobj.execute(q4)
res = curobj.fetchall()
print(res)

