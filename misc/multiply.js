#!/usr/bin/env node
var result = 1
for (var i = 2; i < process.argv.length; i++) {
  result = result * parseInt(process.argv[i])
}
console.log(result)
