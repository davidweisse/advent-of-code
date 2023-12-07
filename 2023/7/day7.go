package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func getType(hand string, joker bool) (max int) {
	chars := "J23456789TQKA"
	jokerPossibilities := 1
	if joker && strings.ContainsRune(hand, 'J') {
		jokerPossibilities = len(chars)
	}
	for i := 0; i < jokerPossibilities; i++ {
		count := make([]int, 5)
		labels := map[rune]int{}
		for _, c := range strings.ReplaceAll(hand, "J", string(chars[i])) {
			index, exists := labels[c]
			if !exists {
				index = len(labels)
				labels[c] = index
			}
			count[index]++
		}
		slices.Sort(count)
		if 2*count[4]+count[3]-3 > max {
			max = 2*count[4] + count[3] - 3
		}
	}
	return
}

func getSum(data []string, joker bool) (sum int) {
	strength := map[byte]int{'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5,
		'8': 6, '9': 7, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
	if joker {
		strength['J'] = -1
	}

	order := [][]int{}
	for i := 0; i < len(data); i += 2 {
		order = append(order, []int{i / 2, getType(data[i], joker)})
	}
	slices.SortFunc(order, func(a, b []int) int {
		if a[1] != b[1] {
			return a[1] - b[1]
		}
		for i := 0; i < 5; i++ {
			if data[2*a[0]][i] != data[2*b[0]][i] {
				return strength[data[2*a[0]][i]] - strength[data[2*b[0]][i]]
			}
		}
		return 0
	})
	for i, v := range order {
		bid, _ := strconv.Atoi(data[2*v[0]+1])
		sum += (i + 1) * bid
	}
	return
}

func main() {
	input, _ := os.ReadFile("input.txt")

	data := strings.Fields(string(input))

	fmt.Println(getSum(data, false))
	fmt.Println(getSum(data, true))
}
