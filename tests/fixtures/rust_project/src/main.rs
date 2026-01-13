/// A simple greeter struct
pub struct Greeter {
    name: String,
}

impl Greeter {
    /// Creates a new Greeter instance
    pub fn new(name: String) -> Self {
        Greeter { name }
    }

    /// Returns a greeting message
    pub fn greet(&self) -> String {
        format!("Hello, {}!", self.name)
    }
}

fn main() {
    let greeter = Greeter::new(String::from("World"));
    println!("{}", greeter.greet());
}
