package kr.co.aiai.dao;

public class EmpVO {
	private String e_id="";
	private String e_name="";
	private String sex="";
	private String addr="";
	
	
	public EmpVO() {
	}

	public EmpVO(String e_id, String e_name, String sex, String addr) {
		super();
		this.e_id = e_id;
		this.e_name = e_name;
		this.sex = sex;
		this.addr = addr;
	}
	
	public String getE_id() {
		return e_id;
	}
	public void setE_id(String e_id) {
		this.e_id = e_id;
	}
	public String getE_name() {
		return e_name;
	}
	public void setE_name(String e_name) {
		this.e_name = e_name;
	}
	public String getSex() {
		return sex;
	}
	public void setSex(String sex) {
		this.sex = sex;
	}
	public String getAddr() {
		return addr;
	}
	public void setAddr(String addr) {
		this.addr = addr;
	}

	@Override
	public String toString() {
		return "EmpVO [e_id=" + e_id + ", e_name=" + e_name + ", sex=" + sex + ", addr=" + addr + "]";
	}
	
	
}
 