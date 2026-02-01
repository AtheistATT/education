package main

import "fmt"

func analyzeGrates(grates []int) (avg float64, maxG int) {

	var total int
	var maxGOut int

	for _, value := range grates {

		total += value

		if maxGOut < value {
			maxG = value
		}

	}

	return float64(total) / float64(len(grates)), maxGOut
}

func main() {

	avg, maxG := analyzeGrates([]int{3, 4, 2, 4, 3, 4, 3})

	fmt.Printf("Средняя оценка: %.2f | Высшая оценка: %d\n", avg, maxG)
}
