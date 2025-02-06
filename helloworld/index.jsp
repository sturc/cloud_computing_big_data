<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"
    import = "java.io.*,java.util.*, javax.servlet.*" 
%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head><title>Hello World JSP</title></head>
<body>
<%! Date creationDate = new Date();%> 
<p> 
	<% out.println("<h1><font color=red>Hello World</h1>"); 
       out.println("<h2>Created: " + creationDate.toString() + "</h2>"); 
       Date date = new Date();
       out.println( "<h2 align = \"center\"> Accessed on: " +date.toString()+"</h2>");
    %>
</p>
</body>
</html>
