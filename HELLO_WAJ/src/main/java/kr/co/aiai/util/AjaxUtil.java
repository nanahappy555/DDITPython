package kr.co.aiai.util;

import java.io.PrintWriter;
import java.util.List;
import java.util.Map;
import javax.servlet.http.HttpServletResponse;
import org.codehaus.jackson.map.ObjectMapper;
import kr.co.aiai.dao.EmpVO;

public class AjaxUtil {
	public static void responseXml(HttpServletResponse response,String resultStr) throws Exception{
		response.setContentType("application/xml");
		PrintWriter out = response.getWriter();
		out.print(resultStr);
		out.flush();
		out.close();
	}	
	
	public static void responseJson(HttpServletResponse response, List<EmpVO> list) throws Exception {
		String result = new ObjectMapper().writeValueAsString(list);
		response.setContentType("text/javascript;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.print(result);
		out.flush();
		out.close();
	}
	
	
	public static void responseJson(HttpServletResponse response, EmpVO vo) throws Exception {
		String result = new ObjectMapper().writeValueAsString(vo);
		response.setContentType("text/javascript;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.print(result);
		out.flush();
		out.close();
	}

	public static void responseJson(HttpServletResponse response, String resultStr) throws Exception {
		String result = new ObjectMapper().writeValueAsString(resultStr);
		response.setContentType("text/javascript;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.print(result);
		out.flush();
		out.close();
	}
	
	public static void responseStr(HttpServletResponse response, String resultStr) throws Exception {
		String result = resultStr;
		response.setContentType("text/javascript;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.print(result);
		out.flush();
		out.close();
	}	

	public static void responseJson(HttpServletResponse response, Map map) throws Exception {
		String result = new ObjectMapper().writeValueAsString(map);
		response.setContentType("text/javascript;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.print(result);
		out.flush();
		out.close();
	}
}
