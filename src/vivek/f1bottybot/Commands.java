package vivek.f1bottybot;
import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.jetbrains.annotations.NotNull;

import java.io.FileNotFoundException;
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
    public void onMessageReceived(@NotNull MessageReceivedEvent event) {
        String[] args = event.getMessage().getContentRaw().split("\\s+");
        if(args[0].equalsIgnoreCase(f1bot.prefix+"f1")){
            try {
                ArrayList<f1> events = eventList.f1events();
                ZonedDateTime current = ZonedDateTime.now();
                Duration diff = null;
                long st = System.nanoTime();
                Iterator<f1> i = events.iterator();
                f1 temp = null;
                while (i.hasNext()) {
                    temp = i.next();
                    if (current.isAfter(temp.z)) i.remove();
                    else {
                        diff = Duration.between(current, temp.z);
                        break;
                    }
                }
                long time = System.nanoTime() - st;
                event.getChannel().sendMessage("Search Time:" + time + "ns").queue();
                if(diff!=null) {
                    long s = diff.toSecondsPart();
                    long d = diff.toDaysPart();
                    long h = diff.toHoursPart();
                    long m = diff.toMinutesPart();
                    if (d != 0) {
                        timeToGo = d + " Days " + h + " Hours " + m + " Minutes " + s + " Seconds ";
                    } else timeToGo = h + " Hours " + m + " Minutes " + s + " Seconds ";
                    eventName = temp.event;
                    gpName = temp.race;
                    EmbedBuilder e = new EmbedBuilder();
                    e.setTitle("Next Formula 1 Event");
                    new embed().buildEmbed(event, e);
                }else event.getChannel().sendMessage("No race events found. This may be because most sessions are still TBC and start times will only be confirmed closer to event date.").queue();
            } catch (FileNotFoundException e) {e.printStackTrace();}
        }
        if(args[0].equalsIgnoreCase(f1bot.prefix+"f2")){
            try {
                ArrayList<f1> events = eventList.f2events();
                ZonedDateTime current = ZonedDateTime.now();
                Duration diff = null;
                Iterator<f1> i = events.iterator();
                f1 temp=null;
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
            } catch (FileNotFoundException e) {e.printStackTrace();}
        }
        if(args[0].equalsIgnoreCase(f1bot.prefix+"f3")){
            try {
                long st = System.nanoTime();
                ArrayList<f1> events = eventList.f3events();
                ZonedDateTime current = ZonedDateTime.now();
                Duration diff = null;
                Iterator<f1> i = events.iterator();
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
                    e.setTitle("Next Formula 3 Event");
                    new embed().buildEmbed(event, e);
                }
                else event.getChannel().sendMessage("No race events found. This may be because most sessions are still TBC and start times will only be confirmed closer to event date.").queue();
                e.clear();
            } catch (FileNotFoundException e) {e.printStackTrace();}
        }
        else if(args[0].equalsIgnoreCase(f1bot.prefix+"remind") && args[1]!=null){
            f1 temp = null;
            ArrayList<f1> events;
            try {
                ZonedDateTime current = ZonedDateTime.now();
                if (args[1].equalsIgnoreCase("f3")) {
                    events = eventList.f3events();
                    Duration diff = null;
                    Iterator<f1> i = events.iterator();
                    while (i.hasNext()) {
                        temp = i.next();
                        if (current.isAfter(temp.z)) i.remove();
                        else {
                            diff = Duration.between(current, temp.z);
                            break;
                        }
                    }
                    long ms = diff.toMillis() - 300000;
                    event.getChannel().sendMessage("Reminder set for " + temp.event + " , " + temp.race).queue();
                    f1 finalTemp = temp;
                    TimerTask f3 = new TimerTask() {
                        @Override
                        public void run() {
                            event.getChannel().sendMessage(event.getAuthor().getAsMention() + " " + finalTemp.event + " for " + finalTemp.race + " is starting now!").queue();
                            event.getChannel().sendMessage("https://giphy.com/gifs/mercedesamgf1-K8ZEMzkfkNAuz8OdBG").queue();
                        }
                    };
                    Timer t = new Timer();
                    t.schedule(f3, ms);
                }
                if (args[1].equalsIgnoreCase("f1")) {
                    long st = System.nanoTime();
                    events = eventList.f1events();
                    Duration diff = null;
                    Iterator<f1> i = events.iterator();
                    while (i.hasNext()) {
                        temp = i.next();
                        if (current.isAfter(temp.z)) i.remove();
                        else {
                            diff = Duration.between(current, temp.z);
                            break;
                        }
                    }
                    long ms = diff.toMillis() - 300000;
                    event.getChannel().sendMessage("Reminder set for " + temp.event + ", " + temp.race).queue();
                    f1 finalTemp = temp;
                    TimerTask f1 = new TimerTask() {
                        @Override
                        public void run() {
                            event.getChannel().sendMessage(event.getAuthor().getAsMention() + " " + finalTemp.event + " for " + finalTemp.race + " is starting now!").queue();
                            event.getChannel().sendMessage("https://giphy.com/gifs/mercedesamgf1-K8ZEMzkfkNAuz8OdBG").queue();
                        }
                    };
                    Timer t = new Timer();
                    t.schedule(f1, ms);
                    System.out.println((System.nanoTime() - st) / 1000000.000 + " ms");
                }
                if (args[1].equalsIgnoreCase("f2")) {
                        events = eventList.f2events();
                        Duration diff = null;
                        Iterator<f1> i = events.iterator();
                        while (i.hasNext()) {
                            temp = i.next();
                            if (current.isAfter(temp.z)) i.remove();
                            else {
                                diff = Duration.between(current, temp.z);
                                break;
                            }
                        }
                        long ms = diff.toMillis() - 300000;
                        event.getChannel().sendMessage("Reminder set for " + temp.event + ", " + temp.race).queue();
                    f1 finalTemp = temp;
                    TimerTask f1 = new TimerTask() {
                            @Override
                            public void run() {
                                event.getChannel().sendMessage(event.getAuthor().getAsMention() + " " + finalTemp.event + " for " + finalTemp.race + " is starting now!").queue();
                                event.getChannel().sendMessage("https://giphy.com/gifs/mercedesamgf1-K8ZEMzkfkNAuz8OdBG").queue();
                            }
                        };
                        Timer t = new Timer();
                        t.schedule(f1, ms);
                }
            }catch(Exception e){
                e.printStackTrace();
            }
        }
        /*else if(args[0].equalsIgnoreCase(f1bot.prefix+"standings")){
            try {
                WebClient w = new WebClient();
                w.getOptions().setCssEnabled(false);
                w.getOptions().setJavaScriptEnabled(false);
                String url = "https://www.formula1.com/en/results.html/2022/drivers.html";
                HtmlPage page = w.getPage(url);
                HtmlTable table = page.getHtmlElementById("resultsarchive-table");
                for (HtmlTableRow row : table.getRows()) {
                    System.out.println("Found row");
                    for (final HtmlTableCell cell : row.getCells()) {
                        System.out.println("   Found cell: " + cell.asNormalizedText());
                    }
                }
            } catch (IOException e) {e.printStackTrace();}
        }*/
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
                ArrayList<f1> events = eventList.f1events(); String all="";
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
