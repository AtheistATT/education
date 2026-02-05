package main

import "fmt"

func main() {

	phonebook := make(map[string]string)

	phonebook["deadpool"] = "666869666"
	phonebook["BG"] = "2128506"
	phonebook["Arthor"] = "Camelot is a stupit sity"

	_, ok := phonebook["Arthor"]

	if ok {
		delete(phonebook, "Arthor")
	}

	_, ok1 := phonebook["Дмитрий"]

	if !ok1 {
		fmt.Println("Дмитрий не найден!")
	}

	for key, value := range phonebook {
		fmt.Printf("Имя: %s Номер: %s\n", key, value)
	}

}
