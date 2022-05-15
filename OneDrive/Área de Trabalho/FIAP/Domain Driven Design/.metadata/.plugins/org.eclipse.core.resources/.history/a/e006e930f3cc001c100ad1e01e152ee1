package br.com.fiap.condicionais.view;

import javax.swing.JOptionPane;

public class Exemplo01 {

	public static void main(String[] args) {
		//Ler um número  
		int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite um número ae"));

		//Não é necessário a chaves quando tiver uma 
		//única instrução dentro do if ou else
		
		//verificar se é par ou ímpar
		if (numero % 2 == 0) 
			JOptionPane.showMessageDialog(null, "O número é par");
		else  
			JOptionPane.showMessageDialog(null, "O número é ímpar");
		
		//Ler a idade
		int idade = Integer.parseInt(JOptionPane.showInputDialog("Digite a idade"));
				
		//Verificar se deve ou não votar
		// entre 16 e 18 ou maior de 65- Opcional
		// Menor de 16 - não vota
		// 18 e 65 - obrigatório
		if (idade >= 16 && idade < 18 || idade >= 65) {
			JOptionPane.showMessageDialog(null, "O voto é opcional");
		} else if (idade >= 18) {
			JOptionPane.showMessageDialog(null, "O voto é obrigatório");
		} else {
			JOptionPane.showMessageDialog(null, "Não pode votar");
		}
				
	}
}