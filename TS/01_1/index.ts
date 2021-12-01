import { readFileSync } from 'fs';

const file = readFileSync("./input.txt", "utf-8");
const lines = file.split(/\s/);
const numbers = lines.map(Number);
let counter = 0;

const f = (acc: number, x: number): number => acc + x;

for (let i = 4; i <= lines.length; i++) {
    let a = numbers.slice(i-4, i-1).reduce(f)
    let b = numbers.slice(i-3, i).reduce(f)
    if (b > a) {
        counter++;
    }
}
console.log(counter);