let sidebar_toggler_btn = document.querySelector('.sidebar-toggler');
let sidebar = document.querySelector('.sidebar');
let sidebar_status = false;

const sidebarToggler = () => {
    if(!sidebar_status){
        sidebar.style.left = '0%';
        sidebar_status = true;
        return;
    }
    
    sidebar.style.left = '-100%';
    sidebar_status = false;

}

sidebar_toggler_btn.addEventListener('click', sidebarToggler)

document.addEventListener('click', (event) => {
    if (
        event.target != sidebar &&
        event.target != sidebar_toggler_btn &&
        sidebar_status != true
    ){
        sidebar.style.left = '-100%';
        sidebar_status = false;
    }
})