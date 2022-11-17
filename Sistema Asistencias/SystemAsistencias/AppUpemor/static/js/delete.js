(function(){
    const btnDelete = document.querySelectorAll('.btnDelete');

    btnDelete.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Estas seguro de eliminar el registro?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
})();