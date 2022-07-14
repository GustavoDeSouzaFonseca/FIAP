package br.com.fiap.revisao.model;

public class Receita {
	
	private int tempoPreparo;
	private String ingredientes;
	private Doce doce;
	
	public Receita() {}
	
	public Receita(int tempoPreparo, String ingredientes, Doce doce) {
		super();
		this.tempoPreparo = tempoPreparo;
		this.ingredientes = ingredientes;
		this.doce = doce;
	}


	public int getTempoPreparo() {
		return tempoPreparo;
	}


	public void setTempoPreparo(int tempoPreparo) {
		this.tempoPreparo = tempoPreparo;
	}


	public String getIngredientes() {
		return ingredientes;
	}


	public void setIngredientes(String ingredientes) {
		this.ingredientes = ingredientes;
	}


	public Doce getDoce() {
		return doce;
	}


	public void setDoce(Doce doce) {
		this.doce = doce;
	}
	
	
	
	
	

}
