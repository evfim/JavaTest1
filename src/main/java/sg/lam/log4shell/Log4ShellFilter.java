package sg.lam.log4shell;

import org.springframework.stereotype.Component;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import java.io.IOException;
import java.util.Enumeration;
import javax.servlet.Filter;

@Component
public class Log4ShellFilter implements Filter {

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {

        /**
         * Log4Shell Mitigation
         * Disallow jndi: in all endpoints
         */
        Enumeration<String> attributes = request.getAttributeNames();
        String name;
        while (attributes.hasMoreElements()) {
            name = attributes.nextElement();
            String value = (String) request.getAttribute(name);
            String filteredValue = value.replaceAll("jndi:", "");
            request.setAttribute(name, filteredValue);
        }

        chain.doFilter(request, response);
    }

}