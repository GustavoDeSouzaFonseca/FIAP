package br.com.fiap.vetores.view;

import javax.swing.JOptionPane;

public class Main {
	public static void main(String[] args) {
		
		
		//RECEBENDO A QUANTIDADE DE PRODUTOS
		int nProd = Integer.parseInt(JOptionPane.showInputDialog("Digite a quantidade de produtos: "));
		
		//RECEBENDO VETOR FORA DO WHILE
		Produto produto[] = new Produto[nProd];
		
		
		
		//DECLARANDO O VETOR DE QUANTIDADE
		int qnt[] = new int[nProd];
		int i = 0;
		while (i<nProd) {
			int quantidade =  Integer.parseInt(JOptionPane.showInputDialog("Digite a quantidade do " + (i+1) +"° Produto: "));
			double preco = Double.parseDouble(JOptionPane.showInputDialog("Digite o preço do " + (i+1) + "° Produto: "));
			double desconto = Double.parseDouble(JOptionPane.showInputDialog("Digite o desconto do " + (i+1) + "° Produto: "));
			
			produto[i] = new Produto(quantidade, preco, desconto);
					
			i ++;
			
		}
		
		

			
			
			
		
	}

}
