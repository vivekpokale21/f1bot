package vivek.f1bottybot;

import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import static vivek.f1bottybot.Commands.*;

public class embed extends ListenerAdapter{
    public void buildEmbed(MessageReceivedEvent event, EmbedBuilder e){
        e.addField("Event Name", gpName, true);
        if (gpName.contains("Bahrain")) {
            location = "Sakhir";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1e7-1f1ed.png");
        } else if (gpName.contains("Saudi")) {
            location = "Jeddah";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1f8-1f1e6.png");
        } else if (gpName.contains("Australia")) {
            location = "Melbourne";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1e6-1f1fa.png");
        } else if (gpName.contains("Emilia")) {
            location = "Imola";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1ee-1f1f9.png");
        } else if (gpName.contains("Miami")) {
            location = "Miami Gardens";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1fa-1f1f8.png");
        } else if (gpName.contains("Spanish")||gpName.contains("Spain")) {
            location = "Barcelona";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1ea-1f1f8.png");
        } else if (gpName.contains("Monaco")) {
            location = "Monte-Carlo";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1f2-1f1e8.png");
        } else if (gpName.contains("Azerbaijan")) {
            location = "Baku";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1e6-1f1ff.png");
        } else if (gpName.contains("Canadian")) {
            location = "Montréal";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1e8-1f1e6.png");
        } else if (gpName.contains("British")) {
            location = "Silverstone";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1ec-1f1e7.png");
        } else if (gpName.contains("Austrian")) {
            location = "Spielberg";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1e6-1f1f9.png");
        } else if (gpName.contains("French")) {
            location = "Le Castellet";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1eb-1f1f7.png");
        } else if (gpName.contains("Hungarian")) {
            location = "Budapest";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1ed-1f1fa.png");
        } else if (gpName.contains("Belgian")) {
            location = "Spa-Francorchamps";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1e7-1f1ea.png");
        } else if (gpName.contains("Dutch")) {
            location = "Zandvoort";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1f3-1f1f1.png");
        } else if (gpName.contains("Singapore")) {
            location = "Marina Bay";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1f8-1f1ec.png");
        } else if (gpName.contains("Japanese")) {
            location = "Suzuka";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1ef-1f1f5.png");
        } else if (gpName.contains("United States")) {
            location = "Austin";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1fa-1f1f8.png");
        } else if (gpName.contains("Mexico")) {
            location = "Mexico City";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1f2-1f1fd.png");
        } else if (gpName.contains("Brazilian")) {
            location = "Sao Paolo";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1e7-1f1f7.png");
        } else {
            location = "Yas Marina";
            e.setThumbnail("https://images.emojiterra.com/twitter/v13.1/512px/1f1e6-1f1ea.png");
        }

        e.addField("Location", location, true);
        e.addField("Session Name", eventName, false);
        e.addField("Time to Go", timeToGo, false);
        e.setColor(0xff69ed);
        e.setFooter("Vivek Pokale | Search Time: "+Commands.time+" ns");

        event.getChannel().sendMessageEmbeds(e.build()).queue();

        e.clear();
    }
}
