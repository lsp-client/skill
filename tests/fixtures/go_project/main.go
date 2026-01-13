package main

import "fmt"

// Greeter provides greeting functionality
type Greeter struct {
	name string
}

// NewGreeter creates a new Greeter instance
func NewGreeter(name string) *Greeter {
	return &Greeter{name: name}
}

// Greet returns a greeting message
func (g *Greeter) Greet() string {
	return fmt.Sprintf("Hello, %s!", g.name)
}

func main() {
	greeter := NewGreeter("World")
	fmt.Println(greeter.Greet())
}
