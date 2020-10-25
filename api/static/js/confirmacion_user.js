function confirmarEliminacion2(id){
    Swal.fire({
        title: 'Estas Seguro?',
        text: "no podras deshacer esta acción!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Eliminar!',
        cancelButtonText: 'Cancelar',

      }).then((result) => {
        if (result.isConfirmed) {
            //redirigir a eliminar 
            window.location.href ="/eliminar-user/"+id+"/";
        }
      })
}