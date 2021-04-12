var userName = document.getElementById('name').innerHTML;
var score = 0;
var word = null;
const bucket = jsonObject;
var ranNum = null;
var seconds = 60;
document.querySelector('body').onload = start();
document.getElementById('details').style.display = "none";

var enterKey = document.getElementById("answer");
enterKey.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("btn1").click();
  }
});

function start() {
    refresh();
    const timer = setInterval(() => {
        seconds-- 
        document.getElementById('timer').innerHTML = seconds;
        if (seconds < 0) {
            clearInterval(timer);
            document.getElementById('timer').innerHTML = 0;
            document.getElementById('word').innerHTML = "Time's Up";
            document.getElementById('id_name').value = userName;
            document.getElementById('id_score').value = score;
            document.forms['myForm'].submit();
            if (a === word) {
                score += 2;
                document.getElementById('id_score').value = score; 
                refresh();
            };
        };
    }, 1000);
}

function refresh() {
    ranNum = Math.floor(Math.random() * bucket.length);
    document.getElementById('answer').value = "";
    word = bucket[ranNum].text;
    document.getElementById('hint').innerHTML = bucket[ranNum].hint;
    document.getElementById('word').innerHTML = bucket[ranNum].mix;
    document.getElementById('hint').style.visibility = "hidden";
    document.getElementById('score').innerHTML = "Score: " + score;
    document.getElementById('btn2').disabled = "";
}

function next() {
    let a = document.getElementById('answer').value.toLowerCase();
    if (a === word) {
        score += 2;
        document.getElementById("btn1").className = "btn btn-success m-2";
        var outcome = setTimeout(() => {
            document.getElementById('btn1').className = "btn btn-primary m-2";
        }, 1000);
        refresh();
    } else {
        document.getElementById("btn1").className = "btn btn-danger m-2";
        var outcome = setTimeout(() => {
            document.getElementById('btn1').className = "btn btn-primary m-2";
        }, 1000);
        refresh();
    };
}

function hint() {
    document.getElementById('hint').style.visibility = "visible";
    document.getElementById('btn2').disabled = "disabled";
    score --;
    if (score < 0) {
        score = 0;
    };
}