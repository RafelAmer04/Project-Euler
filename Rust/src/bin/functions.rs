
pub fn gcd(a: isize, b: isize) -> isize{
    if b == 0 { return a; }
    return gcd(b, a % b)
}