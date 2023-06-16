setInterval(() => {
    const a = document.querySelector('#movie_player');
    const url = "http://localhost:5000";
    const obj = {
        method: "POST",
        mode: "no-cors",
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    }
    if (a.classList.contains('playing-mode')) {
        obj.body = "foo=true";
        fetch(url, obj);
    } else if (a.classList.contains('paused-mode')) {
        obj.body = "foo=false";
        fetch(url, obj);
    }
}, 2000);