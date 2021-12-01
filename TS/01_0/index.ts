import { readFileSync } from 'fs';

const file = readFileSync("./input.txt", "utf-8");
const lines = file.split(/\s/);
let counter = 0;
lines.forEach((v, i) => {
    if (i === 0) return;
    if (Number(v) > Number(lines[i-1]))
        counter += 1;
});
console.log(counter);