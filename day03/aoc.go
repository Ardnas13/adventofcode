package main

import (
	"fmt"
	"os"
	"strings"
)

func getSolutionPart1(input []string) int {
	var half = 0
	var result = 0
	for _, value := range input {
		value = string(value)
		half = len(value)/2
		var first = string(value[0:half])
		var second = string(value[half:])
		for _, letter := range first {
			if strings.Contains(second, string(letter)) {
				result += priority(string(letter))
				break
			}
		}
	}
	return result
}

func priority(letter string) int {
	var startingASCIINumberSmall int = 97
	var startingASCIINumberBig int = 65
	alphabet := make(map[string]int)
	for i := 0; i < 26; i++ {
		alphabet[string(rune(startingASCIINumberSmall+i))] = i + 1
	 }
	for i := 0; i < 26; i++ {
		alphabet[string(rune(startingASCIINumberBig+i))] = i + 27
	}
	return alphabet[letter]
}

func checkIfContains(rucksacks []string) int {
	var result = 0
	for _, letter := range rucksacks[0] {
		if strings.Contains(rucksacks[1], string(letter)) && strings.Contains(rucksacks[2], string(letter)) {
			result += priority(string(letter))
			break
		}
	}
	return result
}

func getSolutionPart2(input []string) int {
	var result = 0
	var three []string
	for _, value := range input {
		value = string(value)
		if len(three) == 3 {
			result += checkIfContains(three)
			three = nil
		}
		three = append(three, string(value))
	}
	if len(three) == 3 {
		result += checkIfContains(three)
	}
	return result
}

func parseInput(input string) ([]string, error) {
	var test []string
	lines := strings.Split(strings.TrimSpace(input), "\n")
	for _, line := range lines {
		test = append(test, line)
	}

	return test, nil
}

func main() {
	inputBytes, err := os.ReadFile("input.txt")
	if err != nil {
		panic("couldn't read input 0")
	}

	input, err := parseInput(string(inputBytes))
	if err != nil {
		panic("couldn't parse input 1")
	}

	fmt.Println("Go")
	part := os.Getenv("part")

	if part == "part2" {
		fmt.Println(getSolutionPart2(input))
	} else {
		fmt.Println(getSolutionPart1(input))
	}
}