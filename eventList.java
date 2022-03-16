package vivek.f1bottybot;
import java.io.File;
import java.io.FileNotFoundException;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;
public class eventList {
    static ArrayList<f1> returnAL() throws FileNotFoundException {
        ArrayList<f1> returnAL = new ArrayList<>(110);
        Scanner f = new Scanner(new File("F:\\Vivvysaur\\Documents\\f1bot\\src\\vivek\\f1bottybot\\f1list.txt"));
        StringTokenizer s;
        while(f.hasNextLine()){
            s= new StringTokenizer(f.nextLine(),"\t\t");
            returnAL.add(new f1(s.nextToken(),s.nextToken(),ZonedDateTime.of(2022,Integer.parseInt(s.nextToken()),Integer.parseInt(s.nextToken()),Integer.parseInt(s.nextToken()),Integer.parseInt(s.nextToken()),0,0,ZoneId.of("UTC+4"))));
        }
        return returnAL;
    }
}
