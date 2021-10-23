var Factor = require('./Factor').Factor;
var n = require('./data').n;
var B = require('./data').B;

console.log('n' = n);
console.log('B' = B);

var res = Factor(n,B);

console.log('ans: ',res[0],res[1]);