package main

import "fmt"

type Shouter interface{
	Shout()
}

type Human struct{
	Name string
}

type Monster struct{
	Type string
}

func (h Human) Shout(){
	fmt.Printf("Меня зовут %s, помогите!\n", h.Name)
}

func (m Monster) Shout(){
	fmt.Printf("ГРРРРРРР! Я %s!\n", m.Type)
}

func Intro(s Shouter){
	fmt.Print("Кто-то кричит: ")
	s.Shout()
}

func main(){
	u1 := Human{Name: "Ринсвинд"}
	u2 := Monster{Type: "Белшамгарот"}

	Intro(u1)
	Intro(u2)
}
