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

    document.querySelector('#dictField').onsubmit = () => {

        // Initialize new request
        const request = new XMLHttpRequest();
        const word = document.querySelector('#dictionary-search').value;
        request.open('POST', '/dictionary');

        // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);
            // Update the result div
            if (data.success) {
                // add searched word into title
                document.querySelector('#queryWord').innerHTML = `Word: ${data.word.id}`;

                // add link to pronunciation
                const url = data.word.results[0].lexicalEntries[0].entries[0].pronunciations[0].audioFile;
                document.querySelector('#pronunciation').innerHTML = `<b>Pronunciaition</b>: <a href="${url}">Link</a>`;

                // add meaning of word
                const meaning = data.word.results[0].lexicalEntries[0].entries[0].senses[0].definitions[0];
                document.getElementById('meaning').innerHTML = `<b>Definition:</b> <p>${meaning}</p>`;

                // example usage
                const example = data.word.results[0].lexicalEntries[0].entries[0].senses[0].examples[0].text;
                document.getElementById('example').innerHTML = `<b>Example usage:</b> <p>${example}</p>`;
            }
            else {
                document.querySelector('#queryWord').innerHTML = 'Error: No such word found.';
            }
        }

        // Add data to send with request
        const data = new FormData();
        data.append('word', word);

        // Send request
        request.send(data);
        return false;
    };

});