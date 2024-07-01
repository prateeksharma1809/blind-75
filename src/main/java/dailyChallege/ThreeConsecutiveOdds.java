package dailyChallege;

public class ThreeConsecutiveOdds {
	
	public boolean threeConsecutiveOdds(int[] arr) {
        int count=0;
        for(int j : arr){
            if(j%2!=0){
                count++;
            }else{
                count=0;
            }
            if(count>=3){
                return true;
            }
        }
        return false;
    }

}
