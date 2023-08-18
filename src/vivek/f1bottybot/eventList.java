package vivek.f1bottybot;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.time.ZoneId;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;
public class eventList {
    public static ArrayList<f1> f1events() throws IOException {
        ArrayList<f1> f1list = new ArrayList<>();
        BufferedReader s = new BufferedReader(new FileReader("src\\vivek\\f1bottybot\\sched.csv"));
        String line = "";
        while ((line = s.readLine()) != null) {
            String[] str = line.split(",");
            DateTimeFormatter format = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss").withZone(ZoneOffset.UTC);
            String race = str[1];
            int i = 2;
            while (i <= 11) {
                String event = str[i];
                ZonedDateTime z = ZonedDateTime.parse(str[i + 1], format);
                f1list.add(new f1(race, event, z));
                i += 2;
            }
        }
        return f1list;
    }
    static ArrayList<f1> f2events() throws FileNotFoundException {
        ArrayList<f1> f2list = new ArrayList<>(10);
        String list = "Round 3: Emilia Romagna\t\tPractice\t\t04\t\t22\t\t13\t\t05\n" +
                "Round 3: Emilia Romagna\t\tQualifying\t\t04\t\t22\t\t17\t\t55\n" +
                "Round 3: Emilia Romagna\t\tSprint Race\t\t04\t\t23\t\t19\t\t55\n" +
                "Round 3: Emilia Romagna\t\tFeature Race\t\t04\t\t24\t\t12\t\t20\n"+
                "Round 4: Spain\t\tPractice\t\t05\t\t20\t\t13\t\t35\n"+
                "Round 4: Spain\t\tQualifying\t\t05\t\t20\t\t20\t\t30\n"+
                "Round 4: Spain\t\tSprint Race\t\t05\t\t21\t\t19\t\t40\n"+
                "Round 4: Spain\t\tFeature Race\t\t05\t\t22\t\t13\t\t35";
        Scanner f = new Scanner(list);
        StringTokenizer s;
        while (f.hasNextLine()) {
            s = new StringTokenizer(f.nextLine(), "\t\t");
            f2list.add(new f1(s.nextToken(), s.nextToken(), ZonedDateTime.of(2022, Integer.parseInt(s.nextToken()), Integer.parseInt(s.nextToken()), Integer.parseInt(s.nextToken()), Integer.parseInt(s.nextToken()), 0, 0, ZoneId.of("UTC+4"))));
        }
        return f2list;
    }
    static ArrayList<f1> f3events() throws FileNotFoundException {
        ArrayList<f1> f3list = new ArrayList<>(10);
        String list = "Round 2: Emilia Romagna\t\tPractice\t\t04\t\t22\t\t11\t\t55\n" +
                "Round 2: Emilia Romagna\t\tQualifying\t\t04\t\t22\t\t17\t\t00\n" +
                "Round 2: Emilia Romagna\t\tSprint Race\t\t04\t\t23\t\t12\t\t35\n" +
                "Round 2: Emilia Romagna\t\tFeature Race\t\t04\t\t24\t\t10\t\t50\n"+
                "Round 3: Spain\t\tFeature Race\t\t05\t\t19\t\t20\t\t40\n";
        Scanner f = new Scanner(list);
        StringTokenizer s;
        while (f.hasNextLine()) {
            s = new StringTokenizer(f.nextLine(), "\t\t");
            f3list.add(new f1(s.nextToken(), s.nextToken(), ZonedDateTime.of(2022, Integer.parseInt(s.nextToken()), Integer.parseInt(s.nextToken()), Integer.parseInt(s.nextToken()), Integer.parseInt(s.nextToken()), 0, 0, ZoneId.of("UTC+4"))));
        }
        return f3list;
    }
}
