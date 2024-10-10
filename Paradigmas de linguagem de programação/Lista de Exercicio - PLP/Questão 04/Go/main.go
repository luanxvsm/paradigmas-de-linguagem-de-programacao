package main
import "fmt"

type Animal interface {
    Som() string
}

type Cachorro struct{}

func (c Cachorro) Som() string {
    return "Cachorro: AuAu"
}

type Gato struct{}

func (g Gato) Som() string {
    return "Gato: Miau"
}

func FazerSom(a Animal) {
    fmt.Println(a.Som())
}

func main() {

    cachorro := Cachorro{}
    gato := Gato{}

    FazerSom(cachorro)
    FazerSom(gato)
}