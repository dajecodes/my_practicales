let display=document.getElementById('screen');
let display2=document.getElementById('screen2');
let operators=['+','-','*','/','%']

function allClear(){
display.value="";
}
function show(n){
    var str =display.value; 
    var lastChar=str.charAt(str.length-1);
    if(operators.includes(lastChar)&&operators.includes(n)){
        display2.value="Operator Error";
    }else{
       display.value+=n;  
    }
   
}

function calc(){
    display2.value=display.value
    display.value=eval(display.value);
}