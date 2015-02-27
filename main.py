import psycopg2
from PyQt4.QtGui import * 
from PyQt4.QtSql import * 
from PyQt4.QtCore import * 
import sys


def main():  
    app 	= QApplication(sys.argv)
    table 	= QTableWidget()
    db 		= QSqlDatabase.addDatabase("QPSQL")
    db.setHostName("localhost")
    db.setDatabaseName("megatron")
    db.setUserName("postgres")
    db.setPassword("admin") 
    
    if (db.open()==False):     
      QMessageBox.critical(None, "Database Error",
			    db.lastError().text())   
			    
    query = QSqlQuery ("SELECT * FROM ACCOUNT_ACCOUNT")   
    
    table.setColumnCount(query.record().count())
    table.setRowCount(query.size())
    
    index=0
    while (query.next()):
	table.setItem(index,0,QTableWidgetItem(query.value(0).toString()))
	table.setItem(index,1,QTableWidgetItem(query.value(1).toString()))
        table.setItem(index,2,QTableWidgetItem(query.value(2).toString()))		
	index = index+1
    
    table.show()
    
    return app.exec_()
if __name__ == '__main__':
  main()
