const scoreEl=document.getElementById("score");
const queEl=document.getElementById("question");
const userAnsEl=document.getElementById("answer");
const formEl=document.getElementById('form');
const submitEl=document.getElementById('submit');
let num1=Math.ceil(Math.random()*10);
let num2=Math.ceil(Math.random()*10);
let score=JSON.parse(localStorage.getItem('score'));
if(!score){
    score=0
}
scoreEl.innerText=`Score: ${score}`

const ans=num1*num2;
queEl.innerText=`What is ${num1} multiply by ${num2}?`;


formEl.addEventListener("submit",()=>{
    const userAns = +userAnsEl.value;
    
    if(userAns===ans){
        score++;
    }else{
        score--;
    }
    updateScore()
function updateScore(){
    localStorage.setItem('score',JSON.stringify(score))
}

});