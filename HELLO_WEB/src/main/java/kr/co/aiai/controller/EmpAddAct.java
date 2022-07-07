package kr.co.aiai.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.co.aiai.dao.DaoEmp;
import kr.co.aiai.dao.EmpVO;

/**
 * Servlet implementation class EmpModAct
 */
@WebServlet("/emp_del_act")
public class EmpAddAct extends HttpServlet {
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		request.setCharacterEncoding("utf-8");
		String e_id = request.getParameter("e_id");
		
		DaoEmp dao = new DaoEmp();
		int cnt = -1;
		try {
			
			cnt = dao.deleteEmp(new EmpVO(e_id,"","",""));
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		request.setAttribute("cnt", cnt);
//		System.out.println("cnt : " + cnt);
		
		RequestDispatcher rd = request.getRequestDispatcher("/emp_del_act.jsp");
		rd.forward(request, response);

	}

	//post는 get을 호출해서 실행하기 때문에 get에 작성하면 됨..
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
