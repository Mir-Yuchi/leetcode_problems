impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let a_chars: Vec<char> = a.chars().collect();
        let b_chars: Vec<char> = b.chars().collect();
        let mut result = Vec::new();
        let mut carry = 0;
        let mut i = a_chars.len() as i32 - 1;
        let mut j = b_chars.len() as i32 - 1;

        while i >= 0 || j >= 0 || carry > 0 {
            let a_bit = if i >= 0 { a_chars[i as usize].to_digit(2).unwrap() } else { 0 };
            let b_bit = if j >= 0 { b_chars[j as usize].to_digit(2).unwrap() } else { 0 };
            let sum = a_bit + b_bit + carry;
            result.push((sum % 2).to_string());
            carry = sum / 2;
            i -= 1;
            j -= 1;
        }

        result.reverse();
        result.join("")
    }
}
