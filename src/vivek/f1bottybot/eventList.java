package vivek.f1bottybot;
import java.io.FileNotFoundException;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;
public class eventList {
    public static ArrayList<f1> f1events() throws FileNotFoundException {
        ArrayList<f1> f1list = new ArrayList<>();
        String list = "Bahrain Grand Prix\t\tFree Practice 1\t\t03\t\t18\t\t16\t\t0\n" +
                "Bahrain Grand Prix\t\tFree Practice 2\t\t03\t\t18\t\t19\t\t0\n" +
                "Bahrain Grand Prix\t\tFree Practice 3\t\t03\t\t19\t\t16\t\t0\n" +
                "Bahrain Grand Prix\t\tQualifying\t\t03\t\t19\t\t19\t\t0\n" +
                "Bahrain Grand Prix\t\tGrand Prix\t\t03\t\t20\t\t19\t\t0\n" +
                "Saudi Arabian Grand Prix\t\tFree Practice 1\t\t03\t\t25\t\t18\t\t0\n" +
                "Saudi Arabian Grand Prix\t\tFree Practice 2\t\t03\t\t25\t\t21\t\t0\n" +
                "Saudi Arabian Grand Prix\t\tFree Practice 3\t\t03\t\t26\t\t18\t\t0\n" +
                "Saudi Arabian Grand Prix\t\tQualifying\t\t03\t\t26\t\t21\t\t0\n" +
                "Saudi Arabian Grand Prix\t\tGrand Prix\t\t03\t\t27\t\t21\t\t0\n" +
                "Australian Grand Prix\t\tFree Practice 1\t\t4\t\t8\t\t7\t\t0\n" +
                "Australian Grand Prix\t\tFree Practice 2\t\t4\t\t8\t\t10\t\t0\n" +
                "Australian Grand Prix\t\tFree Practice 3\t\t4\t\t9\t\t7\t\t0\n" +
                "Australian Grand Prix\t\tQualifying\t\t4\t\t9\t\t10\t\t0\n" +
                "Australian Grand Prix\t\tGrand Prix\t\t4\t\t10\t\t9\t\t0\n" +
                "Emilia Romagna Grand Prix\t\tFree Practice 1\t\t4\t\t22\t\t16\t\t0\n" +
                "Emilia Romagna Grand Prix\t\t Qualifying\t\t4\t\t22\t\t19\t\t0\n" +
                "Emilia Romagna Grand Prix\t\tFree Practice 2\t\t4\t\t23\t\t15\t\t0\n" +
                "Emilia Romagna Grand Prix\t\tF1™Sprint\t\t4\t\t23\t\t19\t\t0\n" +
                "Emilia Romagna Grand Prix\t\tGrand Prix\t\t4\t\t24\t\t17\t\t0\n" +
                "Miami Grand Prix\t\tFree Practice 1\t\t5\t\t6\t\t22\t\t30\n" +
                "Miami Grand Prix\t\tFree Practice 2\t\t5\t\t7\t\t1\t\t30\n" +
                "Miami Grand Prix\t\tFree Practice 3\t\t5\t\t7\t\t21\t\t0\n" +
                "Miami Grand Prix\t\tQualifying\t\t5\t\t8\t\t0\t\t0\n" +
                "Miami Grand Prix\t\tGrand Prix\t\t5\t\t8\t\t23\t\t30\n" +
                "Spanish Grand Prix\t\tFree Practice 1\t\t5\t\t20\t\t16\t\t0\n" +
                "Spanish Grand Prix\t\tFree Practice 2\t\t5\t\t20\t\t19\t\t0\n" +
                "Spanish Grand Prix\t\tFree Practice 3\t\t5\t\t21\t\t15\t\t0\n" +
                "Spanish Grand Prix\t\tQualifying\t\t5\t\t21\t\t18\t\t0\n" +
                "Spanish Grand Prix\t\tGrand Prix\t\t5\t\t22\t\t17\t\t0\n" +
                "Monaco Grand Prix\t\tFree Practice 1\t\t5\t\t27\t\t16\t\t0\n" +
                "Monaco Grand Prix\t\tFree Practice 2\t\t5\t\t27\t\t19\t\t0\n" +
                "Monaco Grand Prix\t\tFree Practice 3\t\t5\t\t28\t\t15\t\t0\n" +
                "Monaco Grand Prix\t\tQualifying\t\t5\t\t28\t\t18\t\t0\n" +
                "Monaco Grand Prix\t\tGrand Prix\t\t5\t\t29\t\t17\t\t0\n" +
                "Azerbaijan Grand Prix\t\tFree Practice 1\t\t6\t\t10\t\t15\t\t0\n" +
                "Azerbaijan Grand Prix\t\tFree Practice 2\t\t6\t\t10\t\t18\t\t0\n" +
                "Azerbaijan Grand Prix\t\tFree Practice 3\t\t6\t\t11\t\t15\t\t0\n" +
                "Azerbaijan Grand Prix\t\tQualifying\t\t6\t\t11\t\t18\t\t0\n" +
                "Azerbaijan Grand Prix\t\tGrand Prix\t\t6\t\t12\t\t15\t\t0\n" +
                "Canadian Grand Prix\t\tFree Practice 1\t\t6\t\t17\t\t22\t\t0\n" +
                "Canadian Grand Prix\t\tFree Practice 2\t\t6\t\t18\t\t1\t\t0\n" +
                "Canadian Grand Prix\t\tFree Practice 3\t\t6\t\t18\t\t21\t\t0\n" +
                "Canadian Grand Prix\t\tQualifying\t\t6\t\t19\t\t0\t\t0\n" +
                "Canadian Grand Prix\t\tGrand Prix\t\t6\t\t19\t\t22\t\t0\n" +
                "British Grand Prix\t\tFree Practice 1\t\t7\t\t1\t\t16\t\t0\n" +
                "British Grand Prix\t\tFree Practice 2\t\t7\t\t1\t\t19\t\t0\n" +
                "British Grand Prix\t\tFree Practice 3\t\t7\t\t2\t\t15\t\t0\n" +
                "British Grand Prix\t\tQualifying\t\t7\t\t2\t\t18\t\t0\n" +
                "British Grand Prix\t\tGrand Prix\t\t7\t\t3\t\t18\t\t0\n" +
                "Austrian Grand Prix\t\tFree Practice 1\t\t7\t\t8\t\t16\t\t0\n" +
                "Austrian Grand Prix\t\tQualifying\t\t7\t\t8\t\t19\t\t0\n" +
                "Austrian Grand Prix\t\tFree Practice 2\t\t7\t\t9\t\t15\t\t0\n" +
                "Austrian Grand Prix\t\tF1™Sprint\t\t7\t\t9\t\t18\t\t0\n" +
                "Austrian Grand Prix\t\tGrand Prix\t\t7\t\t10\t\t17\t\t0\n" +
                "French Grand Prix\t\tFree Practice 1\t\t7\t\t22\t\t16\t\t0\n" +
                "French Grand Prix\t\tFree Practice 2\t\t7\t\t22\t\t19\t\t0\n" +
                "French Grand Prix\t\tFree Practice 3\t\t7\t\t23\t\t15\t\t0\n" +
                "French Grand Prix\t\tQualifying\t\t7\t\t23\t\t18\t\t0\n" +
                "French Grand Prix\t\tGrand Prix\t\t7\t\t24\t\t17\t\t0\n" +
                "Hungarian Grand Prix\t\tFree Practice 1\t\t7\t\t29\t\t16\t\t0\n" +
                "Hungarian Grand Prix\t\tFree Practice 2\t\t7\t\t29\t\t19\t\t0\n" +
                "Hungarian Grand Prix\t\tFree Practice 3\t\t7\t\t30\t\t15\t\t0\n" +
                "Hungarian Grand Prix\t\tQualifying\t\t7\t\t30\t\t18\t\t0\n" +
                "Hungarian Grand Prix\t\tGrand Prix\t\t7\t\t31\t\t17\t\t0\n" +
                "Belgian Grand Prix\t\tFree Practice 1\t\t8\t\t26\t\t16\t\t0\n" +
                "Belgian Grand Prix\t\tFree Practice 2\t\t8\t\t26\t\t19\t\t0\n" +
                "Belgian Grand Prix\t\tFree Practice 3\t\t8\t\t27\t\t15\t\t0\n" +
                "Belgian Grand Prix\t\tQualifying\t\t8\t\t27\t\t18\t\t0\n" +
                "Belgian Grand Prix\t\tGrand Prix\t\t8\t\t28\t\t17\t\t0\n" +
                "Dutch Grand Prix\t\tFree Practice 1\t\t9\t\t2\t\t16\t\t0\n" +
                "Dutch Grand Prix\t\tFree Practice 2\t\t9\t\t2\t\t19\t\t0\n" +
                "Dutch Grand Prix\t\tFree Practice 3\t\t9\t\t3\t\t15\t\t0\n" +
                "Dutch Grand Prix\t\tQualifying\t\t9\t\t3\t\t18\t\t0\n" +
                "Dutch Grand Prix\t\tGrand Prix\t\t9\t\t4\t\t17\t\t0\n" +
                "Italian Grand Prix\t\tFree Practice 1\t\t9\t\t9\t\t16\t\t0\n" +
                "Italian Grand Prix\t\tFree Practice 2\t\t9\t\t9\t\t19\t\t0\n" +
                "Italian Grand Prix\t\tFree Practice 3\t\t9\t\t10\t\t15\t\t0\n" +
                "Italian Grand Prix\t\tQualifying\t\t9\t\t10\t\t18\t\t0\n" +
                "Italian Grand Prix\t\tGrand Prix\t\t9\t\t11\t\t17\t\t0\n" +
                "Singapore Grand Prix\t\tFree Practice 1\t\t9\t\t30\t\t14\t\t0\n" +
                "Singapore Grand Prix\t\tFree Practice 2\t\t9\t\t30\t\t17\t\t30\n" +
                "Singapore Grand Prix\t\tFree Practice 3\t\t10\t\t1\t\t14\t\t0\n" +
                "Singapore Grand Prix\t\tQualifying\t\t10\t\t1\t\t17\t\t0\n" +
                "Singapore Grand Prix\t\tGrand Prix\t\t10\t\t2\t\t16\t\t0\n" +
                "Japanese Grand Prix\t\tFree Practice 1\t\t10\t\t7\t\t8\t\t0\n" +
                "Japanese Grand Prix\t\tFree Practice 2\t\t10\t\t7\t\t12\t\t0\n" +
                "Japanese Grand Prix\t\tFree Practice 3\t\t10\t\t8\t\t8\t\t0\n" +
                "Japanese Grand Prix\t\tQualifying\t\t10\t\t8\t\t11\t\t0\n" +
                "Japanese Grand Prix\t\tGrand Prix\t\t10\t\t9\t\t9\t\t0\n" +
                "United States Grand Prix\t\tFree Practice 1\t\t10\t\t21\t\t23\t\t0\n" +
                "United States Grand Prix\t\tFree Practice 2\t\t10\t\t22\t\t2\t\t0\n" +
                "United States Grand Prix\t\tFree Practice 3\t\t10\t\t22\t\t23\t\t0\n" +
                "United States Grand Prix\t\tQualifying\t\t10\t\t23\t\t2\t\t0\n" +
                "United States Grand Prix\t\tGrand Prix\t\t10\t\t23\t\t23\t\t0\n" +
                "Mexico City Grand Prix\t\tFree Practice 1\t\t10\t\t28\t\t22\t\t0\n" +
                "Mexico City Grand Prix\t\tFree Practice 2\t\t10\t\t29\t\t1\t\t0\n" +
                "Mexico City Grand Prix\t\tFree Practice 3\t\t10\t\t29\t\t21\t\t0\n" +
                "Mexico City Grand Prix\t\tQualifying\t\t10\t\t30\t\t0\t\t0\n" +
                "Mexico City Grand Prix\t\tGrand Prix\t\t10\t\t31\t\t0\t\t0\n" +
                "Brazilian Grand Prix\t\tFree Practice 1\t\t11\t\t11\t\t20\t\t0\n" +
                "Brazilian Grand Prix\t\tQualifying\t\t11\t\t11\t\t23\t\t0\n" +
                "Brazilian Grand Prix\t\tFree Practice 2\t\t11\t\t12\t\t20\t\t0\n" +
                "Brazilian Grand Prix\t\tF1™Sprint\t\t11\t\t12\t\t23\t\t0\n" +
                "Brazilian Grand Prix\t\tGrand Prix\t\t11\t\t13\t\t22\t\t0\n" +
                "Abu Dhabi Grand Prix\t\tFree Practice 1\t\t11\t\t18\t\t14\t\t0\n" +
                "Abu Dhabi Grand Prix\t\tFree Practice 2\t\t11\t\t18\t\t17\t\t0\n" +
                "Abu Dhabi Grand Prix\t\tFree Practice 3\t\t11\t\t19\t\t15\t\t0\n" +
                "Abu Dhabi Grand Prix\t\tQualifying\t\t11\t\t19\t\t18\t\t0\n" +
                "Abu Dhabi Grand Prix\t\tGrand Prix\t\t11\t\t20\t\t17\t\t0";
        Scanner f = new Scanner(list);
        StringTokenizer s;
        while (f.hasNextLine()) {
            s = new StringTokenizer(f.nextLine(), "\t\t");
            f1list.add(new f1(s.nextToken(), s.nextToken(), ZonedDateTime.of(2022, Integer.parseInt(s.nextToken()), Integer.parseInt(s.nextToken()), Integer.parseInt(s.nextToken()), Integer.parseInt(s.nextToken()), 0, 0, ZoneId.of("UTC+4"))));
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
