package main

import "fmt"

func main() {
	var salary int = 50000
	var taxRate float32 = 0.13

	res := float32(salary) * (1 - taxRate)

	a := 10
	b := 20

	a, b = b, a

	fmt.Println(res, a, b)
}
