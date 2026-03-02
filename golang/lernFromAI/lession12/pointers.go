package main

import "fmt"

type Player struct{
	Name string
	Health int
}

func (p *Player) TakeDamage(damage int){
	p.Health -= damage
}

func (p *Player) IsAlive() bool{
	if p.Health <= 0{
		return false
	}else{
		return true
	}
}

func main(){
	player := Player{Name: "Авантюрист", Health: 100}

	fmt.Println(player.Name + "заходит в игру!")

	player.TakeDamage(20)
	fmt.Printf("Мерзкая крыса наносит %d урона!\n", 20)
	fmt.Printf("Герой выжил? %v \n", player.IsAlive())
	player.TakeDamage(200)
	fmt.Printf("Горный великан наносит %d урона!\n", 200)
	fmt.Printf("Герой выжил? %v \n", player.IsAlive())
	player.TakeDamage(-220)
	fmt.Printf("Приходит паладин и лечит героя на %d единиц!\n", 220)
	fmt.Printf("Теперь герой жив? %v\n", player.IsAlive())

}
