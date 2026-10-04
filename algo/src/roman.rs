// convert to fn roman(int) -> string
// roman(10) -> "X"
// roman(4) -> "IV"
// roman(9) -> "IX"
// roman(58) -> "LVIII"
//
//
// roman(32) -> "XXXII"
// 32 -> 10 + 10 + 10 + 1 + 1
// X + fn(22) -> "XXII"
// X + X + fn(12) -> "XII"
// X + X + X + fn(2) -> "II"
// X + X + X + I + I + fn(0)
//
//
fn roman(num: i32) -> String {
    //35
    //39
    let mut num = num;
    let mut result = String::new();
    let roman_numerals = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ];

    for &(value, symbol) in roman_numerals.iter() {
        while num >= value {
            println!("num: {}, value: {}, symbol: {}", num, value, symbol);
            result.push_str(symbol);
            num -= value;
            println!("result: {}, num: {}", result, num);
            
        }
    }

    result
}


fn f(n: i32) -> String {
    let roman_numerals = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ];
    for &(value, symbol) in roman_numerals.iter() {
        if n >= value {
            return format!("{}{}", symbol, f(n - value));
        }
    }
    String::new()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_roman() {
        assert_eq!(roman(10), "X");
        assert_eq!(roman(4), "IV");
        assert_eq!(roman(9), "IX");
        assert_eq!(roman(58), "LVIII");
        assert_eq!(roman(32), "XXXII");
        assert_eq!(roman(39), "XXXIX");
        assert_eq!(roman(1994), "MCMXCIV");
        assert_eq!(roman(1994), "MCMXCIV");
    }

    #[test]
    fn test_f() {

        assert_eq!(f(10), "X");
        assert_eq!(f(4), "IV");
        assert_eq!(f(9), "IX");
        assert_eq!(f(58), "LVIII");
        assert_eq!(f(32), "XXXII");
        assert_eq!(f(39), "XXXIX");
        assert_eq!(f(1994), "MCMXCIV");
    }

}
