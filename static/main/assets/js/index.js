document.addEventListener('DOMContentLoaded', function () {


    // ------------------ About tablink
    const tablink = document.querySelectorAll(".tablink")
    const tabitem = document.querySelectorAll(".tabitem")
    tablink.forEach((e) => {
        e.addEventListener("click", handleTabLink = () => {


            for (var j = 0; j < tablink.length; j++) {
                tablink[j].classList.remove("bg-clr_base", "text-clr_title");
                tablink[j].classList.add("bg-[#1D1D1D]", "text-clr_white")
            }

            e.classList.add("bg-clr_base", "text-clr_title")
            e.classList.remove("bg-[#1D1D1D]", "text-clr_white")


            const tabName = e.getAttribute("data")

            tabitem.forEach((ev) => {
                const itemName = ev.getAttribute("data")
                ev.classList.remove("z-10", "opacity-100", "translate-y-0", "z-10")
                ev.classList.add("top-0", "absolute", "translate-y-20", "-z-10", "opacity-0")
                if (itemName === tabName) {
                    for (let index = 0; index < ev.classList.length; index++) {
                        const element = ev.classList[index];

                        if (element === "absolute") {
                            ev.classList.remove("top-0", "absolute", "translate-y-20", "-z-10", "opacity-0")
                            ev.classList.add("z-10", "opacity-100", "translate-y-0", "z-10")
                        }
                    }
                }

            })

        })
    })

    // -------------- Testimonial slider
    var swiper = new Swiper(".testimonial__slidewrap", {
        spaceBetween: 0,
        speed: 3000,
        loop: true,
        autoplay: {
            delay: 2000,
        },
        pagination: {
            el: ".swiper-pagination3",
            clickable: true,
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                spaceBetween: 10,
            },
            575: {
                slidesPerView: 1,
            },
            991: {
                slidesPerView: 1,
            },
            1200: {
                slidesPerView: 1,
            },
            1400: {
                slidesPerView: 1,
            },
            1600: {
                slidesPerView: 1,
            },
        }
    });


    // ---------- popup modal

    $('.video-btn').magnificPopup({
        type: 'iframe',
        callbacks: {

        }
    });
    $('.imgc').magnificPopup({
        type: 'image',
        gallery: {
            enabled: true,
        }
    });
})