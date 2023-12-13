package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

var cache map[string]int

func arrangements(springs string, info []int) (sum int) {
	if len(springs) == 0 {
		if len(info) == 0 {
			return 1
		}
		return 0
	}
	if len(info) == 0 {
		if strings.Contains(springs, "#") {
			return 0
		}
		return 1
	}

	key := fmt.Sprint(springs, info)
	if v, ok := cache[key]; ok {
		return v
	}

	newInfo := make([]int, len(info)-1)

	if springs[0] == '.' || springs[0] == '?' {
		sum += arrangements(strings.Clone(springs[1:]), info)
	}

	if springs[0] == '#' || springs[0] == '?' {
		if info[0] <= len(springs) &&
			!strings.Contains(springs[:info[0]], ".") {
			copy(newInfo, info[1:])
			if info[0] == len(springs) {
				sum += arrangements("", newInfo)
			} else if springs[info[0]] != '#' {
				sum += arrangements(strings.Clone(springs[info[0]+1:]), newInfo)
			}
		}
	}

	cache[key] = sum
	return
}

func main() {
	input, _ := os.ReadFile("input.txt")

	sumOne := 0
	sumTwo := 0
	cache = make(map[string]int)
	for _, line := range strings.Split(string(input), "\n") {
		row := strings.Fields(line)
		springs := row[0]
		info := []int{}
		for _, v := range strings.Split(row[1], ",") {
			num, _ := strconv.Atoi(v)
			info = append(info, num)
		}
		sumOne += arrangements(springs, info)
		springs = strings.Join([]string{springs, springs, springs, springs, springs}, "?")
		oldInfo := make([]int, len(info))
		copy(oldInfo, info)
		for i := 0; i < 4; i++ {
			info = append(info, oldInfo...)
		}
		sumTwo += arrangements(springs, info)
	}
	fmt.Println(sumOne)
	fmt.Println(sumTwo)
}
