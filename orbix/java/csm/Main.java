import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class SnippetManager extends Application {
    @Override
    public void start(Stage stage) {
        ListView<String> snippetList = new ListView<>();
        TextArea snippetContent = new TextArea();
        TextField snippetTitle = new TextField();
        Button addBtn = new Button("Add Snippet");

        addBtn.setOnAction(e -> {
            String title = snippetTitle.getText();
            // Save snippet to database (pseudo code)
            // db.saveSnippet(title, snippetContent.getText());
            snippetList.getItems().add(title);
        });

        VBox root = new VBox(snippetTitle, snippetContent, addBtn, snippetList);
        Scene scene = new Scene(root, 600, 400);
        stage.setScene(scene);
        stage.setTitle("Code Snippet Manager");
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
