package sg.lam;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Import;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class LoginController {
	
	@Autowired
	UserService userService;

	@RequestMapping(value = "/")
	public ModelAndView home(HttpServletRequest request, HttpServletResponse response) {
		return new ModelAndView("home");
	}

    @RequestMapping(value = "/login", method = RequestMethod.GET)
    public ModelAndView show(HttpServletRequest request, HttpServletResponse response) {
        ModelAndView mv = new ModelAndView("login", "login", new Login());
        mv.addObject("strDisplayMsg", "msg-none");
        return mv;
    }
	
	@RequestMapping(value = "/login2", method = RequestMethod.POST)
	public ModelAndView login(HttpServletRequest request, HttpServletResponse response,
					  @ModelAttribute("login") Login login, BindingResult result) {
		
		ModelAndView mv = null;
		
		User user = userService.login(login.getUsername(), login.getPassword());

		if (user != null && user.isActive()) {
			System.out.println("Login OK.");
			user.setPassword(null);
			request.getSession().setAttribute("loginUser", user);
			mv = new ModelAndView("redirect:/posts");
		} else {
			System.out.println("Login FAILED.");
			
			mv = new ModelAndView("login");
			mv.addObject("strMsg", "Wrong Login!");
			mv.addObject("strDisplayMsg", ".msg-show");
		}
		
		return mv;
	}

}
