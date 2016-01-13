//using array extension method

func fib_with_array() -> Int {
var fibonacci_array = [1, 2]
var sumvar = 2
while fibonacci_array.last < 4000000 {
    
    let next_item = fibonacci_array[fibonacci_array.count - 1] + fibonacci_array[fibonacci_array.count - 2]
    fibonacci_array.append(next_item)
    if next_item % 2 == 0 {
        
        sumvar += next_item
        
    }
    
}
return(sumvar)
}

// keep only last two elements
func fib_no_array() -> Int {
var a = 1
var b = 2
var sumvar = 2
var next_item = a + b 
while next_item < 4000000 {

	
	if next_item % 2 == 0 {
		sumvar += next_item
	}
	a = b
	b = next_item
	next_item = a + b 

}

return(sumvar)
}
print(fib_no_array())

