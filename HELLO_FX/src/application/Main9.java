package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

/**
 * 전화기
 * @author PC-17
 *
 */
public class Main9 extends Application {
	
	Button btn1;
	Button btn2;
	Button btn3;
	Button btn4;
	Button btn5;
	Button btn6;
	Button btn7;
	Button btn8;
	Button btn9;
	Button btn0;
	TextField tf;
	Button btnCall;
	
	
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("main9.fxml"));
			Scene scene = new Scene(root,400,400);
			
			btn1 = (Button) scene.lookup("#btn1");
			btn2 = (Button) scene.lookup("#btn2");
			btn3 = (Button) scene.lookup("#btn3");
			btn4 = (Button) scene.lookup("#btn4");
			btn5 = (Button) scene.lookup("#btn5");
			btn6 = (Button) scene.lookup("#btn6");
			btn7 = (Button) scene.lookup("#btn7");
			btn8 = (Button) scene.lookup("#btn8");
			btn9 = (Button) scene.lookup("#btn9");
			btn0 = (Button) scene.lookup("#btn0");
			btnCall = (Button) scene.lookup("#btn_call");
			tf = (TextField) scene.lookup("#tf");
			
			btn1.setOnMouseClicked(new EventHandler<Event>() {@Override public void handle(Event event) {myClick(event);}});
			btn2.setOnMouseClicked(new EventHandler<Event>() {@Override public void handle(Event event) {myClick(event);}});
			btn3.setOnMouseClicked(new EventHandler<Event>() {@Override public void handle(Event event) {myClick(event);}});
			btn4.setOnMouseClicked(new EventHandler<Event>() {@Override public void handle(Event event) {myClick(event);}});
			btn5.setOnMouseClicked(new EventHandler<Event>() {@Override public void handle(Event event) {myClick(event);}});
			btn6.setOnMouseClicked(new EventHandler<Event>() {@Override public void handle(Event event) {myClick(event);}});
			btn7.setOnMouseClicked(new EventHandler<Event>() {@Override public void handle(Event event) {myClick(event);}});
			btn8.setOnMouseClicked(new EventHandler<Event>() {@Override public void handle(Event event) {myClick(event);}});
			btn9.setOnMouseClicked(new EventHandler<Event>() {@Override public void handle(Event event) {myClick(event);}});
			btn0.setOnMouseClicked(new EventHandler<Event>() {@Override public void handle(Event event) {myClick(event);}});
			
			
			btnCall.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					myCall();
				}


			});
			
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void myCall() {
		String strTel = tf.getText();
		Alert alert = new Alert(AlertType.INFORMATION);
		alert.setTitle("phone");
		alert.setHeaderText("calling");
		alert.setContentText(strTel);
		alert.showAndWait();
	}
	
	public void myClick(Event event) {
		String str_old = tf.getText();
		Button imsi = (Button)event.getSource(); //event는 Object라서 형변환
		String str_new = imsi.getText();
		
		tf.setText(str_old + str_new);
		
	}

	
	
	public static void main(String[] args) {
		launch(args);
	}
}
