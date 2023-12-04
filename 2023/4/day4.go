package main

import (
	"fmt"
	"os"
	"regexp"
	"slices"
	"strings"
)

func main() {
	input, _ := os.ReadFile("input.txt")

	number := regexp.MustCompile(`\d+`)

	count := []int{}
	sum := 0
	for card, line := range strings.Split(string(input), "\n") {
		count = append(count, 0)
		score := 0
		num := number.FindAllString(line, -1)[1:]
		for _, playerNum := range num[10:] {
			if slices.Contains(num[:10], playerNum) {
				count[card]++
				score *= 2
				if score == 0 {
					score = 1
				}
			}
		}
		sum += score
	}
	fmt.Println(sum)
	cardSum := 0
	cardCount := make([]int, len(count))
	for i, v := range count {
		cardSum += cardCount[i] + 1
		for j := 1; j <= v; j++ {
			cardCount[i+j] += cardCount[i] + 1
		}
	}
	fmt.Println(cardSum)
}
