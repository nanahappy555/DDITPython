package application;
	
import java.awt.event.MouseEvent;

import javafx.application.Application;
import javafx.beans.value.ObservableValue;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;


public class Main2 extends Application {
	
	TextField tf;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("main2.fxml"));
			Scene scene = new Scene(root,400,400);
			
			tf = (TextField) scene.lookup("#tf");
			
			Button btn = (Button) scene.lookup("#btn");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					myClick();
				}
				
			});
			
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void myClick() {
		String a = tf.getText();
		int aa = Integer.parseInt(a);
		aa++;
		tf.setText(String.valueOf(aa));
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
