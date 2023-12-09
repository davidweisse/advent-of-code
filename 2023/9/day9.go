package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getNext(nums []int, prev bool) int {
	zero := true
	for _, v := range nums {
		if v != 0 {
			zero = false
		}
	}
	if zero {
		return 0
	}
	newNums := []int{}
	for i := 0; i < len(nums)-1; i++ {
		newNums = append(newNums, nums[i+1]-nums[i])
	}
	if prev {
		return nums[0] - getNext(newNums, true)
	} else {
		return nums[len(nums)-1] + getNext(newNums, false)
	}
}

func main() {
	input, _ := os.ReadFile("input.txt")

	nextSum, prevSum := 0, 0
	for _, line := range strings.Split(string(input), "\n") {
		data := []int{}
		nums := strings.Fields(line)
		for _, v := range nums {
			num, _ := strconv.Atoi(v)
			data = append(data, num)
		}
		nextSum += getNext(data, false)
		prevSum += getNext(data, true)
	}
	fmt.Println(nextSum)
	fmt.Println(prevSum)
}
