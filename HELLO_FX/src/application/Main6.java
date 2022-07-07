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
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;

/**
 * 로또
 * @author PC-17
 *
 */
public class Main6 extends Application {
	
	Label lbl1;
	Label lbl2;
	Label lbl3;
	Label lbl4;
	Label lbl5;
	Label lbl6;
	
	Random random = new Random();
	
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("main6.fxml"));
			Scene scene = new Scene(root,400,400);
			
			lbl1 = (Label) scene.lookup("#lbl1");
			lbl2 = (Label) scene.lookup("#lbl2");
			lbl3 = (Label) scene.lookup("#lbl3");
			lbl4 = (Label) scene.lookup("#lbl4");
			lbl5 = (Label) scene.lookup("#lbl5");
			lbl6 = (Label) scene.lookup("#lbl6");
			Button btn = (Button) scene.lookup("#btn");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					myClick();
					sem();
				}
				
			});
			
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * 쌤 풀이
	 */
	public void sem() {
		String[] arr9 = {
				"1","2","3","4","5",  "6","7","8","9"
		};
		for(int i=0; i<10; i++) {
			int rnd = random.nextInt(arr9.length-1)+1;
			String temp = arr9[rnd];
			arr9[rnd] = arr9[0];
			arr9[0] = temp;
		}
		
		for(int i=0; i<arr9.length; i++) {
			System.out.println(arr9[i]);
		}
		
	}
	
	public void myClick() {
		
		
		int[] lottos = new int[6];
		for(int i=0; i<lottos.length; i++) {
			lottos[i] = random.nextInt(45)+1; //1~45
			
			for(int k=0; k<i; k++) {
				if(lottos[i] == lottos[k]) {
					i--;
					break;
				}
			}
		}
		
		lbl1.setText(String.valueOf(lottos[0]));
		lbl2.setText(String.valueOf(lottos[1]));
		lbl3.setText(String.valueOf(lottos[2]));
		lbl4.setText(String.valueOf(lottos[3]));
		lbl5.setText(String.valueOf(lottos[4]));
		lbl6.setText(String.valueOf(lottos[5]));
		
		
		
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
