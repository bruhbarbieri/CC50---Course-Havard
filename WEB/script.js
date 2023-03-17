//function greet() {
//    let name = document.querySelector('#name').value;
//    alert('hello, ' + name)
//}

//document.addEventListener('DOMContentLoaded', function() {
//    document.querySelector('form').addEventListener('submit', function() {
//        let name = document.querySelector('#name').value;
//        alert('hello, ' + name)
//    });
//});

document.addEventListener('DOMContentLoaded', function() {
    let input = document.querySelector('input');
    input.addEventListener('keyup', function(event) {
        let name = document.querySelector('#name');
        if (input.value) {
            name.innerHTML = `hello, ${input.value}`;
        }
        else {
            name.innerHTML = 'hello, whoever you are';
        }
    });
});




