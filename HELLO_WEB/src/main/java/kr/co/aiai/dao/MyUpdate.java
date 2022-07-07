package kr.co.aiai.dao;
import java.sql.*;

public class MyUpdate {
	
	public static void main(String[] args) throws Exception {

		Class.forName("com.mysql.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python",
													"root", "python");

		String sql = " update emp" + 
					" set e_name=?, sex=?, addr=? " + 
					" where e_id = ? ";
		PreparedStatement pstmt = conn.prepareStatement(sql);
		pstmt.setString(1, "4");
		pstmt.setString(2, "4");
		pstmt.setString(3, "4");
		pstmt.setInt(4, 3);
		

		int cnt = pstmt.executeUpdate();
		
		System.out.println(cnt + "개 행 update 성공");
		
		pstmt.close();
		conn.close();

	}
}
