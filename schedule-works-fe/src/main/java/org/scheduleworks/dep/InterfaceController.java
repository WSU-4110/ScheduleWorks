package org.scheduleworks.dep;

import javafx.fxml.FXML;
import javafx.stage.Stage;
import javafx.scene.control.Button;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.control.ToggleButton;
import javafx.scene.control.TextArea;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.FileWriter;
import javafx.scene.text.Text;
import java.io.IOException; 

public class InterfaceController extends InterfaceMain {
    //  BUTTON LIST
    @FXML
    private Button btn_login_tab;
    @FXML
    private Text userText;
    @FXML
    private TextField username;
    @FXML
    private PasswordField password;
    @FXML
    private Button loginButton;
    @FXML
    private ToggleButton toggle_selenium_bg;
    @FXML
    private ToggleButton toggle_save_cookies;

    @FXML
    private TextField code;
    @FXML
    private Button retrieveStartButton;
    @FXML
    private TextArea taCoursesTaken;
    @FXML
    private Button btn_submit_code;

    //  GLOBAL VARIABLES
    private static Stage stg;
    private double x, y = 0;
    static privateInfo userInfo = new privateInfo();

    //  LOGIN TAB
    public void pressLoginTab() throws Exception {
        changeScene("InterfaceLogin.fxml");

        //changeUserText();         //  FIX THIS if possible, remove/comment out otherwise
    }

    public void changeUserText() throws Exception {
        if (userInfo.getUsername() == "") {
            userText.setText("Not currently logged in ⚠");
            //btn_login_tab.setText("Login");
        }
        else {
            userText.setText("Welcome " + userInfo.getUsername());
            //btn_login_tab.setText("Welcome " + userInfo.getUsername());
        }
    }

    public void pressLoginButton() throws Exception {
        userInfo.setUsername(username.getText().toString());
        userInfo.setPassword(password.getText().toString());
        changeUserText();

        System.out.println(userInfo.getUsername());     //  Test print, can be removed later
        
        Thread t = new Thread(new pythonExecute(userInfo.getUsername(),userInfo.getPassword()));
        t.start();

        username.clear();
        password.clear();
    }

    public void seleniumBackgroundButton() throws Exception {
        boolean isSelected = toggle_selenium_bg.isSelected();
        if (isSelected) {
            toggle_selenium_bg.setText("On");
            userInfo.setSeleniumToggle(true);
        }
        else {
            toggle_selenium_bg.setText("Off");
            userInfo.setSeleniumToggle(false);
        }
    }

    public void saveCookiesButton() throws Exception {
        boolean isSelected = toggle_save_cookies.isSelected();
        if (isSelected) {
            toggle_save_cookies.setText("On");
            userInfo.setSaveCookiesToggle(true);
        }
        else {
            toggle_save_cookies.setText("Off");
            userInfo.setSaveCookiesToggle(false);
        }
    }

    //  RETRIEVE COURSES TAB
    public void retrieveCoursesTab() throws Exception {
        changeScene("InterfaceRetrieve.fxml");
        /*   OLD CODE, DELETE LATER
        taCoursesTaken.clear();
        File file = new File("C:\\Program Files\\ScheduleWorks\\data\\courseHistory.txt");
        try {
            if (file.createNewFile()) {
                System.out.println("File created: " + file.getName());
            } else {
                System.out.println("File already exists.");
            }
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }

       try{
        Scanner scan = new Scanner(file);
        if (file.length()==0){
            taCoursesTaken.clear();
            taCoursesTaken.setPromptText("Please login and submit the 2FA Code");
        }
        while(scan.hasNextLine()){
            taCoursesTaken.appendText(scan.nextLine() + "\n");
            }
        } 
        catch (FileNotFoundException e){
        e.printStackTrace();
       }
       */
    }

    public void pressRetrieveStartButton() throws Exception {
        System.out.println("RETRIEVE START");
        taCoursesTaken.clear();

        //  No login info present
        if (userInfo.getUsername() == "" || userInfo.getPassword() == "") {
            taCoursesTaken.appendText("Username and/or password not entered\nEnter login info in the \"Login\" tab");
            return;
        }

        File file = new File("C:\\Program Files\\ScheduleWorks\\data\\courseHistory.txt");
        try {
            if (file.createNewFile()) {
                System.out.println("File created: " + file.getName());
            } else {
                System.out.println("File already exists.");
            }
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }

       try{
        Scanner scan = new Scanner(file);
        if (file.length()==0){
            taCoursesTaken.clear();
            taCoursesTaken.setPromptText("Please login and submit the 2FA Code");
        }
        while(scan.hasNextLine()){
            taCoursesTaken.appendText(scan.nextLine() + "\n");
            }
        } 
        catch (FileNotFoundException e){
        e.printStackTrace();
       }
    }

    public void submitCode() {
        System.out.println("Code submitted");
        try{
            BufferedWriter br = new BufferedWriter(new FileWriter(new File("C:\\Program Files\\ScheduleWorks\\schedule-works-be\\2fa_code.txt")));
            br.write(code.getText().toString());
            br.write("done");
            br.close();
        }
        catch (java.io.IOException e){
            e.printStackTrace();
        }
        code.setPromptText(code.getText().toString());
        code.clear();
    }

    public void viewCourseHistory(){
        stg.close();
    }

    //  RETRIEVE COURSES TAB
    public void createScheduleTab() throws Exception {
        changeScene("InterfaceCreateSchedule.fxml");
    }

    

    //  Close application
    @FXML private javafx.scene.control.Button Close_button;

    public void closeApplication() throws Exception {
        Stage stage = (Stage) Close_button.getScene().getWindow();
        stage.close(); // this is to close the Application.
        System.out.println("Application closed");

        System.exit(0);
    }
}
