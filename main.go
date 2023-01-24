package main
import "fmt"

func main() {
	i := 10
	fmt.Printf("%T %v \n",&i,&i) // This gives the address of i
	fmt.Printf("%T %v \n",*(&i),*(&i)) // * is used to dereference the variable.

	// I can even assign to a dereferenced var
	j := &i
    fmt.Printf("%T %v \n",j,j)
	fmt.Println("The value at the pointer location is ", *(j)) // comma is used to concatenate.

	// using dereference indicator to modify the value.
	*(j) = 100 // This changes the value of i...since j points to i.
	fmt.Printf("The value of i is now %v \n",i)
   
	t := "Hello"
	fmt.Println("The current value of t is ", t)

	modify(&t) // Pass address of var t.

	fmt.Println("The value of t is now ", t)
}

func modify(s *string) {
 *(s) = "modified!"
}