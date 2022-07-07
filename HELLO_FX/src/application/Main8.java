package application;
	
import java.awt.event.MouseEvent;
import java.util.Random;

import javafx.application.Application;
import javafx.beans.value.ObservableValue;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;

/**
 * 홀짝 게임
 * @author PC-17
 *
 */
public class Main8 extends Application {
	
	TextField tf1;
	TextField tf2;
	TextArea ta;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("main8.fxml"));
			Scene scene = new Scene(root,400,400);
			
			tf1 = (TextField) scene.lookup("#tf1");
			tf2 = (TextField) scene.lookup("#tf2");
			ta = (TextArea) scene.lookup("#ta");
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
		int num1 = Integer.parseInt(tf1.getText());
		int num2 = Integer.parseInt(tf2.getText());
		
		String result = "";
		
		for(int i=num1; i<=num2; i++) {
			result += drawStar(i);
		}
		
		ta.setText(result);
		
	}
	
	public String drawStar(int num) {
		String ret = "";
		for(int i=0; i<num; i++) {
			ret+="*";
		}
		ret+="\n";
		
		return ret;
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
