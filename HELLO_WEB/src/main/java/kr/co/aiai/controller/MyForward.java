package kr.co.aiai.controller;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.co.aiai.dao.EmpVO;

@WebServlet("/myforward")
public class MyForward extends HttpServlet {

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		String a = "999";
		request.setAttribute("a", a); //a라는 방에 999를 넣어줌
		
		ArrayList<EmpVO> list = new ArrayList<EmpVO>();
		list.add(new EmpVO("1","1","1","1"));
		list.add(new EmpVO("2","2","2","2"));
		request.setAttribute("list",list);
		
		RequestDispatcher rd = request.getRequestDispatcher("/myforward.jsp");
		rd.forward(request, response);
		
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
