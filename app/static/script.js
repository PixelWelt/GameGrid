game_scroller = document.getElementById("game-scroller")
index = 0
document.getElementsByClassName("game")[0].classList.add("active")
var select_audio = new Audio("static/sounds/select.mp3")
var start_audio = new Audio("static/sounds/start.mp3")
document.body.style.cursor = 'none';
document.addEventListener("keydown", async (evt) => {
    console.log(evt)
    if (evt.key === "ArrowRight") {
        document.getElementsByClassName("game")[index].classList.remove("active")
        index = (index + 1) % document.getElementsByClassName("game").length
        select_audio.play()

    } else if (evt.key === "ArrowLeft") {
        document.getElementsByClassName("game")[index].classList.remove("active")
        index = (index - 1 + document.getElementsByClassName("game").length) % document.getElementsByClassName("game").length
        select_audio.play()
    }
    document.getElementsByClassName("game")[index].classList.add("active")

    if (evt.key === "Enter") {
        await play_audio(start_audio)
        url = document.getElementsByClassName("game")[index].attributes["game-url"].value
        window.location.href = url
    }
})

function play_audio(audio){
     return new Promise(res=>{
        audio.play()
        audio.onended = res
    })
}