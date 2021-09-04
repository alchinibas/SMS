let copySon=document.getElementById("copySon");
let copyFather=document.getElementById("copyFather");

let sDistrict = document.getElementById("sDistrict");
let sMunicipality = document.getElementById("sMunicipality");
let sTole = document.getElementById("sTole");
let sEmail=document.getElementById("sEmail");
let sContact=document.getElementById("sContact");

let gDistrict1 = document.getElementById("gDistrict1");
let gMunicipality1 = document.getElementById("gMunicipality1");
let gTole1 = document.getElementById("gTole1");
let gEmail1 = document.getElementById("gEmail1");
let gContact1 = document.getElementById("gContact1");

let gDistrict2 = document.getElementById("gDistrict2");
let gMunicipality2 = document.getElementById("gMunicipality2");
let gTole2 = document.getElementById("gTole2");
let gEmail2 = document.getElementById("gEmail2");
let gContact2 = document.getElementById("gContact2");
let noParent = document.getElementById("noParent");

window.onload=function(){
    if(copySon.checked)attachSon();
    if(copyFather.checked)attachFather();
}

copySon.addEventListener("change",function(){
    if(this.checked)attachSon();
})
copyFather.addEventListener("change",function(){
    if(this.checked)attachFather();
})

sDistrict.addEventListener("input",function(){
    if(copySon.checked)gDistrict1.value = sDistrict.value;
    if(copyFather.checked)gDistrict2.value = gDistrict1.value;
})
gDistrict1.addEventListener("input",function(){
    if(copyFather.checked)gDistrict2.value = gDistrict1.value;
})

sMunicipality.addEventListener("input", function(){
    if(copySon.checked)gMunicipality1.value=sMunicipality.value;
    if(copyFather.checked)gMunicipality2.value=gMunicipality1.value;
})
gMunicipality1.addEventListener("input", function(){
    if(copyFather.checked)gMunicipality2.value=gMunicipality1.value;
})

sTole.addEventListener("input",function(){
    if(copySon.checked)gTole1.value=sTole.value;
    if(copyFather.checked)gTole2.value=gTole1.value;
})
gTole1.addEventListener("input",function(){
    if(copyFather.checked)gTole2.value=gTole1.value;
})

sEmail.addEventListener("input",function(){
    if(copySon.checked)gEmail1.value=sEmail.value;
    if(copyFather.checked)gEmail2.value=gEmail1.value;
})
gEmail1.addEventListener("input",function(){
    if(copyFather.checked)gEmail2.value=gEmail1.value;
})

sContact.addEventListener("input",function(){
    if(copySon.checked)gContact1.value = sContact.value;
    if(copyFather.checked)gContact2.value=gContact1.value;
})
gContact1.addEventListener("input",function(){
    if(copyFather.checked)gContact2.value=gContact1.value;
})

function attachSon(){
    gDistrict1.value = sDistrict.value;
    gMunicipality1.value = sMunicipality.value;
    gTole1.value = sTole.value;
    gEmail1.value = sEmail.value;
    gContact1.value = sContact.value;
}

function attachFather(){
    gDistrict2.value = gDistrict1.value;
    gMunicipality2.value = gMunicipality1.value;
    gTole2.value = gTole1.value;
    gEmail1.value = gEmail1.value;
    gContact2.value = gContact1.value;
}

let fatherDetail = document.getElementById("fatherDetail");
let motherDetail = document.getElementById("motherDetail");

noParent.addEventListener("change",function(){
    if(noParent.checked){
        fatherDetail.setAttribute("disabled","disabled");
        motherDetail.setAttribute("disabled","disabled");
        createGuardianForm();
    }
    else{
        fatherDetail.removeAttribute("disabled");
        motherDetail.removeAttribute("disabled");
    }
})
