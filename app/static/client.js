document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#formCoder').onsubmit = () => {

        // Initialize new request
        const request = new XMLHttpRequest();
        const text2 = document.querySelector('#txtInput').value;
        request.open('POST', '/coder');

        // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);

            // Update the result div
            if (data.success) {
                const contents = `<table width="100%"><tr><th>Text</th><th>International</th><th>Gerke</th><th>Morse</th></tr><tr><td>${text2}</td><td>${data.code.international}</td><td>${data.code.gerke}</td><td>${data.code.morse}</td></tr></table>`
                document.querySelector('#result').innerHTML = contents;
            }
            else {
                document.querySelector('#result').innerHTML = 'There was an error.';
            }
        }

        // Add data to send with request
        const data = new FormData();
        data.append('text', text2);

        // Send request
        request.send(data);
        return false;
    };

});