package kr.co.aiai.dao;
import java.sql.*;

public class MyInsert {
	
	public static void main(String[] args) throws Exception {

		Class.forName("com.mysql.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python",
													"root", "python");
		Statement stmt = conn.createStatement();

		String sql = " insert into emp(e_id, e_name, sex, addr) " + 
					" values('3','3','3','3') ";

		int cnt = stmt.executeUpdate(sql);
		
		System.out.println(cnt + "개 행 insert 성공");
		
		stmt.close();
		conn.close();

	}
}
