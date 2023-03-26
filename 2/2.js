// Write a JavaScript function countWords  that takes a string and returns the number of words contained in this string. 
// Example:
// Input: ”Lorem ipsum dolor sit amet consectetur”
// Output: 6

// Constraints:
// using built-in functions is prohibited
function  countWords (str){
    let words = str.split(" ");
    let wordCount = words.length;
    console.log(wordCount); 
}
countWords ("amar sonar blangla ami tomai vlobasi")
