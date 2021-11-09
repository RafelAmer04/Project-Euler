// Problem 005 (https://projecteuler.net/problem=5) solver

mod functions;

fn main() { println!("{}", compute()); }

fn compute() -> isize{
    let mut solution = 1;
    let mut gcd;

    for i in 1..21 {
        gcd = functions::gcd(i, solution);
        solution *= i / gcd
    }
    return solution;
}