package main

import "fmt"

func main() {
	var num1 float64
	var num2 float64
	var operator string

	fmt.Scan(&num1, &operator, &num2)

	switch operator {
	case "+":
		fmt.Println(num1 + num2)
	case "-":
		fmt.Println(num1 - num2)
	case "*":
		fmt.Println(num1 * num2)
	case "/":
		if num2 == 0 {
			fmt.Println("♾️")
		} else {
			fmt.Printf("%.2f\n", num1/num2)
		}
	}

}
