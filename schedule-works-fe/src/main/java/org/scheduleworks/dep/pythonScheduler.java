package org.scheduleworks.dep;

import java.io.IOException;
import java.lang.Thread;


public class pythonScheduler implements Runnable{
    private String arguements;

    public pythonScheduler(String arguements){
        // if (arguements.length()>0){
        //     this.arguements = "--courses ";
        // }
        this.arguements = arguements;

    }


   public void run(){
    try{
        // String command = "cmd /c \"C:/\"Program Files\"/ScheduleWorks/schedule-works-be/scheduler.bat\" "+this.arguements+"";
        // String command = "cmd /c  \"C:\\Program Files\\ScheduleWorks\\schedule-works-be\\scheduler.bat\"";
        String command = "cmd /c \"c:\\Program Files\\ScheduleWorks\\schedule-works-be\\scheduler.bat\" "+this.arguements;
        System.out.println(command);
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

   public static void main(String [] args){
    System.out.println("hi");
    // String command = "cmd /c \"c:\\Program Files\\ScheduleWorks\\schedule-works-be\\scheduler.bat\" ";
    // System.out.println(command);
    Thread t = new Thread(new pythonScheduler("CSC 3200 5 CSC 5290 6"));
    t.start();

   }
}

