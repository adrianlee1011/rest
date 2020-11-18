document.addEventListener('DOMContentLoaded', () => {
/*
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
*/
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

                try {
                    // add link to pronunciation
                    const url = data.word.results[0].lexicalEntries[0].entries[0].pronunciations[0].audioFile;
                    document.querySelector('#pronunciation').innerHTML = `<b>Pronunciation</b>: <a href="${url}">Link</a>`;
                }
                catch {
                    document.querySelector('#pronunciation').innerHTML = `No pronunciation found.`;
                }

                try {
                    // add meaning of word
                    const meaning = data.word.results[0].lexicalEntries[0].entries[0].senses[0].definitions[0];
                    document.getElementById('meaning').innerHTML = `<b>Definition:</b> <p>${meaning}</p>`;
                }
                catch {
                    document.getElementById('meaning').innerHTML = `No definition found.`;
                }

                try {
                    // example usage
                    const example = data.word.results[0].lexicalEntries[0].entries[0].senses[0].examples[0].text;
                    document.getElementById('example').innerHTML = `<b>Example usage:</b> <p>${example}</p>`;
                }
                catch {
                    document.getElementById('example').innerHTML = `No example found.`;
                }

                // Saver stuff
                var contents2 = ""
                for(var i = 0; i < data.saver.text.length; i++) {
                    contents2 += `Text: ${data.saver.text[i]}<br/>International: ${data.saver.international[i]}<br/>Gerke: ${data.saver.gerke[i]}<br/>Morse: ${data.saver.morse[i]}<br/><br/>`
                }
                document.querySelector('#saverResult').innerHTML = contents2;
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