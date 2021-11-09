// Problem 004 (https://projecteuler.net/problem=4) solver


fn main() {
    println!("{}", compute());
}

fn compute()-> u32 {
    let mut max = 0;
    let mut product;
    for i in 1..1000 {
        for j in 1..1000{
            product = i*j;
            if is_palindrome(product.to_string()) && product > max{
                max = product;
            }
        }
    }

    return max;
}

fn is_palindrome(number: String)-> bool{
    let len = number.chars().count();

    for i in 0..len {
        if number.chars().nth(i) != number.chars().nth(len-i-1) {
            return false;
        }
    }
    return true;
}