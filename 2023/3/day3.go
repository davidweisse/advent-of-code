package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	input, _ := os.ReadFile("input.txt")

	data := strings.ReplaceAll(string(input), "\n", "")
	number := regexp.MustCompile(`\d+`)
	symbol := regexp.MustCompile(`[^\d\.\r]`)
	lineLength := 141

	sum := 0
	gearSum := 0
	for _, pos := range symbol.FindAllStringIndex(data, -1) {
		symbolRow := pos[0] / lineLength
		symbolCol := pos[0] % lineLength
		count := 0
		ratio := 1
		for _, num := range number.FindAllStringIndex(data, -1) {
			numRow := num[0] / lineLength
			numColStart := num[0] % lineLength
			numColEnd := (num[1] - 1) % lineLength
			if numRow >= symbolRow-1 && numRow <= symbolRow+1 &&
				numColStart <= symbolCol+1 && numColEnd >= symbolCol-1 {
				i, _ := strconv.Atoi(data[num[0]:num[1]])
				sum += i
				count += 1
				ratio *= i
			}
		}
		if data[pos[0]] == '*' && count == 2 {
			gearSum += ratio
		}
	}
	fmt.Println(sum)
	fmt.Println(gearSum)
}
