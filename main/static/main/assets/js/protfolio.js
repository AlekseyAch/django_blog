document.addEventListener('DOMContentLoaded', function () {

    const tablink = document.querySelectorAll(".tablink")
    const project__item = document.querySelectorAll(".project__item")
    tablink.forEach((e) => {
        e.addEventListener("click", handleTabLink = () => {


            for (var j = 0; j < tablink.length; j++) {
                tablink[j].classList.remove("bg-clr_base", "text-clr_title");
                tablink[j].classList.add("bg-transparent", "text-clr_white")
            }

            e.classList.add("bg-clr_base", "text-clr_title")
            e.classList.remove("bg-transparent", "text-clr_white")


            const tabName = e.getAttribute("data")

            // console.log(tabName)
            project__item.forEach((ev) => {
                ev.classList.remove("hidden")
                const itemName = ev.getAttribute("data")
                const item = itemName.trim().split(/\s*,\s*/)

                console.log(item)
                if (!item.includes(tabName)) {
                    ev.classList.add("hidden")
                    // ev.classList.remove("block")
                }



                //   ev.classList.add("block")

            })

        })
    })

    $('.imgc').magnificPopup({
        type: 'image',
        gallery: {
            enabled: true,
        }
    });

})