import java.io.IOException;
import java.io.File;
import java.lang.Thread;
import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.FileWriter;
public class pythonExecute {
   public static void getInfo(String username, String password){
    try{
        Scanner scan= new Scanner(System.in);
        BufferedWriter br = new BufferedWriter(new FileWriter(new File("2fa_code.txt")));
        //input code here
        Process process = Runtime.getRuntime().exec(
            "cmd /c get_info.bat"+"'"+username+"'"+"'"+password+"'", null, new File(System.getProperty("user.dir")));
        System.out.print("code : ");
        br.write(scan.nextLine());
        br.write("done");
        br.close();



        while(process.isAlive()){
            try{Thread.sleep(10000);}catch(InterruptedException e){System.out.println(e);}   
        }
        try{Thread.sleep(2000);}catch(InterruptedException e){System.out.println(e);}   



    }catch (IOException  e) {
        e.printStackTrace();
    }
   }
}
