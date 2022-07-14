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

@WebServlet("/ajaxlist")
public class AjaxList extends HttpServlet {

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		DaoEmp de = new DaoEmp();
		ArrayList<EmpVO> list = null;
		try {
			list = de.getlist();
			AjaxUtil.responseJson(response, list);
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		

		
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
