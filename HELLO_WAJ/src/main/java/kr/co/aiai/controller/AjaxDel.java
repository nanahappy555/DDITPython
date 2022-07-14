package kr.co.aiai.controller;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

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
@WebServlet("/ajaxdel")
public class AjaxDel extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String e_id = request.getParameter("e_id");
		EmpVO pvo = new EmpVO(e_id, "", "", "");
		
		DaoEmp de = new DaoEmp();
		
		try {
			int cnt = de.delete(pvo);
			//int를 HashMap으로 바꿔서 넣어줌. int는 문제가 많아서..
			HashMap<String,String> hm = new HashMap<String, String>();
			hm.put("cnt", cnt+"");
			AjaxUtil.responseJson(response, hm);
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
