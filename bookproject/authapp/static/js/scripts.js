function showAlert(){


    var username=document.getElementById('username').value;
    var first_name=document.getElementById('firstname').value;
    var last_name=document.getElementById('lastname').value;
    var email=document.getElementById('email').value;
    var password=document.getElementById('password').value;
    var cpassword=document.getElementById('cpassword').value;





    if(!username || !first_name ||!last_name || !email || !password || !cpassword)
        {
        alert('Fill the required fields');
    }
    else{
        alert('Registartion sucessfull. Now you can log in');
    }

}