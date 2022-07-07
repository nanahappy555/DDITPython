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
 * 홀짝 게임
 * @author PC-17
 *
 */
public class Main5 extends Application {
	
	TextField tfMine;
	TextField tfCom;
	TextField tfResult;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("main5.fxml"));
			Scene scene = new Scene(root,400,400);
			
			tfMine = (TextField) scene.lookup("#tf_mine");
			tfCom = (TextField) scene.lookup("#tf_com");
			tfResult = (TextField) scene.lookup("#tf_result");
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
		Random random = new Random();

		String mine = tfMine.getText();
		String com = "";
		
		//난수 생성 및 세팅
		int rnd = random.nextInt(2); //0~1 사이
		
		if(rnd == 1) {
			com = "홀";
		} else {
			com = "짝";
		}
		
		//처리
		String result = "";
		if(com.equals(mine)) {
			result = "이김";
		} else {
			result = "짐";
		}
		
		//결과값 세팅
		tfCom.setText(com);
		tfResult.setText(result);
		
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
