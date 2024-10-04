// Q12) Em Python,
// sobrecarregue o operador + para somar dois objetos Produto baseados no preço. Em Java
// e Golang, crie métodos que permitam essa funcionalidade.

package main

import "fmt"

type Produto struct {
    nome  string
    preco float64
}

func (p Produto) Somar(outro Produto) Produto {
    nomeCombinado := p.nome + " & " + outro.nome
    precoCombinado := p.preco + outro.preco
    return Produto{nome: nomeCombinado, preco: precoCombinado}
}

func main() {
    produto1 := Produto{nome: "Produto A", preco: 50}
    produto2 := Produto{nome: "Produto B", preco: 30}

    produtoSoma := produto1.Somar(produto2)
    fmt.Printf("Produto: %s, Preço: %.2f\n", produtoSoma.nome, produtoSoma.preco)
}