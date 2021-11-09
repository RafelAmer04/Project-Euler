// Problem 003 (https://projecteuler.net/problem=3) solver

fn main() {
println!("{}", compute())
}

fn compute() -> u64 {
    let mut number = 600851475143;
    let mut divisor = 2;

    while number > 1 {
        if number % divisor == 0 {
            number /= divisor;
        } else {
            divisor += 1
        }
    }

    return divisor;
}
