package br.com.fiap.vetores.view;

import javax.swing.JOptionPane;

public class Exemplo01 {
	public static void main(String[] args) {
		//Declarar vetor de NOMES
		String nomes[] = new String[5];
		
		//Adicionar os nomes no vetor (usuário digita)
		
		int b = 1;
		int c = 0;
		while (c<nomes.length) {
			nomes[c] = JOptionPane.showInputDialog("Digite o " + b + "° nome: ");
			b ++;
			c ++; 
		}
		
		//Criar um laço de repetição e exibir os nomes do vetor
		int i = 0;
		while(i<nomes.length) {
			JOptionPane.showConfirmDialog(null, "O "+ (i+1) +" nome é " + nomes[i].toUpperCase());
			i ++;
		}
		
//		//USANDO FOR
//		for(int e = 0; e < nomes.length; e++) {
//			System.out.println(nomes[e]);
//		}
		
	}

}
