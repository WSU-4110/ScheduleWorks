import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Parent;
import javafx.scene.Scene;

public class InterfaceMain extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        Parent root = FXMLLoader.load(getClass().getResource("Interface.fxml"));
        primaryStage.setTitle("ScheduleWorks");
        primaryStage.setScene(new Scene(root, 300, 275));
        primaryStage.show();
    }
}
