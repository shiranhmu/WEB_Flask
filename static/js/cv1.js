
function checkAPI(){
    const inputP = document.getElementById("phone");
    if(!inputP.checkValidity()){
        document.getElementById("demo").innerHTML = inputP.validationMessage;
    }else{
        document.getElementById("demo").innerHTML = "Input OK";
    }
}

function confirm() {
    alert("Database Updated!");
}

function getUsers(){
    console.log("clicked");
    fetch('https://reqres.in/api/users/').then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}
function put_users_inside_html(response_obj_data){
    //console.log(response_obj_data);
    const curr_main = document.querySelector("main");
    let number = parseInt(document.getElementById('number').value);
    for (let user of response_obj_data) {
        const section = document.createElement('section');
        section.innerHTML = `
        <img src="${user.avatar}" alt="Profile Picture"/>
        <div>
            <span> ${user.first_name} ${user.last_name}</span>
            <br>
            <a href="mailto:${user.email}"> Send Email</a>
        </div>
        `;
        if (user.id == number) {
            curr_main.appendChild(section);
        }
    }
}