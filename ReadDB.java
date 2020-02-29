package com.DataBase;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import org.apache.commons.lang3.SystemUtils;
import org.apache.poi.util.SystemOutLogger;

public class ReadDBFile {

	static Object[][] obj ;
	
	public static void main(String[] args) throws ClassNotFoundException, SQLException{
		System.out.println("DB");
		ReadDBFile rdb = new ReadDBFile();
		obj = rdb.readDB();
		for (int i = 0; i < obj.length; i++) {
			for (int j = 0; j < obj[i].length; j++) {
				System.out.print(obj[i][j] + " ");
			}
			System.out.println("");
		}		
		
	}
	
	
	public Object[][] readDB() throws ClassNotFoundException, SQLException{
		
		Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");  
		String connectionUrl = "jdbc:sqlserver://localhost;DatabaseName=loginDB;integratedSecurity=true";
		
		Connection con = DriverManager.getConnection(connectionUrl,"**","*******");  
		Statement stmt=con.createStatement(); 
		ResultSet rs=stmt.executeQuery("select * from login"); 
		
		int i =0;
		int j =0;
		obj = new Object[3][2];
		
		while(rs.next()){  
		//	System.out.println(rs.getInt(1)+" "+rs.getString(2)+" "+rs.getString(3)); 			
			obj[i][j]= rs.getString(2);			
		//	System.out.println("col1:"+obj[i][j]);
			j++;
			obj[i][j]=rs.getString(3);
		//	System.out.println("col2:"+obj[i][j]);
			i++;
			j=0;
		}  
		con.close();

		return obj;
	}
	
	public void setupDB(){
		
	}
}
