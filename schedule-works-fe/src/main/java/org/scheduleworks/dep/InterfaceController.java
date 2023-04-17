package org.scheduleworks.dep;

import javafx.fxml.FXML;
import javafx.stage.Stage;
import javafx.scene.control.Button;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.ToggleButton;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.image.ImageView;
import javafx.scene.image.Image;
import javafx.scene.control.TextArea;
import java.io.File;
import java.io.BufferedWriter;
import java.io.FileWriter;
import javafx.scene.text.Text;
import java.io.IOException;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.FileReader;
import javafx.scene.control.TableColumn;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import java.net.URI;
import java.awt.Desktop;

public class InterfaceController extends InterfaceMain {
    // BUTTON LIST
    @FXML
    private Button btn_login_tab;
    @FXML
    private Text userText;
    @FXML
    private Text incorrectLoginIndicator;
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
    private Button btn_retrieve_tab;
    @FXML
    private TextField code;
    @FXML
    private Button retrieveStartButton;
    @FXML
    private TextArea taCoursesTaken;
    @FXML
    private Button btn_submit_code;

    @FXML
    private Button btn_graph_tab;
    @FXML
    private Button btn_show_graph;
    @FXML
    private Button btn_show_graph_full;

    @FXML
    private Button btn_create_schedule_tab;
    @FXML
    private Button btn_help_tab;

    @FXML
    private TableView<Course> tableCourses;

    // IMAGE LIST
    @FXML
    private ImageView graphView;

    // GLOBAL VARIABLES
    private static Stage stg;
    private double x, y = 0;
    static privateInfo userInfo = new privateInfo();

    // LOGIN TAB
    public void pressLoginTab() throws Exception {
        changeScene("InterfaceLogin.fxml");

        // Reset toggles in privateInfo
        userInfo.setSeleniumToggle(true);
        userInfo.setSaveCookiesToggle(true);
        // System.out.println(userInfo.getSeleniumToggle());
        // System.out.println(userInfo.getSaveCookiesToggle());

        // btn_login_tab.setText("Welcome " + userInfo.getUsername());
        // changeUserText(); // FIX THIS if possible, remove/comment out otherwise
    }

    public void changeUserText() throws Exception {
        if (userInfo.getUsername() == "") {
            userText.setText("Not currently logged in ⚠");
            btn_login_tab.setText("Login");
        } else {
            userText.setText("Welcome " + userInfo.getUsername());
            btn_login_tab.setText("Welcome " + userInfo.getUsername());
        }
    }

    public void pressLoginButton() throws Exception {
        if (username.getText().toString() == "" || password.getText().toString() == "") {
            incorrectLoginIndicator.setOpacity(1);
        } else {
            incorrectLoginIndicator.setOpacity(0);
            userInfo.setUsername(username.getText().toString());
            userInfo.setPassword(password.getText().toString());
            // changeUserText();

            System.out.println(userInfo.getUsername()); // Test print, can be removed later

            Thread t = new Thread(new pythonExecute(userInfo.getUsername(), userInfo.getPassword()));
            t.start();

            username.clear();
            password.clear();
        }
    }

    public void seleniumBackgroundButton() throws Exception {
        boolean isSelected = toggle_selenium_bg.isSelected();
        if (isSelected) {
            toggle_selenium_bg.setText("On");
            userInfo.setSeleniumToggle(true);
        } else {
            toggle_selenium_bg.setText("Off");
            userInfo.setSeleniumToggle(false);
        }
    }

    public void saveCookiesButton() throws Exception {
        boolean isSelected = toggle_save_cookies.isSelected();
        if (isSelected) {
            toggle_save_cookies.setText("On");
            userInfo.setSaveCookiesToggle(true);
        } else {
            toggle_save_cookies.setText("Off");
            userInfo.setSaveCookiesToggle(false);
        }
    }

