$(function(){
    mostrar_campos( document.getElementById('id_tipo_encabezado').value );

    function mostrar_campos(valor) {
        if (valor == 'F') {

        }

        // document.getElementsByClassName('field-url_imagen_2')[0].style.visibility = 'hidden';
        // document.getElementsByClassName('field-text_imagen_2')[0].style.visibility = 'hidden';
        // document.getElementsByClassName('field-subtext_imagen_2')[0].style.visibility = 'hidden';
    }

    document.getElementById('id_tipo_encabezado').onchange = function() {
        var index = this.selectedIndex;
        var inputText = this.children[index].innerHTML.trim();
        console.log(index, inputText);
        
        // mostrar_campos( document.getElementById('id_tipo_encabezado').value );

        // $('fieldset.collapse.open').removeClass('collapsed');
        // $('.collapse').removeClass('collapsed');
        

        let collection = document.getElementsByClassName("collapse");
        console.log( collection );
    }

})(django.jQuery);