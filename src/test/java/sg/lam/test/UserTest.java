package sg.lam.test;

import org.junit.jupiter.api.Test;
import sg.lam.User;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class UserTest {

    @Test
    public void testUser() {
        User user = new User(1, "tester",
                "test@tester.com", "12345678", true, User.UserRole.editor);
        assertEquals("User [id=1, name=tester, email=test@tester.com, " +
                        "password=12345678, role=editor, active=true]", user.toString());
    }

    @Test
    public void testActive() {
        User user = new User(1, "tester",
                "test@tester.com", "12345678", true, User.UserRole.editor);
        user.setActive(false);
        assertTrue(!user.isActive());
    }

}