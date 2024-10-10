package main
import "fmt"

type Motor struct {
    Potencia int
}

type Carro struct {
    Motor Motor
}

func main() {
    motor := Motor{Potencia: 310}
    carro := Carro{Motor: motor}
    fmt.Println("Potência do motor:", carro.Motor.Potencia)
}
