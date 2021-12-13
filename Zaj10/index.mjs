import { Operation } from './module.mjs';

// Nie jest możliwe utworzenie obiektu przed definicją klasy.
console.log(new Operation(parseInt(process.argv[2]), parseInt(process.argv[3])).sum());
