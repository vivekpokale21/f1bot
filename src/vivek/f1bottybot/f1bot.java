package vivek.f1bottybot;
import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.OnlineStatus;
import net.dv8tion.jda.api.entities.Activity;
import javax.security.auth.login.LoginException;
public class f1bot {
    public static JDA jda;
    public static String prefix ="+";
    public static void main(String[] args) throws LoginException {
        jda = JDABuilder.createDefault(Token.token).build();
        jda.getPresence().setStatus(OnlineStatus.IDLE);
        jda.getPresence().setActivity(Activity.watching("T's life unfold"));
        jda.addEventListener(new Commands());
    }
}
