// listen to click event on body
// using addEventListener method
const target = document.querySelector('body')
function handleClick(){
    console.log('clicked the body')
}
target.addEventListener('click',handleClick())

// using html event attributes
// change html source add attribute oneclick="function_name()"
function handleClick2(){
    console.log('clicked the heading')
}