package vivek.f1bottybot;
import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.jetbrains.annotations.NotNull;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.time.Duration;
import java.time.ZonedDateTime;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Timer;
import java.util.TimerTask;

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
    ArrayList<f1> f1events,f2events,f3events; static long time;
    public Commands() throws IOException {
        f1events = eventList.f1events();
        f2events = eventList.f2events();
        f3events = eventList.f3events();
    }
    public void onMessageReceived(@NotNull MessageReceivedEvent event) {
        ZonedDateTime current = ZonedDateTime.now();
        String[] args = event.getMessage().getContentRaw().split("\\s+");
        Iterator<f1> i = null;
        if(args[0].equalsIgnoreCase(f1bot.prefix+"remind")&&args[1]!=null){
            if(args[1].equalsIgnoreCase("f1")) i = f1events.iterator();
            else if(args[1].equalsIgnoreCase("f2")) i = f2events.iterator();
            else if(args[1].equalsIgnoreCase("f3")) i = f3events.iterator();
            Duration diff = null;
            f1 temp = null;
            while (i.hasNext()) {
                temp = i.next();
                if (current.isAfter(temp.z)) i.remove();
                else {
                    diff = Duration.between(current, temp.z);
                    break;
                }
            }
            long ms = diff.toMillis() - 300000;
            event.getChannel().sendMessage("Reminder set for " + temp.event + " for the " + temp.race).queue();
            f1 finalTemp = temp;
            TimerTask timer = new TimerTask() {
                @Override
                public void run() {
                    event.getChannel().sendMessage(event.getAuthor().getAsMention() + " " + finalTemp.event + " for " + finalTemp.race + " is starting now!").queue();
                    event.getChannel().sendMessage("https://giphy.com/gifs/mercedesamgf1-K8ZEMzkfkNAuz8OdBG").queue();
                }
            };
            Timer t = new Timer();
            t.schedule(timer, ms);
        }
        if(args[0].equalsIgnoreCase(f1bot.prefix+"f1")){
                Duration diff = null;
                long st = System.nanoTime();
                f1 temp = null;
                i = f1events.iterator();
                while (i.hasNext()) {
                    temp = i.next();
                    if (current.isAfter(temp.z)) i.remove();
                    else {
                        diff = Duration.between(current, temp.z);
                        break;
                    }
                }
                time = System.nanoTime() - st;
                if(diff!=null) {
                    long s = diff.toSecondsPart();
                    long d = diff.toDaysPart();
                    long h = diff.toHoursPart();
                    long m = diff.toMinutesPart();
                    if (d != 0) {timeToGo = d + " Days " + h + " Hours " + m + " Minutes " + s + " Seconds ";}
                    else timeToGo = h + " Hours " + m + " Minutes " + s + " Seconds ";
                    eventName = temp.event;
                    gpName = temp.race;
                    EmbedBuilder e = new EmbedBuilder();
                    e.setTitle("Next Formula 1 Event");
                    new embed().buildEmbed(event, e);
                }else event.getChannel().sendMessage("No race events found. This may be because most sessions are still TBC and start times will only be confirmed closer to event date.").queue();
        }
        if(args[0].equalsIgnoreCase(f1bot.prefix+"f2")){
                Duration diff = null;
                f1 temp=null;
                i= f2events.iterator();
                while (i.hasNext()) {
                    temp = i.next();
                    if (current.isAfter(temp.z)) i.remove();
                    else {
                        diff = Duration.between(current, temp.z);
                        break;
                    }
                }
                EmbedBuilder e = new EmbedBuilder();
                if(diff!=null) {
                    long s = diff.toSecondsPart();
                    long d = diff.toDaysPart();
                    long h = diff.toHoursPart();
                    long m = diff.toMinutesPart();
                    if(d!=0){timeToGo = d + " Days " + h + " Hours " + m + " Minutes " + s + " Seconds ";}
                    else timeToGo = h + " Hours " + m + " Minutes " + s + " Seconds ";
                    eventName = temp.event;
                    gpName = temp.race;
                    e.setTitle("Next Formula 2 Event");
                    new embed().buildEmbed(event, e);
                } else event.getChannel().sendMessage("No race events found. This may be because most sessions are still TBC and start times will only be confirmed closer to event date.").queue();
                e.clear();
        }
        if(args[0].equalsIgnoreCase(f1bot.prefix+"f3")){
                long st = System.nanoTime();
                Duration diff = null;
                i = f3events.iterator();
                f1 temp=null;
                while (i.hasNext()) {
                    temp = i.next();
                    if (current.isAfter(temp.z)) i.remove();
                    else {
                        diff = Duration.between(current, temp.z);
                        break;
                    }
                }
                System.out.println(System.nanoTime()-st);
                if(args[0].equalsIgnoreCase(f1bot.prefix+"f3")) {
                    EmbedBuilder e = new EmbedBuilder();
                    if (diff != null) {
                        long s = diff.toSecondsPart();
                        long d = diff.toDaysPart();
                        long h = diff.toHoursPart();
                        long m = diff.toMinutesPart();
                        if (d != 0) {
                            timeToGo = d + " Days " + h + " Hours " + m + " Minutes " + s + " Seconds ";
                        } else timeToGo = h + " Hours " + m + " Minutes " + s + " Seconds ";
                        eventName = temp.event;
                        gpName = temp.race;
                        e.setTitle("Next Formula 3 Event");
                        new embed().buildEmbed(event, e);
                    } else
                        event.getChannel().sendMessage("No race events found. This may be because most sessions are still TBC and start times will only be confirmed closer to event date.").queue();
                    e.clear();
                }
        }
        else if(args[0].equalsIgnoreCase(f1bot.prefix+"drivers")){
            ArrayList<driverTeamDetails> std = standings.scrapedrivers();
            EmbedBuilder e = new EmbedBuilder();
            String name ="", country ="",team ="", pts ="";
            for (int c=0;c<std.size();c++) {
                name = name+std.get(c).name+"\n";
                //country=country+std.get(c).country+"\n";
                team=team+std.get(c).team+"\n";
                pts = pts+ std.get(c).pts +"\n";
            }
            e.addField("Driver",name,true);
            e.addField("Team",team,true);
            e.addField("Points",pts,true);
            e.setColor(0xff69ed);
            event.getChannel().sendMessageEmbeds(e.build()).queue();e.clear();
        }
        else if(args[0].equalsIgnoreCase(f1bot.prefix+"teams")){
            ArrayList<driverTeamDetails> std = standings.scrapeteams();
            EmbedBuilder e = new EmbedBuilder();
            String team ="", pts ="";
            for (int c=0;c<std.size();c++) {
                team=team+std.get(c).team+"\n";
                pts = pts+ std.get(c).pts +"\n";
            }
            e.addField("Team",team,true);
            e.addField("Points",pts,true);
            e.setColor(0xff69ed);
            event.getChannel().sendMessageEmbeds(e.build()).queue();e.clear();
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
            int j=0;String all = "";
            i= f1events.iterator();
            while(j<7){
                f1 temp=i.next();
                all+= temp.race;j++;
            }
            event.getChannel().sendMessage(all).queue();
        }
        else if(args[0].equalsIgnoreCase(f1bot.prefix+"invite")){event.getChannel().sendMessage("https://discord.com/api/oauth2/authorize?client_id=951889203581579304&permissions=34628298864&scope=bot").queue();}
        else if(args[0].equalsIgnoreCase(f1bot.prefix+"vansh")){event.getChannel().sendMessage("bhai kis chutiye ka naam le liya").queue();}
        else if(args[0].equalsIgnoreCase(f1bot.prefix+"sadaf")){event.getChannel().sendMessage("https://tenor.com/view/lewis-hamilton-mercedes-f1-gif-24213053").queue();}

    }
}
