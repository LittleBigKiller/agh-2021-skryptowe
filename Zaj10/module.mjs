/** @module module */

/** Klasa reprezentująca operację. */
export class Operation {
  /**
   * Stwórz operację.
   * @param {number} x - Wartość x.
   * @param {number} y - Wartość y.
   */
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  /**
   * Zsumuj podane w definicji klasy wartości x i y.
   * @return {number} - Suma wartości x i y.
   */
  sum() {
    return this.x + this.y;
  }
}

export default Operation;
