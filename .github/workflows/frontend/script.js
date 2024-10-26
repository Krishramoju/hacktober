async function sendMood() {
    const imageInput = document.getElementById("imageInput").files[0];
    const moodInput = document.getElementById("moodInput").value;

    const formData = new FormData();
    if (imageInput) formData.append("image", imageInput);
    formData.append("mood", moodInput);

    const response = await fetch("http://localhost:5000/analyze-mood", {
        method: "POST",
        body: formData
    });

    const result = await response.json();
    displayPlaylist(result.playlist);
}

function displayPlaylist(playlist) {
    const playlistDiv = document.getElementById("playlist");
    playlistDiv.innerHTML = "<h3>Your Playlist:</h3><ul>" + 
        playlist.map(song => `<li>${song}</li>`).join('') + "</ul>";
}
