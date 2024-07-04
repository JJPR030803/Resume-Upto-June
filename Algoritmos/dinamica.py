class Fibonacci(dict):
 
    # Function signature of the
    # __missing__ function in
    # python
    def __missing__(self, n):
         
        # Base case
        if n<= 1:
 
            # Storing the value in the
            # dictionary before returning
            self[n] = n
            return n
 
        # Storing the value in the dictionary
        # before returning the value
        val = self[n] = self[n-1] + self[n-2]
        return val
 
if __name__ == "__main__":
 
    # Create an instance of the class
    Fib = Fibonacci()
    N = Fib[9]
    print(N)