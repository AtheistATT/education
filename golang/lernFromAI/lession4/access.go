package main

import "fmt"

func main() {

	role := "admin"
	age := 20

	if role == "admin" {
		fmt.Println("Полный доступ разрешен")
	} else {
		if role == "user" && age >= 18 {
			fmt.Println("Ограниченый доступ разрешен")
		} else {
			fmt.Println("Доступ запрещен")
		}
	}

}
