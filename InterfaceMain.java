import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.stage.StageStyle;
import javafx.scene.Parent;
import javafx.scene.Scene;

public class InterfaceMain extends Application {
    private static Stage stg;

    public static void main(String[] args) {
        launch(args); // necessary to start the application
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        stg = primaryStage;
        Parent root = FXMLLoader.load(getClass().getResource("Interface.fxml"));
        primaryStage.setTitle("ScheduleWorks");// Title of the page of Interface
        primaryStage.setScene(new Scene(root, 930, 600)); // sets up the size of the interface showm in the scene 
        primaryStage.setResizable(false); // cannot change the size of the screen
        primaryStage.show();
    }
    

    public void changeScene(String fxml) throws Exception {
        Parent pane = FXMLLoader.load(getClass().getResource(fxml));
        stg.getScene().setRoot(pane);
    }
}
