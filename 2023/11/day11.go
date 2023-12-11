package main

import (
	"fmt"
	"os"
	"regexp"
	"slices"
	"strings"
)

func expand(data [][]int, n int) (expanded [][]int) {
	for _, v := range data {
		entry := make([]int, 2)
		copy(entry, v)
		expanded = append(expanded, entry)
	}
	expandFunc(expanded, n, 0)
	slices.SortFunc(expanded, func(a, b []int) int {
		return a[1] - b[1]
	})
	expandFunc(expanded, n, 1)
	return
}

func expandFunc(data [][]int, n, k int) {
	previous := 0
	constant := 0
	for i, loc := range data {
		if loc[k] > previous+1 {
			constant += loc[k] - previous - 1
		}
		previous = loc[k]
		data[i][k] += constant * (n - 1)
	}
}

func calc(data [][]int) (sum int) {
	for i := 0; i < len(data); i++ {
		for j := i + 1; j < len(data); j++ {
			if data[i][0] < data[j][0] {
				sum += data[j][0] - data[i][0] + data[j][1] - data[i][1]
			} else {
				sum += data[i][0] - data[j][0] + data[j][1] - data[i][1]
			}
		}
	}
	return
}

func main() {
	input, _ := os.ReadFile("input.txt")

	re := regexp.MustCompile(`#`)
	data := [][]int{}
	for row, line := range strings.Fields(string(input)) {
		matches := re.FindAllStringIndex(line, -1)
		for _, match := range matches {
			data = append(data, []int{row, match[0]})
		}
	}

	fmt.Println(calc(expand(data, 2)))
	fmt.Println(calc(expand(data, 1000000)))
}
