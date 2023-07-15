const num1=Math.ceil(Math.random()*10);
const num2=Math.ceil(Math.random()*10);
const questionEl=document.getElementById("question")
const formEl=document.getElementById("form")
const inputEl=document.getElementById("input")
const scoreEl=document.getElementById("score")
questionEl.innerText=`What is ${num1} multiply by ${num2}?`
const answer=num1*num2;
let score=JSON.parse(localStorage.getItem("score"))
if(!score){
    score=0;
}
scoreEl.innerText=`Score:${score}`

formEl.addEventListener("submit",()=>{
    const userAns=+inputEl.value
   
    if(answer === userAns){
       score++;       
    }else{
        score--;        
    } 
    updateScore(); 
   

    
});
function updateScore(){
    localStorage.setItem("score",JSON.stringify(score));
}