package main

import "fmt"

type ContaBancaria struct {
	titular string
	saldo   float64
}

func (c *ContaBancaria) ExibirSaldo() float64 {
	return c.saldo
}

func (c *ContaBancaria) Depositar(valor float64) {
	if valor > 0 {
		c.saldo += valor
		fmt.Printf("Depositados R$%.2f na conta de %s.\n", valor, c.titular)
	} else {
		fmt.Println("Valor inválido para depósito.")
	}
}

func (c *ContaBancaria) Sacar(valor float64) {
	if valor > 0 && valor <= c.saldo {
		c.saldo -= valor
		fmt.Printf("Sacados R$%.2f da conta de %s.\n", valor, c.titular)
	} else if valor > c.saldo {
		fmt.Println("Saldo insuficiente para o saque.")
	} else {
		fmt.Println("Valor inválido para saque.")
	}
}

func main() {
	conta := ContaBancaria{titular: "Luan", saldo: 1700.00}

	fmt.Printf("Saldo inicial de %s: R$%.2f\n", conta.titular, conta.ExibirSaldo())

	conta.Depositar(500.00)
	fmt.Printf("Saldo após depósito: R$%.2f\n", conta.ExibirSaldo())

	conta.Sacar(300.00)
	fmt.Printf("Saldo após saque: R$%.2f\n", conta.ExibirSaldo())

	conta.Sacar(2000.00)
	fmt.Printf("Saldo após tentativa de saque: R$%.2f\n", conta.ExibirSaldo())
}
