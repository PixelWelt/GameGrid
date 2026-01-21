const game_scroller = document.getElementById("game-scroller");
let index = 0;
const games = document.getElementsByClassName("game");

if (games.length > 0) {
    games[0].classList.add("active");
}

const select_audio = new Audio("static/sounds/select.mp3");
const start_audio = new Audio("static/sounds/start.mp3");

document.body.style.cursor = 'none';

document.addEventListener("keydown", async (evt) => {
    if (games.length === 0) return;

    let currentIndex = index;

    if (evt.key === "ArrowRight") {
        index = (index + 1) % games.length;
        select_audio.play();
    } else if (evt.key === "ArrowLeft") {
        index = (index - 1 + games.length) % games.length;
        select_audio.play();
    }

    if (currentIndex !== index) {
        games[currentIndex].classList.remove("active");
        games[index].classList.add("active");
        games[index].scrollIntoView({behavior: 'smooth', block: 'center'});
    }

    if (evt.key === "Enter") {
        await play_audio(start_audio);
        const url = games[index].getAttribute("game-url");
        if (url) {
            window.location.href = url;
        }
    }
});

function play_audio(audio) {
    return new Promise(res => {
        audio.play().catch(() => res()); // Handle cases where play is interrupted
        audio.onended = res;
    });
}

// --- Gamepad Support ---

let gamepadIndex;
let lastGamepadState = {axes: [], buttons: []};

window.addEventListener("gamepadconnected", (event) => {
    console.log("Gamepad connected at index %d: %s. %d buttons, %d axes.",
        event.gamepad.index, event.gamepad.id,
        event.gamepad.buttons.length, event.gamepad.axes.length);
    if (gamepadIndex === undefined) {
        gamepadIndex = event.gamepad.index;
        gameLoop();
    }
});

window.addEventListener("gamepaddisconnected", (event) => {
    console.log("Gamepad disconnected from index %d: %s",
        event.gamepad.index, event.gamepad.id);
    if (gamepadIndex === event.gamepad.index) {
        gamepadIndex = undefined;
    }
});

function gameLoop() {
    if (gamepadIndex === undefined) return;

    const gamepad = navigator.getGamepads()[gamepadIndex];
    if (!gamepad) return;

    // --- Axis (Stick) Navigation ---
    const axisThreshold = 0.7;
    const leftStickX = gamepad.axes[0];

    // Left Stick Right
    if (leftStickX > axisThreshold && lastGamepadState.axes[0] < axisThreshold) {
        document.dispatchEvent(new KeyboardEvent('keydown', {'key': 'ArrowRight'}));
    }
    // Left Stick Left
    if (leftStickX < -axisThreshold && lastGamepadState.axes[0] > -axisThreshold) {
        document.dispatchEvent(new KeyboardEvent('keydown', {'key': 'ArrowLeft'}));
    }

    // --- Button Navigation ---
    // D-Pad Right (Button 15)
    if (gamepad.buttons[15] && !lastGamepadState.buttons[15]?.pressed) {
        document.dispatchEvent(new KeyboardEvent('keydown', {'key': 'ArrowRight'}));
    }
    // D-Pad Left (Button 14)
    if (gamepad.buttons[14] && !lastGamepadState.buttons[14]?.pressed) {
        document.dispatchEvent(new KeyboardEvent('keydown', {'key': 'ArrowLeft'}));
    }
    // A Button (or X on PS, Button 0) for Enter
    if (gamepad.buttons[0] && !lastGamepadState.buttons[0]?.pressed) {
        document.dispatchEvent(new KeyboardEvent('keydown', {'key': 'Enter'}));
    }

    // Store current state for next frame
    lastGamepadState = {
        axes: gamepad.axes.map(a => a),
        buttons: gamepad.buttons.map(b => ({pressed: b.pressed, value: b.value}))
    };

    requestAnimationFrame(gameLoop);
}
