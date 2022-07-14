package kr.co.aiai.controller;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.co.aiai.dao.DaoEmp;
import kr.co.aiai.dao.EmpVO;
import kr.co.aiai.util.AjaxUtil;

/**
 * Servlet implementation class AjaxOne
 */
@WebServlet("/ajaxone")
public class AjaxOne extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String e_id = request.getParameter("e_id");
		EmpVO pvo = new EmpVO(e_id, "", "", "");
		
		DaoEmp de = new DaoEmp();
		
		try {
			EmpVO rvo = de.getOne(pvo);
			AjaxUtil.responseJson(response, rvo);
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
