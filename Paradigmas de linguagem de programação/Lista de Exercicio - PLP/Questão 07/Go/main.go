package main
import "fmt"

type Professor struct {
    Nome    string
    Escolas []*Escola
}

func (p *Professor) AdicionarEscola(escola *Escola) {
    p.Escolas = append(p.Escolas, escola)
}

type Escola struct {
    Nome       string
    Professores []*Professor
}

func (e *Escola) AdicionarProfessor(professor *Professor) {
    e.Professores = append(e.Professores, professor)
    professor.AdicionarEscola(e)
}

func main() {
    escola1 := &Escola{Nome: "Escola A"}
    escola2 := &Escola{Nome: "Escola B"}

    professor1 := &Professor{Nome: "Professor X"}
    professor2 := &Professor{Nome: "Professor Y"}

    escola1.AdicionarProfessor(professor1)
    escola2.AdicionarProfessor(professor1)
    escola1.AdicionarProfessor(professor2)

    fmt.Printf("%s leciona em: %s e %s\n", professor1.Nome, professor1.Escolas[0].Nome, professor1.Escolas[1].Nome)
    fmt.Printf("%s tem os professores: %s e %s\n", escola1.Nome, escola1.Professores[0].Nome, escola1.Professores[1].Nome)
}
