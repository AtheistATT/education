package main

import (
	"fmt"
	"time"
)

func SeachBook(librarianName string, bookTitle string){
	time.Sleep(time.Second * 2)
	fmt.Printf("%s нашел книгу '%s'\n", librarianName, bookTitle)
}

func main(){
go SeachBook("Гораций", "Книга точных предсказаний Агнессы Псих")
go SeachBook("Ринсвинд", "Октаво")
go SeachBook("Шноби Шнобс", "Книга из резервуара со льдос с огромной надписью 'ДОЗВОЛЕНО ЧИТАТЬ ТОЛЬКО МАГАМ СТАРШЕ 200 ЛЕТ (ЖЕЛАТЕЛЬНО МЕРТВЫМ)'")

time.Sleep(time.Second * 3)
}
