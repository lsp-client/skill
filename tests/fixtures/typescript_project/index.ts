/**
 * A simple greeter class
 */
export class Greeter {
  private name: string;

  /**
   * Creates a new Greeter instance
   * @param name The name to greet
   */
  constructor(name: string) {
    this.name = name;
  }

  /**
   * Returns a greeting message
   * @returns The greeting message
   */
  greet(): string {
    return `Hello, ${this.name}!`;
  }
}

const greeter = new Greeter("World");
console.log(greeter.greet());
