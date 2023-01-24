package main

import "fmt"

func main() {
	arr := [3]int{10,20,30}
	fmt.Println(arr)
	modify1(arr)
	fmt.Println(arr)
}

func modify1(numbers[3]int){
	for i := range numbers{
		numbers[i] -= 5
	}
}

