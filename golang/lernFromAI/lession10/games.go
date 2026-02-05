package main

import "fmt"

type Game struct {
	Title string
	Genre string
	Year  int
}

func main() {
	games := []Game{{Title: "DOOM", Genre: "Shooter", Year: 1993}, {Title: "Morrowind", Genre: "RPG", Year: 2002}, {Title: "TF2", Genre: "Online action", Year: 2007}}

	games = append(games, Game{Title: "Half life", Genre: "Shooter", Year: 1998})

	for index, game := range games {
		fmt.Printf("%d. Игра: %s Жанр: %s Год выхода: %d\n", index+1, game.Title, game.Genre, game.Year)
	}
}
