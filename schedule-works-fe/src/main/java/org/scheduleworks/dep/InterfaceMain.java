package org.scheduleworks.dep;

import java.awt.*;
import javafx.animation.FadeTransition;
import javafx.application.Application;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.stage.StageStyle;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.layout.StackPane;
import javafx.util.Duration;

import javafx.stage.Screen;

public class InterfaceMain extends Application{

    private static Stage stg;
    private double x, y = 0;

    public static void main(String[] args){
        launch(args); // necessary to start the application
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        stg = primaryStage;
        FXMLLoader loader = new FXMLLoader(getClass().getClassLoader().getResource("InterfaceStart.fxml"));
        //loader.setController(new InterfaceController());
        Parent root = loader.load();

        primaryStage.getIcons().add(new Image(getClass().getClassLoader().getResourceAsStream("ScheduleWorksLogo.png")));
        primaryStage.initStyle(StageStyle.DECORATED);
        primaryStage.setTitle("ScheduleWorks"); // Title of the page of Interface
        primaryStage.setScene(new Scene(root)); // sets up the size of the interface showm in the scene 

        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        primaryStage.setMaxWidth(screenSize.getWidth());
        primaryStage.setMaxHeight(screenSize.getHeight());
        primaryStage.setMinWidth(1280);
        primaryStage.setMinHeight(810);
        primaryStage.setWidth(1280);
        primaryStage.setHeight(810);

        root.setOnMousePressed(mouseEvent ->{
            x=mouseEvent.getSceneX();
            y=mouseEvent.getSceneY();
        });
        root.setOnMouseDragged(mouseEvent ->{
            primaryStage.setX(mouseEvent.getScreenX()-x);
            primaryStage.setY(mouseEvent.getScreenY()-y);
        });

        primaryStage.setResizable(true);
        primaryStage.show();
    }
    

    public void changeScene(String fxml) throws Exception {
        FXMLLoader loader = new FXMLLoader(getClass().getClassLoader().getResource(fxml));
        loader.setController(new InterfaceController());
        Parent root = loader.load();

        Scene newScene = new Scene(root);
        stg.setScene(newScene);
        
        //  Changes the width very slightly so that all scene objects are at the correct resolution
        double width = stg.getWidth();
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        if (width % 1 == 0)
            stg.setWidth(width * 1.00007812);
        else
            stg.setWidth(Math.floor(width));
        //System.out.println("Width: " + width);
    }

    @FXML
    void fadeIn() {
        FadeTransition fadeTransition = new FadeTransition(Duration.seconds(2));
        fadeTransition.setFromValue(1.0);
        fadeTransition.setToValue(0.0);
        fadeTransition.play();
    }

    @FXML
    void fadeOut() {
        FadeTransition fadeTransition = new FadeTransition(Duration.seconds(2));
        fadeTransition.setFromValue(0.0);
        fadeTransition.setToValue(1.0);
        fadeTransition.play();
    }

    public Stage getPane(){
        return stg;
    }
}
