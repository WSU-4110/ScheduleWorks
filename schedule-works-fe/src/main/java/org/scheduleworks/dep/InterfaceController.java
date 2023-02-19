package org.scheduleworks.dep;

import java.awt.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Insets;
import javafx.stage.Stage;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;

public class InterfaceController {
    //  Login menu
    @FXML
    private TextField username;
    @FXML
    private PasswordField password;
    @FXML
    private Button loginButton;
    private static Stage stg;
    
    public void pressLoginTab() throws Exception {
        FXMLLoader loader = new FXMLLoader(getClass().getClassLoader().getResource("InterfaceLogin.fxml"));
        loader.setController(new InterfaceController());
        Parent root = loader.load();

        Stage loginStage = new Stage();
        stg = loginStage;
        loginStage.setTitle("Login");
        loginStage.setScene(new Scene(root,500,375));
        loginStage.setResizable(false);
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

        System.out.println(userInfo.getUsername());
        System.out.println(userInfo.getPassword());
    }

    //  Retrieve courses
    public void retrieveCoursesTab(){
        System.out.println("Retrieve Courses button pressed");
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
}
