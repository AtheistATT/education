package main

import "fmt"

func main() {
	grades := []int{5, 4, 3, 2, 5}

	grades = append(grades, 4)
	var sum int
	var maxG int

	for _, value := range grades {

		sum += value

		if maxG < value {
			maxG = value
		}
	}

	fmt.Println(float64(sum) / float64(len(grades)))

}
