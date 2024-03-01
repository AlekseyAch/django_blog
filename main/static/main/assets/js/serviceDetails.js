// ----------------- accordion
let accordion = document.querySelectorAll(".accordion");
let accordionIcon = document.querySelectorAll(".accordion i");


for (let i = 0; i < accordion.length; i++) {
    accordion[i].addEventListener("click", function () {

        let accordionBody = this.nextElementSibling;

        if (accordionBody.style.display === "block") {
            accordionBody.style.display = "none";

            accordion[i].classList.remove("text-clr_base");
            accordion[i].classList.add("text-white");
            accordionIcon[i].classList.remove("rotate-180")
        } else {
            accordionBody.style.display = "block";
            accordion[i].classList.remove("text-white");
            accordion[i].classList.add("text-clr_base");
            accordionIcon[i].classList.add("rotate-180")
        }
    });
}