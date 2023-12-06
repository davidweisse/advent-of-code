package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getMargin(time, distance int) (margin int) {
	for i := 0; i < time; i++ {
		if i*(time-i) > distance {
			margin++
		}
	}
	return
}

func main() {
	input, _ := os.ReadFile("input.txt")

	data := strings.Fields(string(input))
	times := data[1 : len(data)/2]
	distances := data[len(data)/2+1:]

	product := 1
	for race := range times {
		time, _ := strconv.Atoi(times[race])
		distance, _ := strconv.Atoi(distances[race])
		product *= getMargin(time, distance)
	}

	time, _ := strconv.Atoi(strings.Join(times, ""))
	distance, _ := strconv.Atoi(strings.Join(distances, ""))

	fmt.Println(product)
	fmt.Println(getMargin(time, distance))
}
