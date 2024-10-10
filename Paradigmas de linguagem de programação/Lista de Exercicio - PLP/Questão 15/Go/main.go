package main
import (
    "errors"
    "fmt"
)

type ContaBancaria struct {
    saldo float64
}

func (c *ContaBancaria) Sacar(valor float64) error {
    if valor > c.saldo {
        return errors.New("saldo insuficiente para realizar o saque")
    }
    c.saldo -= valor
    return nil
}

func main() {
    conta := ContaBancaria{saldo: 100}
    err := conta.Sacar(150)
    if err != nil {
        fmt.Println(err)
    }
}