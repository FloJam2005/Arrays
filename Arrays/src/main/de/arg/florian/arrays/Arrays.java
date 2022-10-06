package main.de.arg.florian.arrays;

public class Arrays
{

	public static void main(String[] args)
	{
		int matrix[][] = new int[3][3];
		
		

	}
	
	
	
	/**
	 *  Ueberprueft ob eine 3x3 Matrix loesbar ist
	 *  
	 * @param matrix 3x3 int array
	 * @return true wenn loesbar sonst false
	 */
	public static boolean isLoesbar(int matrix[][])
	{
		int det[][] = new int [3][5];
		
		//Arrays quasi kopieren / erweitern auf die zwei benötigten zusätzlichen Spalten, 4. Spalte = 1. Spalte & 5. Spalte = 2. Spalte
		det[0][0] = matrix[0][0];
		det[0][1] = matrix[0][1];
		det[0][2] = matrix[0][2];
		det[1][0] = matrix[1][0];
		det[1][1] = matrix[1][1];
		det[1][2] = matrix[1][2];
		det[2][0] = matrix[2][0];
		det[2][1] = matrix[2][1];
		det[2][2] = matrix[2][2];
		
		// Erweitert
		det[0][3] = matrix[0][0];
		det[1][3] = matrix[0][1];
		det[2][3] = matrix[0][2];
		det[0][4] = matrix[1][0];
		det[1][4] = matrix[1][1];
		det[2][4] = matrix[1][2];
		
		//Sarrussche Regel:
		int a = det[0][0] * det[1][1] * det[2][2];
		int b = det[0][1] * det[1][2] * det[2][3];
		int c = det[0][2] * det[1][3] * det[2][4];
		
		int d = det[0][4] * det[1][3] * det[2][2];
		int e = det[0][3] * det[1][2] * det[2][1];
		int f = det[0][2] * det[1][1] * det[2][0];
		
		
		if ((a+b+c - (d+e+f)) != 0)
		{
			return true;
		}
		
		
		
		return false;		
	}
	
	
	

}
