// Problem 002 (https://projecteuler.net/problem=2) solver
fn compute() -> u32 {
    let mut solution = 0;
    let mut x = 1;
    let mut y = 2;
    let mut t = 0;

    while x <= 4000000 {
        t = x+y;
        x = y;
        y = t;

        if x % 2 == 0 {
            solution += x
        }
    }
    return solution;
}

fn main() {
    println!("{}", compute())
}
