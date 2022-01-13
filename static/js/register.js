function matchPassword(){
    var pw=document.getElementById("psw1");
    var cpw=document.getElementById("psw2");
    if(pw==cpw){
        alert("password created successfully");
        f1.submit();
    }
    else{
        alert("passwords do not match");
        return pw;
    }
}
