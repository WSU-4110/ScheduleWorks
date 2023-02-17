package org.scheduleworks.dep;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Parent;
import javafx.scene.Scene;

public class App extends Application {
    private static Stage stg;

    public static void main(String[] args) {
       

        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        System.out.println(getClass().getClassLoader().getResource("Interface.fxml").getPath());
        stg = primaryStage;
        FXMLLoader loader = new FXMLLoader(getClass().getClassLoader().getResource("Interface.fxml"));
        loader.setController(new InterfaceController());
        Parent root = loader.load();
        
        primaryStage.setTitle("ScheduleWorks");
        primaryStage.setScene(new Scene(root, 969, 598));
        primaryStage.setResizable(false);
        primaryStage.show();

        // System.out.println(FXMLLoader.load(getClass().getClassLoader().getResource("Interface.fxml")));
    }

    // public void changeScene(String fxml) throws Exception {
    //     Parent pane = FXMLLoader.load(getClass().getResource(fxml));
    //     stg.getScene().setRoot(pane);
    // }
}
