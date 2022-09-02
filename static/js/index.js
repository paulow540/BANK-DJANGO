let pro = document.getElementById('prof')
pro.addEventListener('click',()=>{
    document.getElementById('profile').hidden = false;
    document.getElementById('dash').hidden = true;
    document.getElementById('deposit').hidden = true;
    document.getElementById('transfer').hidden = true;
    document.getElementById('recharge').hidden = true;
    document.getElementById('error').hidden = true;
    document.getElementById('success').hidden = true;
})

document.getElementById('dep').addEventListener('click',()=>{
    document.getElementById('deposit').hidden = false;
    document.getElementById('profile').hidden = true;
    document.getElementById('dash').hidden = true;
    document.getElementById('transfer').hidden = true;
    document.getElementById('recharge').hidden = true;
    document.getElementById('error').hidden = true;
    document.getElementById('success').hidden = true;
})

document.getElementById('tran').addEventListener('click',()=>{
    document.getElementById('transfer').hidden = false;
    document.getElementById('deposit').hidden = true;
    document.getElementById('dash').hidden = true;
    document.getElementById('recharge').hidden = true;
    document.getElementById('error').hidden = true;
    document.getElementById('success').hidden = true;
    document.getElementById('profile').hidden = true;
})

document.getElementById('rech').addEventListener('click',()=>{
    document.getElementById('recharge').hidden = false;
    document.getElementById('deposit').hidden = true;
    document.getElementById('dash').hidden = true;
    document.getElementById('transfer').hidden = true;
    document.getElementById('error').hidden = true;
    document.getElementById('success').hidden = true;
    document.getElementById('profile').hidden = true;
})





