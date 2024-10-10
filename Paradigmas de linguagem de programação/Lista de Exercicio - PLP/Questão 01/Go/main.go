package main

import "fmt"

type Carro struct {
	Marca  string
	Modelo string
	Ano    int
}

func (c Carro) Detalhes() {
	fmt.Printf("Marca: %s, Modelo: %s, Ano: %d\n", c.Marca, c.Modelo, c.Ano)
}

func main() {
	carro1 := Carro{Marca: "Hyundai", Modelo: "HB20x", Ano: 2015}
	carro2 := Carro{Marca: "Fiat", Modelo: "Punto", Ano: 2012}
	carro3 := Carro{Marca: "Ford", Modelo: "EcoSport", Ano: 2019}

	carro1.Detalhes()
	carro2.Detalhes()
	carro3.Detalhes()
}
