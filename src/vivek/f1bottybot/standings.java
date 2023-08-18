package vivek.f1bottybot;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.util.ArrayList;

class driverTeamDetails{
    String name, team,country; int pts;
    driverTeamDetails(String n, String t, String c, int p){name = n; team=t;pts=p;country=c;}
    driverTeamDetails(String t, int p){team=t;pts=p;}

}
public class standings {
    static String getTeam(String t){
        if(t.contains("Red")){t="Red Bull";}
        else if(t.contains("Alpine")){t="Alpine";}
        else if(t.contains("Aston")){t="Aston Martin";}
        else if(t.contains("McLaren")){t="McLaren";}
        else if(t.contains("Williams")){t="Williams";}
        else if(t.contains("Alpha")){t="AlphaTauri";}
        else if(t.contains("Alfa")){t="Alfa Romeo";}
        else if(t.contains("Haas")){t="Haas";}
        return t;
    }
    static ArrayList<driverTeamDetails> scrapedrivers() {
        // initializing the HTML Document page variable
        Document doc;
        try {
            // fetching the target website
            doc = Jsoup.connect("https://www.formula1.com/en/results.html/2023/drivers.html").get();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        Element tableElement = doc.select("table").first();
        System.out.println();
        Elements tableRowElements = tableElement.select(":not(thead) tr");
        ArrayList<driverTeamDetails> a = new ArrayList<>();
        for (int i=0;i< tableRowElements.size();i++) {
            Element row = tableRowElements.get(i);
            Elements rowItems = row.select("td");
            for (int j = 0; j < rowItems.size(); j+=8) {
                String s = rowItems.get(2).text();
                String n = rowItems.get(3).text();
                String team = rowItems.get(4).text();
                s = s.substring(0, s.length() - 4);
                if(s.contains("Vries")){ s=s.split(" ")[1]+" "+s.split(" ")[2];}
                else if (s.contains("Zhou")) {s=s.split(" ")[0];}
                else s = s.split(" ")[1];
                int p = Integer.parseInt(rowItems.get(5).text());
                String t= getTeam(team);
                a.add(new driverTeamDetails(s,t,n,p));
                break;
            }
        }
        return a;
    }
    static ArrayList<driverTeamDetails> scrapeteams() {
        Document doc;
        try {
            // fetching the target website
            doc = Jsoup.connect("https://www.formula1.com/en/results.html/2023/team.html").get();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        Element tableElement = doc.select("table").first();
        System.out.println();
        Elements tableRowElements = tableElement.select(":not(thead) tr");
        ArrayList<driverTeamDetails> a = new ArrayList<>();
        for (int i=0;i< tableRowElements.size();i++) {
            Element row = tableRowElements.get(i);
            Elements rowItems = row.select("td");
            for (int j = 0; j < rowItems.size(); j+=8) {
                String s = rowItems.get(2).text();
                int p = Integer.parseInt(rowItems.get(3).text());
                String t= getTeam(s);
                a.add(new driverTeamDetails(t,p));
                break;
            }
        }
        return a;
    }
}
