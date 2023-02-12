package main

import (
	"fmt"
)

type circle struct {
	radius float64
	area float64
}

func (c *circle) calcArea(){
	c.area = 3.14 * c.radius * c.radius
}

func main() {
	c1 := circle{
		radius: 3,
	}
	c1.calcArea()
	fmt.Println(c1)
}