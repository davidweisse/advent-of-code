package main

import (
	"fmt"
	"os"
	"regexp"
	"slices"
	"strings"
)

func count(data []string, nums []string) int {
	first := regexp.MustCompile(strings.Join(nums, "|"))
	last := regexp.MustCompile(".*(" + strings.Join(nums, "|") + ")")
	sum := 0
	for _, s := range data {
		sum += 10 * (slices.Index(nums, first.FindString(s))%9 + 1)
		sum += slices.Index(nums, last.FindStringSubmatch(s)[1])%9 + 1
	}
	return sum
}

func main() {
	input, _ := os.ReadFile("input.txt")

	data := strings.Fields(string(input))

	nums := []string{"1", "2", "3", "4", "5", "6", "7", "8", "9",
		"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}

	// fmt.Println(count(data, nums[:9]))
	fmt.Println(count(data, nums))
}
