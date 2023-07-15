const textEl=document.getElementById("textarea");
const totalEl=document.getElementById("total");
const remainingEl=document.getElementById("remaining");
textEl.addEventListener("keyup",()=>{
    update();
});
function update(){
    totalEl.innerText=textEl.value.length
    remainingEl.innerText=(50-textEl.value.length)
}