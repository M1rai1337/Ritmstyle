const anchors = document.querySelectorAll('a[href*="#"]');


anchors.forEach(anchors =>{
    anchors.addEventListener('click', event =>{
        const href = anchors.getAttribute('href');
        const id = href.substring(href.search('#') + 1, href.length);

        const block = document.getElementById(id);

        if (block){
            event.preventDefault();

            block.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});