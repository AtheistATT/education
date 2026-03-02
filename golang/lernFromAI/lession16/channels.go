package main

import "fmt"

func SeachBook(libreirianName string, bookTitle string, ch chan string){
	result := fmt.Sprintf("%s нашел книгу %s\n", libreirianName, bookTitle)
	ch <- result
}

func main(){
	channel := make(chan string)

	go SeachBook("Моркоу", "Сборник законов Анк-Морпорка", channel)
	go SeachBook("Чудакулли", "Настольная книга охотника и рыболова с большим магическим потенциалом", channel)
	go SeachBook("Ветинари", "Государь Макиавелли", channel)

	fmt.Println(<-channel)
	fmt.Println(<-channel)
	fmt.Println(<-channel)

}
