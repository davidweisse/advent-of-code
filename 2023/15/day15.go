package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

type lens struct {
	label       string
	focalLength int
}

func hash(s string) (h uint8) {
	for _, c := range s {
		h = (h + uint8(c)) * 17
	}
	return
}

func main() {
	input, _ := os.ReadFile("input.txt")

	sum := 0
	boxes := make(map[uint8][]lens)
	for _, step := range strings.Split(string(input), ",") {
		sum += int(hash(step))
		label := step[:strings.IndexAny(step, "=-")]
		box := hash(label)
		if step[len(step)-2] == '=' {
			focalLength, _ := strconv.Atoi(string(step[len(step)-1]))
			newLens := lens{label, focalLength}
			if index := slices.IndexFunc(boxes[box], func(l lens) bool {
				return l.label == label
			}); index >= 0 {
				boxes[box] = slices.Replace(boxes[box], index, index+1, newLens)
			} else {
				boxes[box] = append(boxes[box], newLens)
			}
		} else {
			boxes[box] = slices.DeleteFunc(boxes[box], func(l lens) bool {
				return l.label == label
			})
		}
	}
	fmt.Println(sum)
	sumPower := 0
	for i, box := range boxes {
		for j, l := range box {
			sumPower += (int(i) + 1) * (j + 1) * l.focalLength
		}
	}
	fmt.Println(sumPower)
}
