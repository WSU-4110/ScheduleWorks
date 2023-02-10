/*----- Displays GUI -----*/

import javax.swing.*;

public class Interface {
    public static void main(String[] args) {
        //  New instance of JFrame
        JFrame f = new JFrame("Schedule Works");

        JButton loginButton = new JButton("Login");
        loginButton.setBounds(130, 100, 100, 40);
        f.add(loginButton);
        f.setSize(1000, 720);
        f.setLayout(null);
        f.setVisible(true);

        //  Note for later: Add a login screen and show everything from the .json
    }
}