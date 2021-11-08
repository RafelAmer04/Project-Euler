// Problem 001 (https://projecteuler.net/problem=1) solver
fn compute() -> u32 {
    let mut solution = 0;

    for i in 1..1000 {
        if i % 3 == 0 || i % 5 == 0 {
            solution += i;
        }
    }
    return solution;
}

fn main() {
    println!("{}", compute())
}