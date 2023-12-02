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

	colors := map[string]int{"red": 12, "green": 13, "blue": 14}
	re := regexp.MustCompile("([0-9]+) ([a-z]+)")

	sum := 0
	powerSum := 0
	for i, line := range strings.Split(string(input), "\n") {
		min := map[string]int{"red": 1, "green": 1, "blue": 1}
		a := re.FindAllStringSubmatch(line, -1)
		possible := true
		for _, match := range a {
			num, _ := strconv.Atoi(match[1])
			if num > min[match[2]] || min[match[2]] < 0 {
				min[match[2]] = num
			}
			if num > colors[match[2]] {
				possible = false
			}
		}
		if possible {
			sum += i + 1
		}
		powerSum += min["red"] * min["green"] * min["blue"]
	}

	fmt.Println(sum)
	fmt.Println(powerSum)
}
