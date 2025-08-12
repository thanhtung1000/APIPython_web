import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-L3PL7A87;DATABASE=danhsachsinhvien;Trusted_Connection=yes")
cursor = conn.cursor()
cursor.execute("SELECT * FROM Sinhvien")
rows = cursor.fetchall()
print(rows)
