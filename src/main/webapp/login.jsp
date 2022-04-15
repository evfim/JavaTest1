<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ taglib prefix="sec" uri="http://www.springframework.org/security/tags" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" isELIgnored="false" %>
<html>
<head>
	<meta http-equiv="Content-Security-Policy" content="policy">

	<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
</head>
<body>
	<div class="row">
		<div class="col-sm-4 col-sm-offset-4 text-center">
			<img style="width: 20em;" src="<c:url value="/resources/crm.png" />" />
			<h2>Hello CRM!</h2>
			<div class="alert alert-danger alert-dismissable" style="display:${strDisplayMsg};">
				<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
				${strMsg}
			</div>
			<form:form action="login2" method="post" modelAttribute="login" >
				<sec:csrfInput />
				<div class="input-group">
				<form:input type="text" id="username" path="username" class="form-control" placeholder="Username"></form:input>
				<form:input type="password" id="password" path="password" class="form-control" placeholder="Password"></form:input>
				<input type="submit" id="submit" class="btn btn-primary form-control" value="Login" />
					<input type="hidden" name="${_csrf.parameterName}" value="${_csrf.token}"/>
				</div>
			</form:form>
		</div>
	</div>
</body>
</html>
