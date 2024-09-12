document.addEventListener('DOMContentLoaded', postData);

const data = document.location.search;
const params = new URLSearchParams(data);

const name = params.get('fname');
const amount = params.get('amount');
const color = params.get('color');
const fightstyle = params.get('fightstyle');
const yorn = params.get('yorn');
const activity = params.getAll('activity');
const breathingstyle = params.get('breathingstyle');

let total = 0;
let breath;



if (amount >= 72) {
    total += 5;
} else if (amount >= 66 && amount < 72) {
    total += 3;
} else {
    total = total;
}
   
if (color == "red") {
    total += 10;
} else if (color == "purple") {
    total += 5;
} else if (color == "yellow") {
    total += 3;
} else {
    total = total;
}

if (fightstyle == "power") {
    total += 10;
} else if(fightstyle == "deciet") {
    total += 5;
} else if(fightstyle == "speed") {
    total += 3;
} else {
    total = total
}

if (yorn == "yes") {
    total += 5;
} else {
    total = total;
}


for(let i = 0; i < activity.length; i++) {
    if(activity[i] == "workingout") {
        total += 10;
    } else if(activity[i] == "stargazing") {
        total += 5;
    } else if(activity[i] == "stormchasing") {
        total += 3;
    } else {
        total = total;
    }
}

if(breathingstyle == "sunbreathing") {
    total += 10;
}else if(breathingstyle == "moonbreathing") {
    total += 5;
} else if(breathingstyle == "thunderbreathing") {
    total += 3;
} else {
    total = total;
}

let image;
let sentence;

if(total >= 45) {
    breath = "Sun Breathing";
    image = 'images/sunbreath.avif';
    sentence = 'Sun Breathing is the original Breathing style that all others branch from. It is even said that only a select few can learn this style!';
} else if (total < 45 && total >= 35) {
    breath = "Moon Breathing";
    image = 'images/moonbreath.jpg';
    sentence = 'Moon breathing is the counterpart of sun breathing that was created when the first demons slayers brother found himself unable to learn sun breathing!';
}else if (total < 35 && total >= 20) {
    breath = "Thunder Breathing";
    image = 'images/thunderbreath.jpg';
    sentence = 'Thunder breathing is the fastest of all breathing styles. The users put all of their power into lighting fast strikes!';
} else {
    breath = "Water Breathing";
    image = 'images/waterbreath.jpg';
    sentence = 'Water breathing is one of the most adaptive breathing styles. The users movement resembles that of water with its flexibility and continuous flow!';
}

//html code below
function postData() {
    const container = document.getElementById('results');
    container.innerHTML = `<h1>If things get bad learn ${breath}!!</h1>
                           <img src="${image}"></img>
                           <p id="description">${sentence}</p>`;
}



