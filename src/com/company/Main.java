package com.company;
import java.io.*;
import java.net.MalformedURLException;
import java.util.*;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.nio.channels.Channels;
import java.nio.channels.ReadableByteChannel;
import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.io.InputStream;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;


class Advent {

    public void solve() {
        solve(1);
    }


    public void solve(int i ) {
        String path = "./" + i + "/";


        System.out.println("solving " + i);
        switch (i){
            case 1: solveSubmarine1(path);
            case 2: solveCoursePlot2(path);
            case 3: binaryDiagnostic3(path);
            default: break;
        }

    }

    private void binaryDiagnostic3(String path) {
        String fileName = "input.txt";
        File inputFile;
        try {inputFile = getInputFile(path, fileName); } catch (IOException e) {
            e.printStackTrace();
            return;
        }
        Scanner sc;
        try {sc = new Scanner(inputFile); } catch (FileNotFoundException e) {
            e.printStackTrace();
            return;
        }
        int xPos = 0; int yPosInv = 0;
        while(sc.hasNext()){
            String subCommand = sc.next();
            int amount = sc.nextInt();
            if(subCommand.equals("forward"))
                xPos += amount;
            else if (subCommand.equals("up"))
                yPosInv -= amount;
            else if (subCommand.equals("down"))
                yPosInv += amount;
        } sc.close();
        FileWriter myWriter;
        try {
            myWriter = new FileWriter(path + "outputA.txt");
            myWriter.write(Integer.toString(xPos * yPosInv) + "\n");
            myWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
            return;
        }
        if(true)
            return;

        try {sc = new Scanner(inputFile); } catch (FileNotFoundException e) {
            e.printStackTrace();
            return;
        }
        xPos = 0; yPosInv = 0; int aim = 0;
        while(sc.hasNext()){
            String subCommand = sc.next();
            int amount = sc.nextInt();
            if(subCommand.equals("forward")) {
                xPos += amount;
                yPosInv += amount * aim;
            }
            else if (subCommand.equals("up"))
                aim -= amount;
            else if (subCommand.equals("down"))
                aim += amount;
        } sc.close();
        try {
            myWriter = new FileWriter(path + "outputB.txt");
            myWriter.write(Integer.toString(xPos * yPosInv) + "\n");
            myWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
            return;
        }

    }

    private void solveCoursePlot2(String path) {
        String fileName = "input.txt";
        File inputFile;
        try {inputFile = getInputFile(path, fileName); } catch (IOException e) {
            e.printStackTrace();
            return;
        }
        Scanner sc;
        try {sc = new Scanner(inputFile); } catch (FileNotFoundException e) {
            e.printStackTrace();
            return;
        }
        int xPos = 0; int yPosInv = 0;
        while(sc.hasNext()){
            String subCommand = sc.next();
            int amount = sc.nextInt();            
            if(subCommand.equals("forward"))
                xPos += amount;
            else if (subCommand.equals("up"))
                yPosInv -= amount;
            else if (subCommand.equals("down"))
                yPosInv += amount;
        }sc.close();
        FileWriter myWriter;
        try {
            myWriter = new FileWriter(path + "outputA.txt");
            myWriter.write(Integer.toString(xPos * yPosInv) + "\n");
            myWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
            return;
        }


        try {sc = new Scanner(inputFile); } catch (FileNotFoundException e) {
            e.printStackTrace();
            return;
        }
        xPos = 0; yPosInv = 0; int aim = 0;
        while(sc.hasNext()){
            String subCommand = sc.next();
            int amount = sc.nextInt();
            if(subCommand.equals("forward")) {
                xPos += amount;
                yPosInv += amount * aim;
            }
            else if (subCommand.equals("up"))
                aim -= amount;
            else if (subCommand.equals("down"))
                aim += amount;
        } sc.close();
        try {
            myWriter = new FileWriter(path + "outputB.txt");
            myWriter.write(Integer.toString(xPos * yPosInv) + "\n");
            myWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
            return;
        }



    }

    private void solveSubmarine1(String path) {
        String fileName = "inputA.txt";
        File inputFile;
        try {
            inputFile = getInputFile(path, fileName);
        } catch (IOException e) {
            e.printStackTrace();
            return;
        }



        Scanner sc;
        try {
            sc = new Scanner(inputFile);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return;
        }

        int prev = 0;
        int curr = sc.nextInt();
        int countDown = 0;
        while (sc.hasNextInt()){
            prev = curr; curr = sc.nextInt();
            if(curr > prev)
                ++countDown;
        } sc.close();




        FileWriter myWriter;
        try {
            myWriter = new FileWriter(path + "outputA.txt");
            myWriter.write(Integer.toString(countDown) + "\n");
            myWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
            return;
        }


        try {
            sc = new Scanner(inputFile);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return;
        }

        Queue<Integer> q = new LinkedList();
        q.add(sc.nextInt());q.add(sc.nextInt());q.add(sc.nextInt());
        countDown = 0;
        while (sc.hasNextInt()){
            int a = sc.nextInt();
            q.add(a);
            if(a >  q.poll())
                ++countDown;
        } sc.close();


        try {
            myWriter = new FileWriter(path + "outputB.txt");
            myWriter.write(Integer.toString(countDown) + "\n");
            myWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
            return;
        }
    }


    private void getFile(String website, File file) throws IOException {
        URL url = new URL(website);
        try (InputStream in = url.openStream()) {
            Files.copy(in, file.toPath());
        }

    }
    private File getInputFile(String path, String fileName) throws IOException{
        File tempFile = new File(path + fileName);
        if(!tempFile.exists()){
            try {
                new File(path).mkdirs();
                this.getFile("https://adventofcode.com/" + "2021/day/1/input.txt", tempFile);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return tempFile;
    }
}

public class Main {
    public static void start(int n){
        Advent advent = new Advent();
        advent.solve(n);
    }


    public static void main(String[] args) {
	    System.out.println("\nHello Programmer, you are solving advent calender at https://adventofcode.com/. Continue session? \n");
        Scanner sc = new Scanner(System.in);
        String in = sc.nextLine();
        if(in == "")
            start(2);
        else if(Integer.parseInt(in) > 0 && Integer.parseInt(in) < 25)
            start(Integer.parseInt(in));


        System.out.println("\n");
    }
}
