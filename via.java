import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Scanner;

public class via {
	public static void main(String[] args) {
		try {
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		ArrayList<String> array = new ArrayList<String>(); 
		for (int i = 0; i < n; i++) {
			BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
			String str = br.readLine();
			array.add(str);
		}
		for(int i=0;i<array.size();i++){
			String str = array.get(i);
			String[] numbers = str.split(" ");
			String first = numbers[0];
			String second = numbers[1];
			int count = 0;
			while (!first.equals(second)) {
				String temp = first;
				String original = temp;
				String incremented = String.format("%0" + original.length()
						+ "d", Integer.parseInt(original) + 1);
				
				int hr = Integer.parseInt(first.substring(0, 2));
				int min = Integer.parseInt(first.substring(2));
				if (hr >= 00 && hr <= 24 && min >= 00 && min <= 59) {
					int k = 0;
					int j = temp.length()-1;
					while(k<=j){
						if(temp.charAt(k)!=temp.charAt(j)){							
							break;
						} else {
							k++;
							j--;
						}
					}					
					if(k==j+1){
						count = count + 1;
					}
				}				
				first = incremented;
			}
			int k = 0;
			int j = second.length()-1;
			while(k<=j){
				if(second.charAt(k)!=second.charAt(j)){							
					break;
				} else {
					k++;
					j--;
				}
			}					
			if(k==j+1){				
				count = count + 1;
			}
			
			System.out.println(count);
		}
		} catch(Exception e) {
			
		}
			

	}


}