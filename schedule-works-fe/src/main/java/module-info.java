module org.scheduleworks.dep {
    requires javafx.controls;
    requires javafx.fxml;


    requires java.desktop;

    opens org.scheduleworks.dep to javafx.fxml;
    exports org.scheduleworks.dep;
}
