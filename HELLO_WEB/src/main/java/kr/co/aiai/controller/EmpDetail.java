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

@WebServlet("/emp_detail")
public class EmpDetail extends HttpServlet {
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		String e_id = request.getParameter("e_id"); //parameter로 e_id를 받아옴 // e_id=<%=temp.getE_id()
		DaoEmp dao = new DaoEmp();
		EmpVO vo = null;
		try {
			
			vo = dao.getOne(new EmpVO(e_id,"","",""));
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		request.setAttribute("empvo", vo);
		
		RequestDispatcher rd = request.getRequestDispatcher("/emp_detail.jsp");
		rd.forward(request, response);

	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
