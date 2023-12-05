package main

import (
	"fmt"
	"os"
	"regexp"
	"slices"
	"strconv"
	"strings"
)

type state struct {
	dest   int
	source int
	length int
}

func findLocation(seed int, data [][]state) int {
	dest := seed
	for _, stage := range data {
		for _, mapping := range stage {
			if seed >= mapping.source && seed < mapping.source+mapping.length {
				dest = mapping.dest + seed - mapping.source
				seed = dest
				break
			}
		}
	}
	return dest
}

func main() {
	input, _ := os.ReadFile("input.txt")

	rawData := strings.Split(string(input), "\n")

	seedRe := regexp.MustCompile(`\d+`)
	seedsStr := seedRe.FindAllString(rawData[0], -1)
	seeds := make([]int, len(seedsStr))
	for i, v := range seedsStr {
		seedNum, _ := strconv.Atoi(v)
		seeds[i] = seedNum
	}

	numsRe := regexp.MustCompile(`\d+`)
	data := [][]state{}
	currentStage := -1
	for i := 1; i < len(rawData); i++ {
		if nums := numsRe.FindAllString(rawData[i], -1); len(rawData[i]) != 1 {
			dest, _ := strconv.Atoi(nums[0])
			source, _ := strconv.Atoi(nums[1])
			length, _ := strconv.Atoi(nums[2])
			newState := state{dest, source, length}
			data[currentStage] = append(data[currentStage], newState)
		} else {
			data = append(data, []state{})
			currentStage++
			i++
		}
	}

	locations := []int{}
	for _, v := range seeds {
		locations = append(locations, findLocation(v, data))
	}
	fmt.Println(slices.Min(locations))

	for i := 0; i < len(seeds); i += 2 {
		seeds[i+1] += seeds[i]
	}

	for _, stage := range data {
		newSeeds := []int{}
		for len(seeds) > 0 {
			seedStart := seeds[0]
			seedEnd := seeds[1]
			seeds = seeds[2:]
			found := false
			for _, v := range stage {
				overlapStart := max(seedStart, v.source)
				overlapEnd := min(seedEnd, v.source+v.length)
				if overlapStart < overlapEnd {
					found = true
					newSeeds = append(newSeeds, overlapStart-v.source+v.dest, overlapEnd-v.source+v.dest)
					if overlapStart > seedStart {
						seeds = append(seeds, seedStart, overlapStart)
					}
					if seedEnd > overlapEnd {
						seeds = append(seeds, overlapEnd, seedEnd)
					}
					break
				}
			}
			if !found {
				newSeeds = append(newSeeds, seedStart, seedEnd)
			}
		}
		seeds = make([]int, len(newSeeds))
		copy(seeds, newSeeds)
	}
	fmt.Println(slices.Min(seeds))
}
