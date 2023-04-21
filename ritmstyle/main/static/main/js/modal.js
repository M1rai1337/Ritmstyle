const buttonOpen = document.getElementById("open-modal-btn");
const buttonClose = document.querySelector('.modal__close-button');
const modalWindow = document.querySelector('.modal');
const modalBox = document.querySelector('.modal__info');

const button1 = document.getElementById('button-address-1');
const button2 = document.getElementById('button-address-2');
const addresses = document.getElementById('id_addresses').children;


function modalOpen(){
    modalWindow.classList.add('open'); 
    body.classList.add('lock'); 
}

function modalClose(){
    modalWindow.classList.remove('open');
    body.classList.remove('lock'); 
}

function doSelected(value){
    for(let addres of addresses){
        if (addres.value === value){addres.selected = true;}
        else {addres.selected = false;}
    }
}

buttonOpen.addEventListener("click", () => {modalOpen();});
buttonClose.addEventListener("click", () => {modalClose();});
window.addEventListener('keydown', (e) => {
    if(e.key === "Escape"){
        modalClose();
    }
});

if (button1 && button2){
    button1.addEventListener("click", () => {
        doSelected("1");
        modalOpen();
    });
    
    button2.addEventListener("click", () => {
        doSelected("2");
        modalOpen();
    });
}