    // RETRIEVE COURSES TAB
    public void retrieveCoursesTab() throws Exception {
        changeScene("InterfaceRetrieve.fxml");

        /*
         * OLD CODE, DELETE LATER
         * taCoursesTaken.clear();
         * File file = new
         * File("C:\\Program Files\\ScheduleWorks\\data\\courseHistory.txt");
         * try {
         * if (file.createNewFile()) {
         * System.out.println("File created: " + file.getName());
         * } else {
         * System.out.println("File already exists.");
         * }
         * } catch (IOException e) {
         * System.out.println("An error occurred.");
         * e.printStackTrace();
         * }
         * 
         * try{
         * Scanner scan = new Scanner(file);
         * if (file.length()==0){
         * taCoursesTaken.clear();
         * taCoursesTaken.setPromptText("Please login and submit the 2FA Code");
         * }
         * while(scan.hasNextLine()){
         * taCoursesTaken.appendText(scan.nextLine() + "\n");
         * }
         * }
         * catch (FileNotFoundException e){
         * e.printStackTrace();
         * }
         */
    }

    public void setUpTable() {

        TableColumn<Course, String> attributeColumn = new TableColumn<>("Discipline");
        attributeColumn.setMinWidth(50);
        attributeColumn.setCellValueFactory(new PropertyValueFactory<>("discipline"));

        TableColumn<Course, String> passColumn = new TableColumn<>("Passed");
        passColumn.setMinWidth(60);
        passColumn.setCellValueFactory(new PropertyValueFactory<>("pass"));

        TableColumn<Course, String> nameColumn = new TableColumn<>("Name");
        nameColumn.setMinWidth(200);
        nameColumn.setCellValueFactory(new PropertyValueFactory<>("name"));

        TableColumn<Course, String> creditColumn = new TableColumn<>("Credit");
        creditColumn.setMinWidth(40);
        creditColumn.setCellValueFactory(new PropertyValueFactory<>("credit"));

        TableColumn<Course, String> numberColumn = new TableColumn<>("Number");
        numberColumn.setMinWidth(50);
        numberColumn.setCellValueFactory(new PropertyValueFactory<>("number"));

        tableCourses.setItems(getCoursedList());
        tableCourses.getColumns().addAll(attributeColumn, numberColumn, creditColumn, nameColumn, passColumn);
    }

    public void pressRetrieveStartButton() throws Exception {
        System.out.println("RETRIEVE START");
        // taCoursesTaken.clear();
        setUpTable();
        // // No login info present
        // if (userInfo.getUsername() == "" || userInfo.getPassword() == "") {
        // taCoursesTaken.appendText("Username and/or password not entered\nEnter login
        // info in the \"Login\" tab");
        // return;
        // }

        // File file = new File("C:\\Program
        // Files\\ScheduleWorks\\data\\courseHistory.txt");
        // try {
        // if (file.createNewFile()) {
        // System.out.println("File created: " + file.getName());
        // } else {
        // System.out.println("File already exists.");
        // }
        // } catch (IOException e) {
        // System.out.println("An error occurred.");
        // e.printStackTrace();
        // }

        // try{
        // Scanner scan = new Scanner(file);
        // if (file.length()==0){
        // taCoursesTaken.clear();
        // taCoursesTaken.setPromptText("Please login and submit the 2FA Code");
        // }
        // while(scan.hasNextLine()){
        // taCoursesTaken.appendText(scan.nextLine() + "\n");
        // }
        // }
        // catch (FileNotFoundException e){
        // e.printStackTrace();
        // }

    }

    public void submitCode() {
        System.out.println("Code submitted");
        try {
            BufferedWriter br = new BufferedWriter(
                    new FileWriter(new File("C:\\Program Files\\ScheduleWorks\\schedule-works-be\\2fa_code.txt")));
            br.write(code.getText().toString());
            br.write("done");
            br.close();
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }
        code.setPromptText(code.getText().toString());
        code.clear();
    }

    public void viewCourseHistory() {
        stg.close();
    }

    // COURSE GRAPH TAB
    public void courseGraphTab() throws Exception {

        changeScene("InterfaceCourseGraph.fxml");
    }

    public void showGraphFull() throws Exception {
        System.out.println(getPane().widthProperty().getValue());
        graphView.setFitWidth(getPane().widthProperty().getValue() / 2);
        graphView.setLayoutX(getPane().widthProperty().getValue() / 5);
        try {
            graphView.setImage(new Image(getClass().getClassLoader().getResourceAsStream("graph_full.png")));
        } catch (java.lang.RuntimeException e) {
            System.out.println("Couldn't find image");
            return;
        }
        btn_show_graph.setVisible(false);
        btn_show_graph_full.setVisible(false);

    }

