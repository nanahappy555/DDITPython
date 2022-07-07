<%@page import="java.util.ArrayList"%>
<%@page import="kr.co.aiai.dao.*"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
table {
	border: 5px dashed skyblue;
	border-collapse: collapse;
}
</style>
</head>
<body>

myforward jsp 

<%
	String a = (String)request.getAttribute("a");
	ArrayList<EmpVO> list = (ArrayList<EmpVO>)request.getAttribute("list");
	//System.out.println(list); //콘솔창에 찍힘
%>

<%=a %> <br/>

<table border="1px">
<tr>
	<th>사번</th>
	<th>사원명</th>
	<th>성별</th>
	<th>주소</th>
</tr>
<%for(int i=0; i<list.size(); i++){%>
<% EmpVO temp = (EmpVO)list.get(i); %>
	<tr>
		<td><%=temp.getE_id() %></td>
		<td><%=temp.getE_name() %></td>
		<td><%=temp.getSex() %></td>
		<td><%=temp.getAddr() %></td>
	</tr>
<%} %>
</table>

</body>
</html>