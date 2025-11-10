import javax.swing.*;
import java.awt.event.*;
import java.net.*;
import java.io.*;

public class RestApiTester extends JFrame {
    private JTextField urlField = new JTextField("http://");
    private JComboBox<String> methodBox = new JComboBox<>(new String[]{"GET","POST","PUT","DELETE"});
    private JTextArea responseArea = new JTextArea();

    public RestApiTester() {
        setTitle("REST API Tester");
        setSize(600,400);
        setLayout(null);

        urlField.setBounds(20,20,400,25);
        add(urlField);

        methodBox.setBounds(430, 20, 100, 25);
        add(methodBox);

        JButton sendBtn = new JButton("Send");
        sendBtn.setBounds(540, 20, 70, 25);
        add(sendBtn);

        responseArea.setBounds(20, 60, 590, 300);
        add(new JScrollPane(responseArea));
        responseArea.setEditable(false);

        sendBtn.addActionListener(e -> {
            try {
                String urlStr = urlField.getText();
                String method = (String) methodBox.getSelectedItem();
                HttpURLConnection conn = (HttpURLConnection) new URL(urlStr).openConnection();
                conn.setRequestMethod(method);
                BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
                String line;
                StringBuilder content = new StringBuilder();
                while((line=in.readLine()) != null) content.append(line).append("\n");
                responseArea.setText(content.toString());
            } catch(Exception ex) {
                responseArea.setText("Error: " + ex.getMessage());
            }
        });

        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }

    public static void main(String[] args) {
        new RestApiTester();
    }
}
