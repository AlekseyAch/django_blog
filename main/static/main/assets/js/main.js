// -------------- Scroll top sticky header
const header = document.querySelector(".header")
const isSticky = (e) => {
    const scrollTop = window.scrollY;

    if (scrollTop >= 35) {
        header.classList.add("fixed", "top-0", "left-0", "z-50", "bg-black", "w-full")
        header.classList.remove("relative")
    }
    else {
        header.classList.add("relative")
        header.classList.remove("fixed", "top-0", "left-0", "z-50", "bg-black", "w-full")
    }

};
window.addEventListener("scroll", isSticky);



// ---------------- small devise menu hide and show
const menus = document.querySelector(".menus")
const menuActiveIcon = document.querySelector(".menuActiveIcon")
const menuCloseIcon = document.querySelector(".menuCloseIcon")

menuActiveIcon.addEventListener("click", () => {
    menus.classList.add("opacity-100", "visible")
    menus.classList.remove("opacity-0", "invisible", "lg:opacity-100", "lg:visible")
    menuCloseIcon.classList.remove("hidden")
    menuActiveIcon.classList.add("hidden")
})

menuCloseIcon.addEventListener("click", () => {
    menus.classList.add("opacity-0", "invisible", "lg:opacity-100", "lg:visible")
    menus.classList.remove("opacity-100", "visible")
    menuCloseIcon.classList.add("hidden")
    menuActiveIcon.classList.remove("hidden")
})


// ---------- sidebar menu or drawer
const drawerActiveIcon = document.querySelector(".drawerActiveIcon")
const drawerCloseIcon = document.querySelector(".drawerCloseIcon")
const drawer = document.querySelector(".drawer")
drawerActiveIcon.addEventListener("click", () => {
    drawer.classList.add("right-0")
    drawer.classList.remove("-right-80")
})
drawerCloseIcon.addEventListener("click", () => {
    drawer.classList.remove("right-0")
    drawer.classList.add("-right-80")
})



// -------------- DropDown menu
const dropdown = document.querySelectorAll(".dropdown")
const dropdownItem = document.querySelectorAll(".dropdownItem")
dropdown.forEach((e, i) => {
    e.addEventListener("click", () => {
        dropdownItem.forEach((_, index) => {
            if (i === index) {
                dropdownItem[index].classList.toggle("hidden")
            }
        })
    })
})


AOS.init();
