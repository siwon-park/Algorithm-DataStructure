public class LowerUpperBound {
	
	// lowerBound
	static int lowerBound(int[] arr, int target) {
		int s = 0;
		int e = arr.length - 1;
		int idx = e + 1;
		while (s <= e) {
			int mid = (s + e) / 2;
			if (arr[mid] >= target) {
				e = mid - 1;
				idx = mid;
			} else {
				s = mid + 1;
			}
		}
		return idx;
	}
	
	// upperBound
	static int upperBound(int[] arr, int target) {
		int s = 0;
		int e = arr.length - 1;
		int idx = e + 1;
		while (s <= e) {
			int mid = (s + e) / 2;
			if (arr[mid] > target) {
				e = mid - 1;
				idx = mid;
			} else {
				s = mid + 1;
			}
		}
		
		return idx;
	}
	
 	public static void main(String[] args) throws IOException {

 	}
}