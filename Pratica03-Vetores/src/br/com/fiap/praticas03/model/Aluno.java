package br.com.fiap.praticas03.model;

public class Aluno {
	
	private String nome;
	
	//Vetor que armazena as 3 notas do aluno
	private double notas[] = new double[3];

	//CTRL + 3 -> ggas e gcuf
	
	//Construtor
	public Aluno(String nome, double[] notas) {
		super();
		this.nome = nome;
		this.notas = notas;
	}
	
	//Criar um método que retorna a maior nota do aluno
	public double maiorNota() {
		double maior = notas[0];
		for (int i = 1; i < notas.length; i++) {
			if (notas[i] > maior)
				maior = notas[i];
		}
		return maior;
	}

	//Getters and Setters
	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public double[] getNotas() {
		return notas;
	}

	public void setNotas(double[] notas) {
		this.notas = notas;
	}
	
	

}
