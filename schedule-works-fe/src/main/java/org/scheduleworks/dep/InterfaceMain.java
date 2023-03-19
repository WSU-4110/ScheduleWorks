package org.scheduleworks.dep;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.stage.StageStyle;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.layout.*;
import javafx.scene.control.*;
import javafx.scene.image.Image;

public class InterfaceMain extends Application{
    private static Stage stg;
    private double x,y = 0;

    public static void main(String[] args){
        launch(args); // necessary to start the application
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        stg = primaryStage;
        FXMLLoader loader = new FXMLLoader(getClass().getClassLoader().getResource("Interface.fxml"));
        loader.setController(new InterfaceController());
        Parent root = loader.load();

        primaryStage.getIcons().add(new Image(getClass().getClassLoader().getResourceAsStream("ScheduleWorksLogo.png")));
        primaryStage.initStyle(StageStyle.DECORATED);
        primaryStage.setTitle("ScheduleWorks"); // Title of the page of Interface
        primaryStage.setScene(new Scene(root)); // sets up the size of the interface showm in the scene 
        primaryStage.setMinWidth(1200);
        primaryStage.setMinHeight(800);

        root.setOnMousePressed(mouseEvent ->{
            x=mouseEvent.getSceneX();
            y=mouseEvent.getSceneY();
        });
        root.setOnMouseDragged(mouseEvent ->{
            primaryStage.setX(mouseEvent.getScreenX()-x);
            primaryStage.setY(mouseEvent.getScreenY()-y);
        });

        primaryStage.setResizable(true); // cannot change the size of the screen
        primaryStage.show();

    }
    

    public void changeScene(String fxml) throws Exception {
        FXMLLoader loader = new FXMLLoader(getClass().getClassLoader().getResource(fxml));
        loader.setController(new InterfaceController());
        Parent root = loader.load();

        Scene newScene = new Scene(root);
        stg.setScene(newScene);
    }
}
