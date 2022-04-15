package sg.lam.test;

import org.junit.jupiter.api.Test;
import org.springframework.web.multipart.MultipartFile;
import sg.lam.Post;
import sg.lam.PostOwner;
import sg.lam.User;

import java.util.Date;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class PostTest {

    @Test
    public void testPost() {
        Date publishToDate = new Date();
        Post post = new Post(1, "test post", "http://test.com/img.jpg", "test content",
                publishToDate, Post.Status.draft);
        assertEquals("Post [id=1, title=test post, imagePath=http://test.com/img.jpg, content=test content, " +
                "publishToDate=" + new Date().toString() + ", status=draft, owner=0]", post.toString());
    }

    @Test
    public void testOwner() {
        PostOwner owner = new User(1, "tester",
                "test@tester.com", "12345678", true, User.UserRole.editor);
        Date publishToDate = new Date();
        Post post = new Post(1, "test post", "http://test.com/img.jpg", "test content",
                publishToDate, Post.Status.draft);
        post.setOwner(owner);
        assertEquals("User [id=1, name=tester, email=test@tester.com, " +
                "password=12345678, role=editor, active=true]", post.getOwner().toString());
    }

    @Test
    public void testSanitizer() {
        Date publishToDate = new Date();
        Post post = new Post(1, "<script>alert('hacked')</script>", "http://test.com/img.jpg",
                "test <script>alert('hacked')</script> content",
                publishToDate, Post.Status.draft);
        assertEquals("", post.getTitle());
        assertEquals("test  content", post.getContent());
    }

}