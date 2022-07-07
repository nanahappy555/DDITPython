<%@page import="kr.co.aiai.dao.EmpVO"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<%
int cnt = (int)request.getAttribute("cnt");
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
let cnt = <%=cnt%>;

if(cnt == 1){
	alert("정상적으로 수정됐습니다.");
	location.href = "emp_list";
} else {
	history.back();
// 	history.go(-1); back(1) 과 같음
}
</script>
</head>
<body>

</body>
</html>