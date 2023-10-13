package vivek.f1bottybot;
import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.OnlineStatus;
import net.dv8tion.jda.api.entities.Activity;
import net.dv8tion.jda.api.requests.GatewayIntent;

import javax.security.auth.login.LoginException;
import java.io.FileNotFoundException;
import java.io.IOException;

public class f1bot {
    public static JDA jda;
    public static String prefix ="+";
    public static void main(String[] args) throws LoginException, IOException {
        jda = JDABuilder.createLight(Token.token, GatewayIntent.GUILD_MESSAGES, GatewayIntent.MESSAGE_CONTENT, GatewayIntent.GUILD_MEMBERS).build();
        jda.getPresence().setStatus(OnlineStatus.IDLE);
        jda.getPresence().setActivity(Activity.watching("T's life unfold"));
        jda.addEventListener(new Commands());
    }
}
