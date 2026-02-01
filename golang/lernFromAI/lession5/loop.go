package main

import "fmt"

func main() {

	for i := 1; i < 21; i++ {
		if i%3 == 0 && i%5 == 0 {
			fmt.Println("Число", i, "- БИНГО!")
		} else if i%3 == 0 {
			fmt.Println("Число", i, "делится на 3")
		} else if i%5 == 0 {
			fmt.Println("Число", i, "делится на 5")
		}
	}
}
