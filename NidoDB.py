#*******CONNECTION SETUP******************
import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', password='nido', database='nidoran')

try:
    print(con.connection_id)

except:
    print("Connection Failure")

#Instatiation of Cursor object
#curobj = con.cursor()

#************CREATE OPERATIONS************************
#Database creation
#q1 = "create database nidoran"
#curobj.execute(q1)

#Table creation
#q2 = 'create table Transcript(courseid integer(4), course varchar(20), gpa float)'
#curobj.execute(q2)

#Data creation
#q3 = 'insert into Transcript values(%s, %s, %s)'
#rec1 = (100914,'Data Science',1.7)
#rec2 = (100952,'Fuzzy Systems',2.0)
#rec3 = (100904,'Distributed Systems',3.1)

#whitelist = [(100876,'Deep Learning',2.0),(100872,'Visual Analytics',1.3),(100801,'Data Mining',3.3)]
#curobj.execute(q3, rec1)
#curobj.execute(q3, rec2)
#curobj.execute(q3, rec3)
#curobj.executemany(q3, whitelist)
#con.commit()

#***********READ OPERATIONS******************************
#q4 = 'select * from transcript'
#curobj.execute(q4)
#res = curobj.fetchall()
#for val in res:
 #   print(val)

#*************UPDTAE OPERATIONS**************************
#q5 = 'update transcript set gpa=2 where course="Data Science"'
#curobj.execute(q5)
#con.commit()

#*************DELETE OPERATIONS**************************
#q6 = "delete from transcript where course='Data Science'"
#curobj.execute(q6)
#con.commit()
