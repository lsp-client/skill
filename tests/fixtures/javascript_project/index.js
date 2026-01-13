/**
 * A simple greeter class
 */
export class Greeter {
  /**
   * Creates a new Greeter instance
   * @param {string} name - The name to greet
   */
  constructor(name) {
    this.name = name;
  }

  /**
   * Returns a greeting message
   * @returns {string} The greeting message
   */
  greet() {
    return `Hello, ${this.name}!`;
  }
}

const greeter = new Greeter("World");
console.log(greeter.greet());
