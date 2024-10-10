package main

import "fmt"

type Empregado struct {
    Nome    string
    Cargo   string
    Salario float64
}

type Empresa struct {
    Empregados []Empregado
}

func (e *Empresa) AdicionarEmpregado(empregado Empregado) {
    e.Empregados = append(e.Empregados, empregado)
}

func main() {
    empresa := Empresa{}
    empresa.AdicionarEmpregado(Empregado{"João", "Desenvolvedor", 3000.00})
    empresa.AdicionarEmpregado(Empregado{"Maria", "Gerente", 5000.00})

    for _, e := range empresa.Empregados {
        fmt.Printf("%s - %s - %.2f\n", e.Nome, e.Cargo, e.Salario)
    }
}
