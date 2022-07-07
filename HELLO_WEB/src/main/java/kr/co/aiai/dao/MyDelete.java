package kr.co.aiai.dao;
import java.sql.*;

public class MyDelete {
	
	public static void main(String[] args) throws Exception {

		Class.forName("com.mysql.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python",
													"root", "python");

		String sql = " delete from emp where e_id = ?"; 

		PreparedStatement pstmt = conn.prepareStatement(sql);
		pstmt.setInt(1, 3);
		

		int cnt = pstmt.executeUpdate();
		
		System.out.println(cnt + "개 행 delete 성공");
		
		pstmt.close();
		conn.close();

	}
}
