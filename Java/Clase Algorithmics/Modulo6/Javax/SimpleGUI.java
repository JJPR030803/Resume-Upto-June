package Modulo6.Javax;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SimpleGUI {
    public static void main(String[] args) {
        // Create the main frame (window)
        JFrame frame = new JFrame("Simple GUI Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);

        // Create a panel to hold components
        JPanel panel = new JPanel();

        // Create a button
        JButton button = new JButton("Click Me!");

        // Add an action listener to the button
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Show a message dialog when the button is clicked
                JOptionPane.showMessageDialog(frame, "Button was clicked!");
            }
        });

        // Add the button to the panel
        panel.add(button);

        // Add the panel to the frame
        frame.add(panel);

        // Make the frame visible
        frame.setVisible(true);
    }
}
