package kr.co.aiai.controller;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.co.aiai.dao.DaoEmp;
import kr.co.aiai.dao.EmpVO;

/**
 * Servlet implementation class EmpList
 */
@WebServlet("/emp_list")
public class EmpList extends HttpServlet {

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		DaoEmp dao = new DaoEmp();
		ArrayList<EmpVO> emplist = null;
		try {
			
			emplist = dao.getlist();
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		request.setAttribute("emplist", emplist);
		
		RequestDispatcher rd = request.getRequestDispatcher("/emp_list.jsp");
		rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
