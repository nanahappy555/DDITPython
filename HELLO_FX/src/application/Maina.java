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
 * x부터 y까지 z의 배수의 합을 구하기
 * @author PC-17
 *
 */
public class Maina extends Application {
	
	TextField tf1;
	TextField tf2;
	TextField tf3;
	TextField tf4;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("maina.fxml"));
			Scene scene = new Scene(root,400,400);
			
			tf1 = (TextField) scene.lookup("#tf1");
			tf2 = (TextField) scene.lookup("#tf2");
			tf3 = (TextField) scene.lookup("#tf3");
			tf4 = (TextField) scene.lookup("#tf4");
			
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
		int x = Integer.parseInt(tf1.getText());
		int y = Integer.parseInt(tf2.getText());
		int z = Integer.parseInt(tf3.getText());
		
		int result = 0;
		
		//x부터 y까지 z의 배수의 합을 구하기
		//2부터 5까지 3의 배수의 합 2<=n<=5,n%3 = 0
		for(int i=x; i<=y; i++) {
			if(i%z == 0) {
				result += i;
			}
		}
		
		tf4.setText(String.valueOf(result));
	}

	
	
	public static void main(String[] args) {
		launch(args);
	}
}
