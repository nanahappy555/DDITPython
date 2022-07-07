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
</style>
<script>
function fn_list() {
	location.href = "emp_list"	
}
function fn_mod() {
	location.href = "emp_mod?e_id=" + "<%=empvo.getE_id() %>";	
}
function fn_del() {
	let flag = confirm("한번 지워진 데이터는 복구가 불가합니다.\n그래도 삭제하시렵니까?");
	if(!flag){
		return;
	}
	location.href = "emp_del_act?e_id=" + "<%=empvo.getE_id() %>";	
}
</script>
</head>
<body>
<div>
<h1>emp detail</h1>
</div>

<table border="1px">
<tr>
	<td>사번</td>
	<td><%=empvo.getE_id() %></td>
</tr>
<tr>
	<td>사원명</td>
	<td><%=empvo.getE_name() %></td>
</tr>
<tr>
	<td>성별</td>
	<td><%=empvo.getSex() %></td>
</tr>
<tr>
	<td>주소</td>
	<td><%=empvo.getAddr() %></td>
</tr>
<tr>
	<td colspan="2">
		<input type="button" value="목록" onclick="fn_list()" />
		<input type="button" value="수정" onclick="fn_mod()" />
		<input type="button" value="삭제" onclick="fn_del()" />
	</td>
</tr>
</table>
</body>
</html>