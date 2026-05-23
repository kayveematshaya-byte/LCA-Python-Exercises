//TODO: Create an array called numbers with values 1 through 5
let numbers = [1, 2, 3, 4, 5];1, 2, 3, 4, 5

//TODO: Write a for loop that prints each number in the array
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);1, 2, 3, 4, 5
}

//TODO: Write a while loop that counts down from 5 to 1
let count = 5;5
while (count > 0) {
    console.log(count);5, 4, 3, 2, 1
    count--;5, 4, 3, 2, 1
}

//TODO: Create a loop that prints only even numbers from the numbers array
for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0) {
        console.log(numbers[i]);2, 4
    }
}

//TODO: Create a loop that calculates the sum of all numbers in the array
let sum = 0;0
for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];1, 2, 3, 4, 5 
}
console.log(sum);15


