<%@page import="kr.co.aiai.dao.EmpVO"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
table {
	border: 2px solid olive;
	border-collapse: collapse;
	width: 200px;
	
}
</style>
<script>
function fn_add() {
	location.href = "emp_add"	
}
</script>
</head>
<body>
<%
ArrayList<EmpVO> emplist = (ArrayList<EmpVO>)request.getAttribute("emplist");
// System.out.println(emplist);
%>
<div>
<h1>emp list</h1>
</div>
<table border="1px">
<tr>
	<th>사번</th>
	<th>사원명</th>
	<th>성별</th>
	<th>주소</th>
</tr>
<%for(int i=0; i<emplist.size(); i++){%>
<% EmpVO temp = (EmpVO)emplist.get(i); %>
	<tr>
		 <!-- 파라미터 e_id=<%=temp.getE_id() %> -->
		<td><a href="emp_detail?e_id=<%=temp.getE_id() %>"><%=temp.getE_id()%></a></td>
		<td><%=temp.getE_name() %></td>
		<td><%=temp.getSex() %></td>
		<td><%=temp.getAddr() %></td>
	</tr>
<%} %>
	<tr>
		<td colspan="4"><input type="button" value="추가" onclick="fn_add()"> </td>
	</tr>
</table>
</body>
</html>