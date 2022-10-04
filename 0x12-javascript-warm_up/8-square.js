#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let a = 0; a < size; a++) {
    let caps = '';
    for (let b = 0; b < size; b++) caps += 'X';
    console.log(caps);
  }
}
