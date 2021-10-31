import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='infoaeropuertos'
)


cursor = connection.cursor()
# sql = "INSERT INTO aeropuertos(id,ident,type,name,elevation_ft,municipality,iata_code,score) VALUES(39340,'SHCC','heliport','Clinica Las Condes Heliport',2461,'Santiago','',25)"
# sql2 = "INSERT INTO aeropuertos(id,ident,type,name,elevation_ft,municipality,iata_code,score) VALUES(39379,'SHMA','heliport','Clinica Santa Maria Heliport',2028,'Santiago','',25)"
# sql3 = "INSERT INTO aeropuertos(id,ident,type,name,elevation_ft,municipality,iata_code,score) VALUES(39390,'SHPT','heliport','Portillo Heliport',9000,'Los Andes','',25)"
# print(cursor.execute(sql))
# print(cursor.execute(sql2))
# print(cursor.execute(sql3))

sql_select = "select name,type,municipality,elevation_ft from aeropuertos where elevation_ft>5000"
cursor.execute(sql_select)
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.commit()