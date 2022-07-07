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
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;

/**
* 원하는 단 입력하면 해당하는 구구단 출력
*/
public class Main4 extends Application {
	
	TextField tf;
	TextArea ta;
	
	@Override
	public void start(Stage primaryStage) {
		try {
//			BorderPane root = new BorderPane();
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("main4.fxml"));
			Scene scene = new Scene(root,400,400);
			
			tf = (TextField) scene.lookup("#tf");
			Button btn = (Button) scene.lookup("#btn");
			ta = (TextArea) scene.lookup("#ta");
			
			
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					myclick();
				}
				
			});
			
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void myclick() {
		String a = tf.getText();
		int aa = Integer.parseInt(a);
		
		ta.setText(gugudan(aa));
		
	}
	
	public String gugudan(int dan) {
//		int i = dan;
		
		String result= "";
		
		result += "***" + dan + "단 ***\n";
		
		for(int j = 1; j<10; j++) {
			result += dan + "*" + j + "=" + dan*j + "\n";
		}
		
		return result;
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
