<%@page import="kr.co.aiai.dao.EmpVO"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<%
EmpVO empvo = (EmpVO)request.getAttribute("empvo");
// System.out.println(empvo);
%>

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

input[type=text] {
	width: 100px;
}
</style>
<script>
function fn_detail() {
	history.back();
}
</script>
</head>
<body>
<div>
<h1>emp delete</h1>
</div>
<form action="emp_del_act" method="post">
	<table border="1px">
	<tr>
		<td>사번</td>
		<td>
			<%=empvo.getE_id() %>
		</td>
	</tr>
	<tr>
		<td>사원명</td>
		<td>
			<%=empvo.getE_name() %>
		</td>
	</tr>
	<tr>
		<td>성별</td>
		<td>
			<%=empvo.getSex() %>
		</td>
	</tr>
	<tr>
		<td>주소</td>
		<td>
			<%=empvo.getAddr() %>
		</td>
	</tr>
	<tr>
		<td colspan="2">
			<input type="submit" value="삭제" />
			<input type="button" value="뒤로 돌아가기" onclick="fn_detail()"/>
		</td>
	</tr>
	</table>
</form>
</body>
</html>