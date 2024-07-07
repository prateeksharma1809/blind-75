package dailyChallege;

public class Pillow {
	public int passThePillow(int n, int time) {
        int m = (time-1)%(n-1);
        if(((time-1)/(n-1))%2==0){
            return m+2;
        }else{
            return n-(m+1);
        }
    }

}
