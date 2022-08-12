package br.com.fiap.praticas03.view;

import java.util.Iterator;

import javax.swing.JOptionPane;

import br.com.fiap.praticas03.model.Aluno;

public class main03 {
	public static void main(String[] args) {
		//Solicitar a quantidade de alunos
		int quantidade = Integer.parseInt(JOptionPane.showInputDialog("Digite a quantidade de alunos: "));
		
		//Vetor de alunos com n posições
			Aluno[] qntAlunos= new Aluno [quantidade];
			String nome;
			Double maiorNota = 0.0;
			String melhorAluno = null;
		//Vetor de notas 
			double notas[] = new double [3]; 
		
		//Laço de repetição para ler os alunos
			for (int i = 0; i < qntAlunos.length; i ++) {
				
				//Solicitar o nome do aluno
				nome = JOptionPane.showInputDialog("Digite o nome do " + (i + 1) + "° aluno: ");
				for (int j = 0; j < notas.length; j++) {
					notas[j] =	Double.parseDouble(JOptionPane.showInputDialog("Digite a " + (j + 1)+ "º nota"));			
				}
				
				qntAlunos[i] = new Aluno(nome, notas);
			}
			//Verificar o aluno que possui a mior nota
			for (int i = 1; i < qntAlunos.length; i++) {
					maiorNota = qntAlunos[0].maiorNota();
				if (qntAlunos[i].maiorNota() > maiorNota) {
					maiorNota = qntAlunos[i].maiorNota();
					melhorAluno = qntAlunos[i].getNome();
				}	
			}
			JOptionPane.showMessageDialog(null, "O melhor aluno foi o " + melhorAluno +" que tirou " + maiorNota + " como sua maior nota");
			
		
	}

}
