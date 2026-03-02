package main

import("fmt"
		"errors")

func CastSpell(mana int)(string, error){
	if mana > 50{
		return "Ринсвинд поднатужившись выпустает чуть теплый шарик.", nil
	}
	if mana > 0{
		return "На пальцах ринсвинда появляются слабые разряды статического электричества", nil
	}
	if mana <= 0{
		return "", errors.New("От отчаяния Ринсвинд произносит восьмое заклинание Октаво и разрушает мир")
	}
	return "", errors.New("Если правила математики в вашем мире уже не работаюст да поможет вам Бог")
}

func main(){

	for{		
		var mana int

		fmt.Println("Введите количество маны Ринсвинда\n>>>")
		fmt.Scan(&mana)
		magicSpell, e := CastSpell(mana)

		if e == nil{
			fmt.Println(magicSpell)
		}else{
			fmt.Println(e.Error())
			break
		}
	}
}
