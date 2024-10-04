// Q10) Implemente uma classe Calculadora com métodos somar que aceita diferentes números
// de parâmetros (dois ou três números). Em Golang, use funções com nomes diferentes
// para diferentes quantidades de parâmetros

package main

import "fmt"

type Calculadora struct{}

func (c Calculadora) SomarDois(a int, b int) int {
    return a + b
}

func (c Calculadora) SomarTres(a int, b int, c1 int) int {
    return a + b + c1
}

func main() {
    calc := Calculadora{}
    
    resultado1 := calc.SomarDois(5, 10)
    fmt.Println("Soma de 5 + 10 =", resultado1)

    resultado2 := calc.SomarTres(5, 10, 15)
    fmt.Println("Soma de 5 + 10 + 15 =", resultado2)
}
