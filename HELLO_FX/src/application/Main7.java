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
 * 가위바위보 게임
 * @author PC-17
 *
 */
public class Main7 extends Application {
	
	TextField tfMine;
	TextField tfCom;
	TextField tfResult;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("main7.fxml"));
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
		int rnd = random.nextInt(3); //0~2 사이
		
		if(rnd == 0) {
			com = "가위";
		} else if(rnd == 1) {
			com = "바위";
		} else {
			com = "보";
		}
		
		//처리
		String result = "";
		if(com.equals(mine)) {
			result = "비김";
		} else if(com.equals("가위") && mine.equals("바위")
				||com.equals("바위") && mine.equals("보")
				||com.equals("보") && mine.equals("가위")) {
			result = "내가 이김";
		} else {
			result = "컴퓨터 이김";
		}
		
		//결과값 세팅
		tfCom.setText(com);
		tfResult.setText(result);
		
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
