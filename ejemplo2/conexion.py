from PySide6.QtSql import QSqlDatabase, QSqlQuery

db = QSqlDatabase.addDatabase("QMYSQL")
db.setHostName("localhost")
db.setDatabaseName("mi_base_de_datos")
db.setUserName("root")
db.setPassword("")

if not db.open():
    print("Error al conectar a la base de datos")
else:
    print("Conexión exitosa a la base de datos MySQL")