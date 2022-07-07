package kr.co.aiai.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

public class DaoEmp {
	
	public EmpVO getOne(EmpVO pvo) throws Exception{

		EmpVO rvo = new EmpVO();
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python", "root", "python");
		Statement stmt = conn.createStatement();
		String sql = "";
		sql += "select e_id,e_name,sex,addr from emp ";
		sql += "where e_id = '"+pvo.getE_id()+"' ";

		ResultSet rs = stmt.executeQuery(sql);

		while (rs.next()) {
			String e_id = rs.getString("e_id");
			String e_name = rs.getString("e_name");
			String sex = rs.getString("sex");
			String addr = rs.getString("addr");
			rvo.setE_id(e_id);
			rvo.setE_name(e_name);
			rvo.setSex(sex);
			rvo.setAddr(addr);
		}

		rs.close();
		stmt.close();
		conn.close();
		
		return rvo;
	}

	public ArrayList<EmpVO> getlist() throws Exception{
		
		ArrayList<EmpVO> list = new ArrayList<EmpVO>();
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python", "root", "python");
		Statement stmt = conn.createStatement();
		String sql = "select * from emp";

		ResultSet rs = stmt.executeQuery(sql);

		while (rs.next()) {
			String e_id = rs.getString("e_id");
			String e_name = rs.getString("e_name");
			String sex = rs.getString("sex");
			String addr = rs.getString("addr");
			EmpVO temp = new EmpVO();
			temp.setE_id(e_id);
			temp.setE_name(e_name);
			temp.setSex(sex);
			temp.setAddr(addr);
			list.add(temp);

		}

		rs.close();
		stmt.close();
		conn.close();
		
		return list;
		
	}
	
	public int insertEmp(EmpVO vo) throws Exception{
		Class.forName("com.mysql.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python",
													"root", "python");
		Statement stmt = conn.createStatement();

		String sql = "";
		sql += "insert into emp ";
		sql += "(e_name,sex,addr) ";
		sql += "values ";
		sql += "('" + vo.getE_name() + "','" + vo.getSex() + "','" + vo.getAddr() + "')";

		int cnt = stmt.executeUpdate(sql);
		
		
		stmt.close();
		conn.close();

		return cnt;
	}
	
	public int updateEmp(EmpVO vo) throws Exception{
		Class.forName("com.mysql.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python",
				"root", "python");
		Statement stmt = conn.createStatement();
		
		String sql = " update emp "
				+ " set e_name= '" + vo.getE_name() + "',"
				+ " sex= '" + vo.getSex() + "',"
				+ " addr= '" + vo.getAddr()+ "'"
				+ " where e_id= '" + vo.getE_id()+ "'";
		
		
		
		int cnt = stmt.executeUpdate(sql);
		
		
		stmt.close();
		conn.close();
		
		return cnt;
		
	}
	
	public int deleteEmp(EmpVO vo) throws Exception{
		Class.forName("com.mysql.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python",
				"root", "python");
		Statement stmt = conn.createStatement();
		
		String sql = " delete from emp "
				+ " where e_id= " + vo.getE_id();
		
		int cnt = stmt.executeUpdate(sql);
		
		
		stmt.close();
		conn.close();
		
		return cnt;
		
	}
	
	public static void main(String[] args) throws Exception {
		DaoEmp de = new DaoEmp();
		int cnt = de.insertEmp(new EmpVO("2", "2", "2", "2"));
		int cnt2 = de.insertEmp(new EmpVO("3", "3", "3", "3"));
//		int cnt = de.updateEmp(new EmpVO("2", "4", "4", "4"));
//		int cnt = de.deleteEmp(new EmpVO("2", "4", "4", "4"));
//		EmpVO vo = de.getOne(new EmpVO("1", "1", "1", "1"));
//		System.out.println("vo : " + vo);
//		
		System.out.println("cnt: " + cnt);
		System.out.println("cnt2: " + cnt2);
//		ArrayList<EmpVO> list = de.getlist();
//		for(int i=0;i<list.size();i++) {
//			EmpVO imsi = list.get(i);
//			System.out.println(imsi.getE_name());
//		}
		
		
		
	}
}
