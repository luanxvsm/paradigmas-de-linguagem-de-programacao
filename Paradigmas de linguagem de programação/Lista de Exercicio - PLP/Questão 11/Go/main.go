// Q11) Crie uma classe abstrata Funcionario com um método abstrato
// calcularSalario. Derive classes como FuncionarioHorista e FuncionarioAssalariado que
// implementam calcularSalario de formas distintas

package main

import "fmt"

type Funcionario interface {
    calcularSalario() float64
}

type FuncionarioHorista struct {
    horasTrabalhadas int
    valorPorHora     float64
}

func (f FuncionarioHorista) calcularSalario() float64 {
    return float64(f.horasTrabalhadas) * f.valorPorHora
}

type FuncionarioAssalariado struct {
    salarioFixo float64
}

func (f FuncionarioAssalariado) calcularSalario() float64 {
    return f.salarioFixo
}

func main() {
    horista := FuncionarioHorista{
        horasTrabalhadas: 160,
        valorPorHora:     25,
    }

    assalariado := FuncionarioAssalariado{
        salarioFixo: 3000,
    }

    fmt.Printf("Salário do funcionário horista: %.2f\n", horista.calcularSalario())
    fmt.Printf("Salário do funcionário assalariado: %.2f\n", assalariado.calcularSalario())
}