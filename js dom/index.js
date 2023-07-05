let answer = prompt('What is your name?');

//to display answer as an html element
if (typeof (answer) === 'string') {
    var h1 = document.createElement('h1')
    h1.innerText = answer;
    document.body.innerText = '';
    document.body.appendChild(h1);
}

// add event listener to show the input given
input.addEventListener('change', function () {
    h1.innerText = input.value
})

//to show given input on webpage
var h2 = document.createElement('h2');
input.addEventListener('change', function () {
    h2.innerText = input.value
    document.body.appendChild(h2);
})