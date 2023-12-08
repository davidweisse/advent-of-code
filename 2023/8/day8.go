package main

import (
	"fmt"
	"os"
	"regexp"
	"slices"
	"strings"
)

func getSteps(start string, end []string, instructions string, network map[string][]string) (steps int) {
	current := start
	for i := 0; !slices.Contains(end, current); i = (i + 1) % len(instructions) {
		lr := 0
		if instructions[i] == 'R' {
			lr = 1
		}
		current = network[current][lr]
		steps++
	}
	return
}

func gcd(a, b int) int {
	if a == 0 {
		return b
	}
	return gcd(b%a, a)
}

func lcm(nums ...int) int {
	if len(nums) == 1 {
		return nums[0]
	} else if len(nums) == 2 {
		return (nums[0] / gcd(nums[0], nums[1])) * nums[1]
	}
	return lcm(nums[0], lcm(nums[1:]...))
}

func main() {
	input, _ := os.ReadFile("input.txt")

	lines := strings.Split(string(input), "\r\n")
	instructions := lines[0]
	network := map[string][]string{}

	lineRe := regexp.MustCompile(`(\w+) = \((\w+), (\w+)\)`)

	for _, line := range lines[2:] {
		nodes := lineRe.FindStringSubmatch(line)[1:]
		network[nodes[0]] = []string{nodes[1], nodes[2]}
	}

	start := []string{}
	end := []string{}
	for key := range network {
		if key[2] == 'A' {
			start = append(start, key)
		} else if key[2] == 'Z' {
			end = append(end, key)
		}
	}
	fmt.Println(getSteps("AAA", []string{"ZZZ"}, instructions, network))
	stepsArr := []int{}
	for _, startNode := range start {
		stepsArr = append(stepsArr, getSteps(startNode, end, instructions, network))
	}
	fmt.Println(lcm(stepsArr...))
}
