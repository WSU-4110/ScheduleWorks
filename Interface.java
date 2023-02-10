import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import static javax.swing.WindowConstants.EXIT_ON_CLOSE;

public class Interface {
    private JTextField usernameField;
    private JPanel panelMain;
    private JPasswordField passwordField;
    private JButton loginButton;

    public Interface() {
        loginButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(null, "Login successful");
            }
        });
    }

    public static void main(String[] args) {
        JFrame f = new JFrame("Schedule Works");

        f.setContentPane(new Interface().panelMain);
        f.setDefaultCloseOperation(EXIT_ON_CLOSE);
        f.setSize(1000, 720);
        f.pack();
        f.setVisible(true);
    }
}
