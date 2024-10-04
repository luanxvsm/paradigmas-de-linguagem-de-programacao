// Q2) Adicione um método acelerar e frear à classe Carro que altere um atributo
// velocidade. Crie um método para exibir a velocidade atual

package main

import "fmt"

type Carro struct {
	Marca     string
	Modelo    string
	Ano       int
	Velocidade int 
}

func (c *Carro) Detalhes() {
	fmt.Printf("Marca: %s, Modelo: %s, Ano: %d\n", c.Marca, c.Modelo, c.Ano)
}

func (c *Carro) Acelerar(incremento int) {
	c.Velocidade += incremento
	fmt.Printf("%s acelerou para %d km/h.\n", c.Modelo, c.Velocidade)
}

func (c *Carro) Frear(decremento int) {
	c.Velocidade -= decremento
	if c.Velocidade < 0 {
		c.Velocidade = 0  // Velocidade mínima é 0
	}
	fmt.Printf("%s freou para %d km/h.\n", c.Modelo, c.Velocidade)
}

func (c *Carro) ExibirVelocidade() {
	fmt.Printf("A velocidade atual do %s é %d km/h.\n", c.Modelo, c.Velocidade)
}

func main() {
	carro1 := Carro{Marca: "Hyundai", Modelo: "HB20x", Ano: 2015}
	carro2 := Carro{Marca: "Fiat", Modelo: "Punto", Ano: 2012}
	carro3 := Carro{Marca: "Ford", Modelo: "EcoSport", Ano: 2019}

	carro1.Detalhes()
	carro2.Detalhes()
	carro3.Detalhes()

	carro1.Acelerar(30)
	carro1.ExibirVelocidade()
	carro1.Frear(10)
	carro1.ExibirVelocidade()

	carro2.Acelerar(50)
	carro2.ExibirVelocidade()
	carro2.Frear(20)
	carro2.ExibirVelocidade()

	carro3.Acelerar(40)
	carro3.ExibirVelocidade()
	carro3.Frear(40)
	carro3.ExibirVelocidade()
}