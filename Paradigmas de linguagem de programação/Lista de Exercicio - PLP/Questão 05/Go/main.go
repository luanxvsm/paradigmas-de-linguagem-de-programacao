package main
import "fmt"

type Animal interface {
    Som() string
}

type Vaca struct{}
func (c Vaca) Som() string {
    return "Vaca: Muuu"
}

type Cabra struct{}
func (g Cabra) Som() string {
    return "Cabra: Béééé"
}

func FazerSomAnimais(animais []Animal) {
    for _, animal := range animais {
        fmt.Println(animal.Som())
    }
}

func main() {
    animais := []Animal{Vaca{}, Cabra{}}
    FazerSomAnimais(animais)
}
