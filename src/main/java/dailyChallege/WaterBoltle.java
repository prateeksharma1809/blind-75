package dailyChallege;

public class WaterBoltle {
	   public int numWaterBottles(int numBottles, int numExchange) {
	        int result = numBottles;
	        int empty = numBottles;
	        while(empty>=numExchange){
	            int newfilled = empty/numExchange;
	            empty = empty%numExchange;
	            result+=newfilled;
	            empty+=newfilled;

	        }
	        return result;
	    }

}
