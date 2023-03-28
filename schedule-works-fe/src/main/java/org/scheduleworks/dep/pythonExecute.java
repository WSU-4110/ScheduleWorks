package org.scheduleworks.dep;

import java.io.IOException;
import java.io.File;
import java.lang.Thread;
import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.FileWriter;

public class pythonExecute implements Runnable{
    private String username;
    private String password;

    public pythonExecute(String username,String password){
        this.username = username;
        this.password = password;
    }


   public void run(){
    try{
        Scanner scan= new Scanner(System.in);
        BufferedWriter br = new BufferedWriter(new FileWriter(new File("C:\\Program Files\\ScheduleWorks\\schedule-works-be\\2fa_code.txt")));
        //input code here
        // String command = "cmd /c \"C:/Program Files/ScheduleWorks/schedule-works-be/get_info.bat\""+"\'"+username+"\'"+" "+"\'"+password+"\'";
        String command = "cmd /c \"C:/Program Files/ScheduleWorks/schedule-works-be/get_info.bat\""+ " "+this.username+" "+this.password;
        // System.out.println(command);
        Process process = Runtime.getRuntime().exec(command);
  


        long start = System.currentTimeMillis();
        long end = start + 180*1000; // 180 seconds
        while (System.currentTimeMillis() < end)
        {
            try{Thread.sleep(10000);}catch(InterruptedException e){System.out.println(e);}   
        }
        
    }catch (IOException  e) {
        e.printStackTrace();
    }
   }
}
