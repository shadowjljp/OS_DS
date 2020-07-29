package asdf;

import java.util.Arrays;

public class Test {

	public static void main(String[] args) {
		int[][] A = new int[][] {
			{1,1,1,0,0},
			{1,1,1,0,0},
			{1,0,0,0,0},
			{1,1,1,1,0},
			{1,0,0,0,0}
		};
		Test test = new Test();
		test.MaxOneofRow(A);

	}
	public void MaxOneofRow(int[][] A) {
		int row =A.length; 
		int MaxNumOfOne=0;
		int row_index=0;

		
		for(int i=0;i<row;i++) {
			while(MaxNumOfOne<row&&A[i][MaxNumOfOne]==1) {
				MaxNumOfOne++;
				row_index=i+1;
			}
		}
		
		System.out.println("Max row is= "+row_index+", Max count of number  1 is "+MaxNumOfOne);

	}
	
//		int n=5;
//		int[][] A = new int[][] {
//			{1,1,1,0,0},
//			{1,1,1,0,0},
//			{1,0,0,0,0},
//			{1,1,1,1,1},
//			{1,0,0,0,0}
//		};
//		int i=n-1;
//		int j=0;
//		int max_i=0;
//		int numofOneMax=0;
//		
//		while(i>=0 &&j<n) {
//			if(A[i][j]==1) {
//				j=j+1;
//				if(j==n) {
//					numofOneMax=j;
//					max_i=i+1;
//					break;
//				}
//			}else {
//				if(j>numofOneMax) {
//					numofOneMax=j;
//					max_i=i+1;
//				}
//				i=i-1;
//			}
//		}
//		System.out.println("Max row is= "+max_i+", Max number of 1 is "+numofOneMax);
//
//	}

}
