/*
 * RemoteUser authentication module for Cascade
 *
 * This module lets you use Tomcat or Apache authentication
 * with Cascade.
 *
 * February 2008, Earl Fogel, University of Saskatchewan
 */
package edu.bethel.cascade;

import java.io.*;
import javax.servlet.http.*;
import com.hannonhill.cascade.model.security.authentication.*;

public class RemoteUserAuth implements Authenticator {
	public boolean redirect(HttpServletRequest request, HttpServletResponse response, AuthenticationPhase phase) throws IOException {
	  
		if (request.getHeader("CAS-User") == null) {
			return false;
		}

		if (phase == AuthenticationPhase.LOGIN) {
			response.sendRedirect("/customauth");
			return true;
		}
		if (phase == AuthenticationPhase.LOGOUT) {
			response.sendRedirect("http://auth.bethel.edu/cas/logout");
			return true;
		}

		return false;
	}

	public String authenticate(HttpServletRequest request, HttpServletResponse response) {
		return request.getHeader("CAS-User");
	}
}