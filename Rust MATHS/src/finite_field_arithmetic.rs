fn xgcd(x: i32, y: i32) -> (i32, i32, i32) {
    let (mut old_r, mut r) = (x, y);
    let (mut old_s, mut s) = (1, 0);
    let (mut old_t, mut t) = (0, 1);
    let mut count = 0;
    println!("\tEncontrando el xgcd({}): {} {} {}", count, old_r, old_t, old_s);
    while r != 0 {
        let quotient = old_r / r;
        let tmp = r;
        r = old_r - quotient * r;
        old_r = tmp;
        let tmp = s;
        s = old_s - quotient * s;
        old_s = tmp;
        let tmp = t;
        t = old_t - quotient * t;
        old_t = tmp;
        count += 1;
    }
    return (old_s, old_t, old_r); // (a, b, g)
}


fn main() {
    let prime = 13;

    println!("Operadores matemáticos en campo finito:");

    ////////////////////
    // FF Suma
    ////////////////////
    let lefthand = 4;
    let righthand = 12;
    println!(
        "\tSuma: ({} + {}) % {} = {}\n",
        lefthand,
        righthand,
        prime,
        (lefthand + righthand) % prime
    );

    ////////////////////
    // FF Resta
    ////////////////////
    let lefthand = 35;
    let righthand = 5;
    println!(
        "\tResta: ({} - {}) % {} = {}\n",
        lefthand,
        righthand,
        prime,
        (lefthand + righthand * -1 + prime) % prime
    );

    ////////////////////
    // FF Multiplicación
    ////////////////////
    let lefthand = 90;
    let righthand = 10;
    println!(
        "\tMultiplicación: ({} * {}) % {} = {}\n",
        lefthand,
        righthand,
        prime,
        (lefthand * righthand) % prime
    );

    ////////////////////
    // FF División
    ////////////////////
    let dividend = 2;
    let divisor = 3;
    println!("\tDivisión: ({} / {})", dividend, divisor);
    let (a, b, _) = xgcd(divisor, prime);
    println!(
        "\tse encontró: {}*{:2} + {}*{:2} = 1\n",
        a, divisor, b, prime
    );
    println!(
        "\t({} / {}) % {} = {}\n",
        dividend,
        divisor,
        prime,
        ((dividend * a % prime) + prime) % prime
    );
}
