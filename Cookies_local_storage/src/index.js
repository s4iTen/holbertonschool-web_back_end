function setCookies() {
    const firstname = document.getElementById('firstname');
    const email = document.getElementById('email');
    console.log(firstname.value)
    console.log(email.value)

    if (firstname.value && email.value) {
        document.cookie = 'firstname=' + firstname.value + ';' +  'email=' + email.value + ';' + 'expires=Thu, 18 Dec 2025 12:00:00 UTC';
        console.log(document.cookie);
    } else {
        console.error("Error: Firstname and email are required");
    }
}

function showCookies() {
    const p = document.createElement('p')
    p.innerHTML = document.cookie
    document.body.appendChild(p)
    console.log(document.cookie)
}