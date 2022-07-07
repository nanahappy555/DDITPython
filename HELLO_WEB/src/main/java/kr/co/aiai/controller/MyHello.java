package kr.co.aiai.controller;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class MyHello
 */
@WebServlet("/myhello")
public class MyHello extends HttpServlet {
	private static final long serialVersionUID = 1L;
    
	//out.print
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String p = request.getParameter("p");
		PrintWriter out = response.getWriter();
		out.println("hello servlet : " + p); //run on server 실행하면 출력됨                                          
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
