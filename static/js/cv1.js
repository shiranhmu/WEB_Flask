

function checkAPI(){
    const inputP = document.getElementById("phone");
    if(!inputP.checkValidity()){
        document.getElementById("demo").innerHTML = inputP.validationMessage;
    }else{
        document.getElementById("demo").innerHTML = "Input OK";
    }
}
