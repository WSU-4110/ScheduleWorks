package org.scheduleworks.dep;

import java.io.IOException;
import java.lang.Thread;

public class pythonNub implements Runnable{
    public void run(){
        try{

            String command = "cmd /c \"C:/Program Files/ScheduleWorks/schedule-works-be/build_graphs.bat";
            Process process = Runtime.getRuntime().exec(command);
      
    
    
            long start = System.currentTimeMillis();
            long end = start + 80*1000; // 80 seconds * 1000 ms/sec
            while (System.currentTimeMillis() < end)
            {
                try{Thread.sleep(10000);}catch(InterruptedException e){System.out.println(e);}   
            }
            
        }catch (IOException  e) {
            e.printStackTrace();
        }
       }
}
