package br.com.fiap.condicionais.view;

import javax.swing.JOptionPane;

public class Exemplo02 {

	//Criar uma calculadora
	public static void main(String[] args) {
		//Ler dois números
		int n1 = Integer.parseInt(JOptionPane.showInputDialog("Digite um número"));
		int n2 = Integer.parseInt(JOptionPane.showInputDialog("Digite outro número"));
		
		//Pedir a operação para o usuário (+, -, *, /)
		String operador = JOptionPane.showInputDialog("Digite a operação");
		
		//CTRL + / -> comenta as linhas selecionadas
		//Realizar a operação e exibir a resposta
		switch(operador) {
		case "+":
			JOptionPane.showMessageDialog(null, "A soma é: " + (n1 + n2));
			break;
		case "-":
			JOptionPane.showMessageDialog(null, "A subtração é: " + (n1 - n2));
			break;
		case "*":
			JOptionPane.showMessageDialog(null, "A multiplicação é: " + (n1 * n2));
			break;
		case "/":
			JOptionPane.showMessageDialog(null, "A divisão é: " + (n1 /n2));
			break;
		default:
			JOptionPane.showMessageDialog(null, "Operação inválida");
		}
		
	}//main
}//class