    public void showGraph() throws Exception {
        System.out.println(getPane().widthProperty().getValue());
        graphView.setFitWidth(getPane().widthProperty().getValue() / 2);
        graphView.setLayoutX(getPane().widthProperty().getValue() / 5);
        try {
            graphView.setImage(new Image(getClass().getClassLoader().getResourceAsStream("graph_small.png")));
        } catch (java.lang.RuntimeException e) {
            System.out.println("Couldn't find image");
            return;
        }
        btn_show_graph.setVisible(false);
        btn_show_graph_full.setVisible(false);

    }

    public ArrayList<ArrayList<String>> getCourseData() {
        ArrayList<ArrayList<String>> arrList = new ArrayList<ArrayList<String>>();

        File file = new File("C:\\Program Files\\ScheduleWorks\\data\\courseHistory.txt");
        BufferedReader reader;
        int iter = 0;
        ArrayList<String> tempList = new ArrayList<String>();

        try {
            reader = new BufferedReader(new FileReader(file));
            String line = reader.readLine();

            while (line != null) {
                // System.out.println(line);
                int col = iter % 5;
                if (col % 5 == 0 && tempList.size() > 0) {
                    arrList.add((ArrayList<String>) tempList.clone());
                    tempList.clear();
                }
                tempList.add(line);
                line = reader.readLine();
                iter += 1;
            }

            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        // System.out.println(Arrays.deepToString(arrList.toArray()));

        return arrList;
    }

    public ObservableList<Course> getCoursedList() {
        ObservableList<Course> data = FXCollections.observableArrayList();

        for (ArrayList<String> tempList : getCourseData()) {
            // System.out.println(tempList.get(4)+tempList.get(3)+tempList.get(2)+tempList.get(0)+tempList.get(1));
            data.add(new Course(tempList.get(4), tempList.get(3), tempList.get(2), tempList.get(0), tempList.get(1)));
        }

        return data;
    }

    // CREATE SCHEDULE TAB
    public void createScheduleTab() throws Exception {
        changeScene("InterfaceCreateSchedule.fxml");
    }

    // Close application
    @FXML
    private javafx.scene.control.Button Close_button;

    public void closeApplication() throws Exception {
        Stage stage = (Stage) Close_button.getScene().getWindow();
        stage.close(); // this is to close the Application.
        System.out.println("Application closed");

        System.exit(0);
    }

    public void pressHelp() throws Exception {
        changeScene("Help.fxml");

    }

    public void EmailPage() throws Exception {
        System.out.println("Link clicked");
        Desktop.getDesktop().browse(new URI("https://mail.google.com/mail"));
    }

    public void FaqPage() throws Exception {
        changeScene("Faq.fxml");

    }

    public void firstMenu() throws Exception {
        changeScene("first.fxml");

    }

    public void secondMenu() throws Exception {
        changeScene("second.fxml");

    }

    public void thirdMenu() throws Exception {
        changeScene("third.fxml");
    }

    public void fourthMenu() throws Exception {
        changeScene("fourth.fxml");
    }

    // function to delete files from the user's directory
    // files classData.json, courseHistory.json, courseHistory.txt,
    // degreeRequirment.txt,userData.json,userData.txt
    public void deleteAllFiles() {
        String[] fileNames = { "C:\\Program Files\\ScheduleWorks\\data\\classData.json",
                "C:\\Program Files\\ScheduleWorks\\data\\courseHistory.json",
                "C:\\Program Files\\ScheduleWorks\\data\\courseHistory.txt",
                "C:\\Program Files\\ScheduleWorks\\data\\degreeRequirement.txt",
                "C:\\Program Files\\ScheduleWorks\\data\\userData.json",
                "C:\\Program Files\\ScheduleWorks\\data\\userData.txt" };
        for (String fileName : fileNames) {
            File file = new File(fileName);
            if (file.delete())
                System.out.println(fileName + " deleted successfully.");
            else
                System.out.println(fileName + " does not exist.");
        }
    }
}
