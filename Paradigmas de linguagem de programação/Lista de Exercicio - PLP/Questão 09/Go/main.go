package main
import "fmt"

type Imprimivel interface {
    Imprimir()
}

type Relatorio struct {
    Conteudo string
}

func (r Relatorio) Imprimir() {
    fmt.Println("Imprimindo relatório:", r.Conteudo)
}

type Contrato struct {
    Detalhes string
}

func (c Contrato) Imprimir() {
    fmt.Println("Imprimindo contrato:", c.Detalhes)
}

func main() {
    relatorio := Relatorio{Conteudo: "Relatório financeiro"}
    contrato := Contrato{Detalhes: "Contrato de prestação de serviços"}

    relatorio.Imprimir()
    contrato.Imprimir()
}
