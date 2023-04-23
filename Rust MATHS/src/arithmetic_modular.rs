use std::io::{stdout, Write};
use std::{thread, time};
use crossterm::{execute, cursor, terminal};

fn main() {
    let mut hours = 0;
    let mut carries = 0;
    let modulus = 12;

    let mut stdout = stdout();
    execute!(stdout, terminal::Clear(terminal::ClearType::All)).unwrap();

    ////////////////////
    // Numbers "wrap"
    // the modulus
    ////////////////////
    for _i in 0..720 {
        execute!(stdout, cursor::MoveTo(0, 0)).unwrap();
        write!(
            stdout,
            "\t Time: {:02}\tHours: {:02}\t Days: {:.1}",
            hours % modulus,
            hours,
            carries as f64 / 2.0
        ).unwrap();
        stdout.flush().unwrap();
        hours += 1;
        if hours % modulus == 0 {
            carries += 1;
        }
        thread::sleep(time::Duration::from_millis(300));
    }
}
