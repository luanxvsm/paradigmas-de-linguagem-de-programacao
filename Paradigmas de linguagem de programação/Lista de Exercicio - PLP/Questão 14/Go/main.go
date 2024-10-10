package main
import (
    "fmt"
    "sync"
)

type Configuracao struct{}

var instance Configuracao
var once sync.Once

func GetInstance()Configuracao {
    once.Do(func() {
        instance = Configuracao{}
    })
    return instance
}

func main() {
    config1 := GetInstance()
    config2 := GetInstance()

    fmt.Println(config1 == config2)  // true
}