package vivek.f1bottybot;
import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.jetbrains.annotations.NotNull;
import java.io.FileNotFoundException;
import java.time.Duration;
import java.time.ZonedDateTime;
import java.util.ArrayList;
class f1 {
    ZonedDateTime z;
    String race, event;
    f1(String race, String event, ZonedDateTime z) {
        this.z = z;
        this.event = event;
        this.race = race;
    }
}
public class Commands extends ListenerAdapter {
    public static String timeToGo,eventName,gpName,location;int i;
    public void onMessageReceived(@NotNull MessageReceivedEvent event) {
        String[] args = event.getMessage().getContentRaw().split("\\s+");
        if(args[0].equalsIgnoreCase(f1bot.prefix+"f1")){
            try {
                ArrayList<f1> events = eventList.returnAL();
                ZonedDateTime current = ZonedDateTime.now();
                int start = 0;
                Duration diff = null;
                for (i = start; i < events.size(); i++) {
                    if (current.isBefore(events.get(i).z)) {
                        diff = Duration.between(current, events.get(i).z);
                        break;
                    } else start = i;
                }
                long s = diff.toSecondsPart();
                long d = diff.toDaysPart();
                long h = diff.toHoursPart();
                long m = diff.toMinutesPart();
                timeToGo = d + " Days " + h + " Hours " + m + " Mins " + s + " Seconds ";
                eventName = events.get(i).event;
                gpName = events.get(i).race;
                EmbedBuilder e = new EmbedBuilder();
                e.setTitle("Next Formula 1 Event");
                e.addField("Event Name", gpName, true);
                if (Commands.gpName.contains("Bahrain")) {location="Sakhir";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1e7-1f1ed.png");}
                else if (Commands.gpName.contains("Saudi")) {location="Jeddah";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1f8-1f1e6.png");}
                else if (Commands.gpName.contains("Australia")) {location="Melbourne";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1e6-1f1fa.png");}
                else if (Commands.gpName.contains("Emilia")) {location="Imola";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1ee-1f1f9.png");}
                else if (Commands.gpName.contains("Miami")) {location="Miami Gardens";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1fa-1f1f8.png");}
                else if (Commands.gpName.contains("Spanish")) {location="Barcelona";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1ea-1f1f8.png");}
                else if (Commands.gpName.contains("Monaco")) {location="Monte-Carlo";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1f2-1f1e8.png");}
                else if (Commands.gpName.contains("Azerbaijan")) {location="Baku";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1e6-1f1ff.png");}
                else if (Commands.gpName.contains("Canadian")) {location="Montréal";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1e8-1f1e6.png");}
                else if (Commands.gpName.contains("British")) {location="Silverstone";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1ec-1f1e7.png");}
                else if (Commands.gpName.contains("Austrian")) {location="Spielberg";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1e6-1f1f9.png");}
                else if (Commands.gpName.contains("French")) {location="Le Castellet";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1eb-1f1f7.png");}
                else if (Commands.gpName.contains("Hungarian")) {location="Budapest";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1ed-1f1fa.png");}
                else if (Commands.gpName.contains("Belgian")) {location="Spa-Francorchamps";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1e7-1f1ea.png");}
                else if (Commands.gpName.contains("Dutch")) {location="Zandvoort";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1f3-1f1f1.png");}
                else if (Commands.gpName.contains("Singapore")) {location="Marina Bay";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1f8-1f1ec.png");}
                else if (Commands.gpName.contains("Japanese")) {location="Suzuka";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1ef-1f1f5.png");}
                else if (Commands.gpName.contains("United States")) {location="Austin";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1fa-1f1f8.png");}
                else if (Commands.gpName.contains("Mexico")) {location="Mexico City";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1f2-1f1fd.png");}
                else if (Commands.gpName.contains("Brazilian")) {location="Sao Paolo";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1e7-1f1f7.png");}
                else{location="Yas Marina";e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1e6-1f1ea.png");}

                e.addField("Location",location,true);
                e.addField("Session Name", eventName, false);
                e.addField("Time to Go",timeToGo, false);
                e.setColor(0xff69ed);
                e.setFooter("Created by Vivek Pokale");

                event.getChannel().sendMessageEmbeds(e.build()).queue();
                e.clear();
            } catch (FileNotFoundException e) {e.printStackTrace();}
        }
        else if(args[0].equalsIgnoreCase(f1bot.prefix+"anmol")){event.getChannel().sendMessage("you mean *professor* anmol?").queue();}
        else if(args[0].equalsIgnoreCase(f1bot.prefix+"sans")){
            event.getChannel().sendMessage(":regional_indicator_o::regional_indicator_m::regional_indicator_g::regional_indicator_o::regional_indicator_s::regional_indicator_h:\n" +
                ":regional_indicator_s::regional_indicator_o:\n:regional_indicator_t::regional_indicator_o::regional_indicator_x::regional_indicator_i::regional_indicator_c:").queue();
        }
        else if(args[0].equalsIgnoreCase(f1bot.prefix+"sanika")){event.getChannel().sendMessage("Not found. Try `+sunnyka` instead. Maybe that'll work. Maybe.").queue();}
        else if(args[0].equalsIgnoreCase(f1bot.prefix+"sunnyka")){event.getChannel().sendMessage("9GPA never forget").queue();}
        else if(args[0].equalsIgnoreCase(f1bot.prefix+"tatu")){event.getChannel().sendMessage("The best thing that's ever happened to little v").queue();}
        else if(args[0].equalsIgnoreCase(f1bot.prefix+"all")) {
            try {
                ArrayList<f1> events = eventList.returnAL(); String all="";
                for (i=0;i<events.size()/2;i++) {all+=events.get(i).race+" "+events.get(i).event+"\n";}
                event.getChannel().sendMessage(all).queue(); all="";
                for (i=events.size()/2+1;i<events.size();i++) {all+=events.get(i).race+" "+events.get(i).event+"\n";}
                event.getChannel().sendMessage(all).queue();
            } catch (FileNotFoundException e) {e.printStackTrace();}
        }
        else if(args[0].equalsIgnoreCase(f1bot.prefix+"invite")){event.getChannel().sendMessage("https://discord.com/api/oauth2/authorize?client_id=951889203581579304&permissions=34628298864&scope=bot").queue();}
        else if(args[0].equalsIgnoreCase(f1bot.prefix+"vansh")){event.getChannel().sendMessage("bhai kis chutiye ka naam le liya").queue();}
        else if(args[0].equalsIgnoreCase(f1bot.prefix+"sadaf")){event.getChannel().sendMessage("https://tenor.com/view/lewis-hamilton-mercedes-f1-gif-24213053").queue();}
    }
}
