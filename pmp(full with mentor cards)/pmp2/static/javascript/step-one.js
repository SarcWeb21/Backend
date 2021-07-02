const btn1 = document.getElementsByClassName('btn1')[0]
const  secondStep = document.getElementsByClassName('secondStep')[0]

btn1.addEventListener('click', () => {
    secondStep.classList.toggle('active')
})


const btn2 = document.getElementsByClassName('btn2')[0]
const thirdStep = document.getElementsByClassName('thirdStep')[0]

btn2.addEventListener('click', () => {
    thirdStep.classList.toggle('active')
})



