package main

import (
	"fmt"
	"time"
)

type Game struct {
	Title string
	Genre string
	Year  int
}

func (g Game) PrintInfo() {
	fmt.Printf("Игра: %s Жанр: %s Год выхода: %d Возраст: %d\n", g.Title, g.Genre, g.Year, g.Age())
}

func (g Game) Age() int {
	t := time.Now()
	return t.Year() - g.Year
}

func main() {
	games := []Game{{Title: "DOOM", Genre: "Shooter", Year: 1993}, {Title: "Morrowind", Genre: "RPG", Year: 2002}, {Title: "TF2", Genre: "Online action", Year: 2007}}

	games = append(games, Game{Title: "Half life", Genre: "Shooter", Year: 1998})

	for _, game := range games {
		game.PrintInfo()
	}
}
