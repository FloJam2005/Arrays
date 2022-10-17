package Q1P2;



public class Feld
{
	
	public static void main(String[] args)
	{
		// Konstanten festlegen, hier maximale Anzahl der Feldelemente
		final int MAXZAHLEN = 20;
		final int MAXZAHL = 100;
		
		
		// Deklaration des Feldes und weitere Variablen
		int zahlen[];
		
		// Allokation  
		zahlen = new int[MAXZAHLEN];
		
		//Initalisieren
		System.out.println("============== Feld initialisieren ================");
		FeldFuellen(zahlen, MAXZAHLEN, 0);
		FeldAusgeben(zahlen);
		
		
		// Zuffallszahlen
		System.out.println("============== Feld initialisieren ================");
		FeldFuellenZufallszahl(zahlen, MAXZAHL);
		FeldAusgeben(zahlen);
	}

	private static void FeldFuellen(int[] zahlen, int mAXZAHLEN, int value)
	{
		for(int i = 0; i<zahlen.length; i++)
		{
			zahlen[i] = value;
		}
		
	}
	
	private static void FeldAusgeben(int[] zahlen)
	{
		for(int i = 0; i<zahlen.length; i++)
		{
			System.out.println(zahlen[i]);
		}
		
	}
	
	private static void FeldFuellenZufallszahl(int[] feld, final int zufallszahl)
	{
		for(int i = 0; i<feld.length; i++)
		{
			feld[i] = (int) (Math.random() * zufallszahl) + 1;
		}
	}
	
	
}
