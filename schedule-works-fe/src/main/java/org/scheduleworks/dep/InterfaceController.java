package org.scheduleworks.dep;

import java.awt.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Insets;
import javafx.stage.Stage;
import javafx.stage.StageStyle;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.control.TextArea;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.FileWriter;
import javafx.scene.image.Image;
import java.io.IOException; 



public class InterfaceController {
    //  Login menu
    @FXML
    private TextField username;
    @FXML
    private PasswordField password;
    @FXML
    private Button loginButton;
    @FXML
    private TextField code;
    @FXML
    private TextArea taCoursesTaken;
    @FXML
    private Button btn_submit_code;

    private static Stage stg;
    private double x,y=0;
    
    public void pressLoginTab() throws Exception {
        FXMLLoader loader = new FXMLLoader(getClass().getClassLoader().getResource("InterfaceLogin.fxml"));
        loader.setController(new InterfaceController());
        Parent root = loader.load();
        Stage loginStage = new Stage();

        loginStage.getIcons().add(new Image(getClass().getClassLoader().getResourceAsStream("ScheduleWorksLogo.png")));
        loginStage.initStyle(StageStyle.UNDECORATED);
        stg = loginStage;
        loginStage.setTitle("Login");
        loginStage.setScene(new Scene(root));
        loginStage.setResizable(false);


        root.setOnMousePressed(mouseEvent ->{
            x=mouseEvent.getSceneX();
            y=mouseEvent.getSceneY();
        });
        root.setOnMouseDragged(mouseEvent ->{
            loginStage.setX(mouseEvent.getScreenX()-x);
            loginStage.setY(mouseEvent.getScreenY()-y);
        });

        loginStage.show();// show the login page

        System.out.println("Login tab pressed");
    }

    public void pressLoginButton() throws Exception{
        privateInfo userInfo = new privateInfo();
        userInfo.setUsername(username.getText().toString());
        userInfo.setPassword(password.getText().toString());
        stg.close();
        
        /*
        InterfaceMain x = new InterfaceMain();
        x.changeScene("Interface.fxml");
        */
        Thread t = new Thread(new pythonExecute(userInfo.getUsername(),userInfo.getPassword()));
        t.start();

        System.out.println(userInfo.getUsername());

        // System.out.println(userInfo.getPassword());
        closeApplication();
    }

    //  Retrieve courses
    public void retrieveCoursesTab(){
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
    }

    public void submitCode() {
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

    

    //  Close application
    @FXML private javafx.scene.control.Button Close_button;

    public void closeApplication() throws Exception{
        Stage stage = (Stage) Close_button.getScene().getWindow();
        stage.close(); // this is to close the Application.
        System.out.println("Application closed");
    }
        public void pressHelp() throws Exception {
        FXMLLoader loader = new FXMLLoader(getClass().getClassLoader().getResource("Help.fxml"));
        loader.setController(new InterfaceController());
        Parent root = loader.load();
        Stage helpStage = new Stage();


        //loginStage.initStyle(StageStyle.UNDECORATED);
        stg = helpStage;
        helpStage.setTitle("Help");
        helpStage.setScene(new Scene(root));
        helpStage.setResizable(false);


        root.setOnMousePressed(mouseEvent ->{
            x=mouseEvent.getSceneX();
            y=mouseEvent.getSceneY();
        });
        root.setOnMouseDragged(mouseEvent ->{
            helpStage.setX(mouseEvent.getScreenX()-x);
            helpStage.setY(mouseEvent.getScreenY()-y);
        });

        helpStage.show();

    }
}
