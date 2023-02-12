package main

import "fmt"

type Movie struct {
	name string
	rating float32
}

func getMovie(s string, r float32) (m Movie) {
	m = Movie{
		name: s,
		rating: r,
	}
	return
}

func increaseRating(m *Movie) {
	m.rating += 1.0
}

func main() {
//   m := Movie{name: "ABCD"}
//   var m2 Movie
//   fmt.Printf("%+v", m)
//   fmt.Printf("%+v", m2)

//  fmt.Printf("%+v",getMovie("xyz",3.5))

// mov := getMovie("xyz", 2.0)
// increaseRating(&mov)
// fmt.Printf("%+v", mov)

// mov := getMovie("xyz", 2.0)
// fmt.Println(mov.name)
// fmt.Println(mov.rating)
   mov  := getMovie("xyz", 2.1)
   mov1 := getMovie("abc", 3.3)
   movies := append(append(make([]Movie, 5), mov), mov1)
   for _, value := range movies{
	 fmt.Println(value)
   }

}