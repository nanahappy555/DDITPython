<%@page import="kr.co.aiai.dao.EmpVO"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<%
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
function fn_list() {
	location.href = "emp_list";
}
</script>
</head>
<body>
<div>
<h1>emp add</h1>
</div>
<form action="emp_add_act" method="post">
	<table border="1px">
	<tr>
		<td>사번</td>
		<td>
			자동생성
		</td>
	</tr>
	<tr>
		<td>사원명</td>
		<td>
			<input type="text" name="e_name" />
		</td>
	</tr>
	<tr>
		<td>성별</td>
		<td>
			<input type="text" name="sex" />
		</td>
	</tr>
	<tr>
		<td>주소</td>
		<td>
			<input type="text" name="addr" />
		</td>
	</tr>
	<tr>
		<td colspan="2">
			<input type="submit" value="실행" />
			<input type="button" value="뒤로 돌아가기" onclick="fn_list()"/>
		</td>
	</tr>
	</table>
</form>
</body>
</html>