$('.tabs-navigation .tab-ctrl').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    // Español
    if (url.indexOf("/alumni") >= 0 || url.indexOf("/media/") >= 0 || url.indexOf("centro-simulacion-clinica-avanzada") >= 0 || url.indexOf("universidad-valencia") >= 0 || url.indexOf("universidad-elche") >= 0 || url.indexOf("universidad-castellon") >= 0 || url.indexOf("/becas-universitarias/") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    else if (url.indexOf("/estudios/") >= 0 || url.indexOf("/investigacion/") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2] + '/' + url.split('/')[3];
    }
    else if (url.indexOf("/nuevo-alumno/") >= 0 || url.indexOf("/padres-familias") >= 0 || url.indexOf("/servicios/") >= 0 || url.indexOf("/departamento/") >= 0 || url.indexOf("/conocenos/") >= 0 || url.indexOf("/catedra/") >= 0 || url.indexOf("/instituto/") >= 0 || url.indexOf("/programa-creadores/") >= 0 || url.indexOf("/espacios-avanzados-aprendizaje/") >= 0 || url.indexOf("/grupos-lineas-investigacion/") >= 0 || url.indexOf("/observatorio/") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
    }
    
    else if (url.indexOf("/actividades/") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2] + '/' + url.split('/')[3] + '/' + url.split('/')[4];
    }


    if (url.indexOf("nuevo-alumno/proceso-admision-grado") >= 0)
    {
        window.history.pushState("object or string", document.title, url + '/' + $(this).find('span').text().toLowerCase().replace(/[\*\^\'\!\,\(\)]/g, '').replace(" en ", " ").replace(" /", "").replace(" los ", " ").replace(" de ", " ").replace(" tus ", " ").replace(" y ", " ").replace(" e ", " ").replace(" a ", " ").replace(" ", "-").replace("inicio", "medicina").replace(/á/gi, "a").replace(/é/gi, "e").replace(/í/gi, "i").replace(/ó/gi, "o").replace(/ú/gi, "u").replace(/ñ/gi, "n").split(' ').join('-'));
    }
    else if (!url.indexOf("/area-")) {
        window.history.pushState("object or string", document.title, url + '/' + $(this).find('span').text().toLowerCase().replace(/[\*\^\'\!\,\(\)]/g, '').replace(" en ", " ").replace(" los ", " ").replace(" de ", " ").replace(" una ", " ").replace(" tus ", " ").replace(" /", "").replace(" y ", " ").replace(" e ", " ").replace(" a ", " ").replace(" ", "-").replace("inicio", "").replace(/á/gi, "a").replace(/é/gi, "e").replace(/í/gi, "i").replace(/ó/gi, "o").replace(/ú/gi, "u").replace(/ñ/gi, "n").split(' ').join('-').replace("presentacion", "").replace("ceu-innova", "").replace("diferentes", "").replace("?", "").replace("¿", "").replace("conoce-el-campus", "campus").replace("que-master", "").replace("solo-ir-clase", "").replace("no-te-conformes", "").replace("educacion-4.0", "educacion").replace("instantes-el-campus", "instantes").replace("becas-estudios-grado", "grado").replace("becas-estudios-posgrado", "posgrado").replace("becas-para-estudiantes-internacionales", "internacional").replace("+docencia", "docencia").replace("+conciencia", "conciencia").replace("+enfoques", "enfoques").replace("+transversal", "transversal").replace("n-e-w-s", "news"));
    }
    

});

// Arreglo para generar el padding en móviles para landing pages (resize)
$(window).resize(function(){
 if($(window).width()<775){
  $('.arregloPaddingMovil').removeClass('none-padding');
 }
    if($(window).width()>775){
  $('.arregloPaddingMovil').addClass('none-padding');
 }
});


$(document).ready(function () {
// Arreglo para generar el padding en móviles para landing pages (onload)
if($(window).width()<775){
  $('.arregloPaddingMovil').removeClass('none-padding');
 }
    if($(window).width()>775){
  $('.arregloPaddingMovil').addClass('none-padding');
 }

    var url = window.location.pathname;
    if (url.indexOf("/estudios/posgrado-enero-marzo") >= 0 || url.indexOf("/estudios/posgrado-abril-mayo") >= 0) {
        if (url.indexOf("/area-comunicacion") >= 0) {
            $(".areas-content").show();
            $(".sh_diseno").hide();
            $(".sh_salud").hide();
            $(".sh_veterinaria").hide();
            $(".sh_derecho").hide();
            $(".sh_gastronomia").hide();
            $(".sh_comunicacion").show();
        }
        else if (url.indexOf("/area-diseno") >= 0) {
            $(".areas-content").show();
            $(".sh_salud").hide();
            $(".sh_veterinaria").hide();
            $(".sh_derecho").hide();
            $(".sh_comunicacion").hide();
            $(".sh_gastronomia").hide();
            $(".sh_diseno").show();
        }
        else if (url.indexOf("/area-salud") >= 0) {
            $(".areas-content").show();
            $(".sh_veterinaria").hide();
            $(".sh_derecho").hide();
            $(".sh_comunicacion").hide();
            $(".sh_diseno").hide();
            $(".sh_gastronomia").hide();
            $(".sh_salud").show();
        }
        else if (url.indexOf("/area-veterinaria") >= 0) {
            $(".areas-content").show();
            $(".sh_salud").hide();
            $(".sh_derecho").hide();
            $(".sh_comunicacion").hide();
            $(".sh_diseno").hide();
            $(".sh_gastronomia").hide();
            $(".sh_veterinaria").show();
        }
        else if (url.indexOf("/area-derecho") >= 0) {
            $(".areas-content").show();
            $(".sh_veterinaria").hide();
            $(".sh_salud").hide();
            $(".sh_comunicacion").hide();
            $(".sh_diseno").hide();
            $(".sh_gastronomia").hide();
            $(".sh_derecho").show();
        }
        else if (url.indexOf("/area-gastronomia") >= 0) {
            $(".areas-content").show();
            $(".sh_veterinaria").hide();
            $(".sh_salud").hide();
            $(".sh_comunicacion").hide();
            $(".sh_diseno").hide();
            $(".sh_derecho").hide();
            $(".sh_gastronomia").show();
        }
        else {
            $(".areas-content").hide();
        }
    }

    /*Iconos de áreas*/
    $('.i-educacion').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
        var url = window.location.pathname;
        if (url.indexOf("/estudios") >= 0) {
            url = url.split('/')[0] + '/' + url.split('/')[1];
            window.history.pushState("object or string", document.title, url + '/area-educacion');
        }
    });
    
    $( document ).ready(function() {
        $("#serProfesional11").hide();
        $("#serProfesional22").hide();
        $("#serProfesional33").hide();
        $("#serProfesional44").hide();
        $("#serProfesional55").hide();
        $("#serProfesional66").hide();
        if (window.location.href.indexOf("/soft-skills") > -1 ) {
            $("#serProfesional11").show();
            $("#serProfesional22").hide();
            $("#serProfesional33").hide();
            $("#serProfesional44").hide();
            $("#serProfesional55").hide();
            $("#serProfesional66").hide();
            $('html, body').animate({
            scrollTop: $("#secciones-ser-profesional").offset().top
            }, 1000);
        }
        else if (window.location.href.indexOf("/internacionalizacion") > -1 ){
            $("#serProfesional22").show();
            $("#serProfesional11").hide();
            $("#serProfesional33").hide();
            $("#serProfesional44").hide();
            $("#serProfesional55").hide();
            $("#serProfesional66").hide();
            $('html, body').animate({
            scrollTop: $("#secciones-ser-profesional").offset().top
            }, 1000);
        }
        else if (window.location.href.indexOf("/compromiso-etico") > -1 ){
            $("#serProfesional33").show();
            $("#serProfesional22").hide();
            $("#serProfesional11").hide();
            $("#serProfesional44").hide();
            $("#serProfesional55").hide();
            $("#serProfesional66").hide();
            $('html, body').animate({
            scrollTop: $("#secciones-ser-profesional").offset().top
            }, 1000);
        }
        else if (window.location.href.indexOf("/competencias-instrumentales") > -1 ){
            $("#serProfesional44").show();
            $("#serProfesional22").hide();
            $("#serProfesional33").hide();
            $("#serProfesional11").hide();
            $("#serProfesional55").hide();
            $("#serProfesional66").hide();
            $('html, body').animate({
            scrollTop: $("#secciones-ser-profesional").offset().top
            }, 1000);
        }
        else if (window.location.href.indexOf("/investigacion") > -1 ){
            $("#serProfesional55").show();
            $("#serProfesional22").hide();
            $("#serProfesional33").hide();
            $("#serProfesional44").hide();
            $("#serProfesional11").hide();
            $("#serProfesional66").hide();
            $('html, body').animate({
            scrollTop: $("#secciones-ser-profesional").offset().top
            }, 1000);
        }
        else if (window.location.href.indexOf("/sociabilizacion-laboral") > -1 ){
            $("#serProfesional66").show();
            $("#serProfesional22").hide();
            $("#serProfesional33").hide();
            $("#serProfesional44").hide();
            $("#serProfesional55").hide();
            $("#serProfesional11").hide();
            $('html, body').animate({
            scrollTop: $("#secciones-ser-profesional").offset().top
            }, 1000);
        }
    });


    $('#serProfesional1').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
        var url = window.location.pathname;

        
            $("#serProfesional11").show();
            $("#serProfesional22").hide();
            $("#serProfesional33").hide();
            $("#serProfesional44").hide();
            $("#serProfesional55").hide();
            $("#serProfesional66").hide();
            $('html, body').animate({
            scrollTop: $("#secciones-ser-profesional").offset().top
            }, 1000);


            url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
            window.history.pushState("object or string", document.title, url + '/soft-skills');
        

    });
    $('#serProfesional2').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
        var url = window.location.pathname;

        
            $("#serProfesional22").show();
            $("#serProfesional11").hide();
            $("#serProfesional33").hide();
            $("#serProfesional44").hide();
            $("#serProfesional55").hide();
            $("#serProfesional66").hide();
            $('html, body').animate({
            scrollTop: $("#secciones-ser-profesional").offset().top
            }, 1000);


            url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
            window.history.pushState("object or string", document.title, url + '/internacionalizacion');
        

    });
        $('#serProfesional3').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
        var url = window.location.pathname;

        
            $("#serProfesional33").show();
            $("#serProfesional22").hide();
            $("#serProfesional11").hide();
            $("#serProfesional44").hide();
            $("#serProfesional55").hide();
            $("#serProfesional66").hide();
            $('html, body').animate({
            scrollTop: $("#secciones-ser-profesional").offset().top
            }, 1000);


            url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
            window.history.pushState("object or string", document.title, url + '/compromiso-etico');
        

    });
    $('#serProfesional4').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
        var url = window.location.pathname;

        
            $("#serProfesional44").show();
            $("#serProfesional22").hide();
            $("#serProfesional33").hide();
            $("#serProfesional11").hide();
            $("#serProfesional55").hide();
            $("#serProfesional66").hide();
            $('html, body').animate({
            scrollTop: $("#secciones-ser-profesional").offset().top
            }, 1000);


            url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
            window.history.pushState("object or string", document.title, url + '/competencias-instrumentales');
        

    });
    $('#serProfesional5').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
        var url = window.location.pathname;

        
            $("#serProfesional55").show();
            $("#serProfesional22").hide();
            $("#serProfesional33").hide();
            $("#serProfesional44").hide();
            $("#serProfesional11").hide();
            $("#serProfesional66").hide();
            $('html, body').animate({
            scrollTop: $("#secciones-ser-profesional").offset().top
            }, 1000);


            url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
            window.history.pushState("object or string", document.title, url + '/investigacion');
        


    });
    $('#serProfesional6').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
        var url = window.location.pathname;

        
            $("#serProfesional66").show();
            $("#serProfesional22").hide();
            $("#serProfesional33").hide();
            $("#serProfesional44").hide();
            $("#serProfesional55").hide();
            $("#serProfesional11").hide();
            $('html, body').animate({
            scrollTop: $("#secciones-ser-profesional").offset().top
            }, 1000);


            url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
            window.history.pushState("object or string", document.title, url + '/sociabilizacion-laboral');
        
        




    });
    $('.i-comunicacion').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
        var url = window.location.pathname;

        if (url.indexOf("/estudios/posgrado-enero-marzo") >= 0) {
            $(".areas-content").show();
            $(".sh_diseno").hide();
            $(".sh_salud").hide();
            $(".sh_veterinaria").hide();
            $(".sh_derecho").hide();
            $(".sh_gastronomia").hide();
            $(".sh_deporte").hide();
            $(".sh_comunicacion").show();

            url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
            window.history.pushState("object or string", document.title, url + '/area-comunicacion');
        }
        else if (url.indexOf("/estudios") >= 0) {
            url = url.split('/')[0] + '/' + url.split('/')[1];
            window.history.pushState("object or string", document.title, url + '/area-comunicacion');
        }




    });
    $('.i-marketing').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
        var url = window.location.pathname;
        if (url.indexOf("/estudios") >= 0) {
            url = url.split('/')[0] + '/' + url.split('/')[1];
            window.history.pushState("object or string", document.title, url + '/area-empresa-marketing');
        }



    });
    $('.i-salud').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
        var url = window.location.pathname;
        if (url.indexOf("/estudios/posgrado-enero-marzo") >= 0 || url.indexOf("/estudios/posgrado-abril-mayo") >= 0) {
            $(".areas-content").show();
            $(".sh_comunicacion").hide();
            $(".sh_diseno").hide();
            $(".sh_veterinaria").hide();
            $(".sh_derecho").hide();
            $(".sh_gastronomia").hide();
            $(".sh_deporte").hide();
            $(".sh_salud").show();

            url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
            window.history.pushState("object or string", document.title, url + '/area-ciencias-salud');
        }
       
        else if (url.indexOf("/estudios") >= 0) {
            url = url.split('/')[0] + '/' + url.split('/')[1];
            window.history.pushState("object or string", document.title, url + '/area-ciencias-salud');
        }



    });

    $('.i-arquitectura').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
        var url = window.location.pathname;
        if (url.indexOf("/estudios") >= 0) {
            url = url.split('/')[0] + '/' + url.split('/')[1];
            window.history.pushState("object or string", document.title, url + '/area-arquitectura');
        }
    });

    $('.i-diseno').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
        var url = window.location.pathname;
        if (url.indexOf("/estudios/posgrado-enero-marzo") >= 0 || url.indexOf("/estudios/posgrado-abril-mayo") >= 0 ) {
            $(".areas-content").show();
            $(".sh_comunicacion").hide();
            $(".sh_salud").hide();
            $(".sh_veterinaria").hide();
            $(".sh_derecho").hide();
            $(".sh_gastronomia").hide();
            $(".sh_deporte").hide();
            $(".sh_diseno").show();

            url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
            window.history.pushState("object or string", document.title, url + '/area-diseno');
        }
       
        else if (url.indexOf("/estudios") >= 0) {
            url = url.split('/')[0] + '/' + url.split('/')[1];
            window.history.pushState("object or string", document.title, url + '/area-diseno');
        }
    });

    $('.i-ingenieria').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
        var url = window.location.pathname;
        if (url.indexOf("/estudios") >= 0) {
            url = url.split('/')[0] + '/' + url.split('/')[1];
            window.history.pushState("object or string", document.title, url + '/area-ingenieria');
        }
    });

    $('.i-derecho').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
        var url = window.location.pathname;
        if (url.indexOf("/estudios/posgrado-enero-marzo") >= 0) {
            $(".areas-content").show();
            $(".sh_comunicacion").hide();
            $(".sh_diseno").hide();
            $(".sh_salud").hide();
            $(".sh_veterinaria").hide();
            $(".sh_gastronomia").hide();
            $(".sh_deporte").hide();
            $(".sh_derecho").show();

            url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
            window.history.pushState("object or string", document.title, url + '/area-derecho-politicas');
        }
        else if (url.indexOf("/estudios") >= 0) {
            url = url.split('/')[0] + '/' + url.split('/')[1];
            window.history.pushState("object or string", document.title, url + '/area-derecho-politicas');
        }



    });
    $('.i-veterinaria').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
        var url = window.location.pathname;
        if (url.indexOf("/estudios/posgrado-enero-marzo") >= 0) {
            $(".areas-content").show();
            $(".sh_comunicacion").hide();
            $(".sh_diseno").hide();
            $(".sh_salud").hide();
            $(".sh_derecho").hide();
            $(".sh_gastronomia").hide();
            $(".sh_deporte").hide();
            $(".sh_veterinaria").show();
            url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
            window.history.pushState("object or string", document.title, url + '/area-veterinaria');
        }
        else if (url.indexOf("/estudios") >= 0) {
            url = url.split('/')[0] + '/' + url.split('/')[1];
            window.history.pushState("object or string", document.title, url + '/area-veterinaria');
        }


    });
    $('.i-gastronomia').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
        var url = window.location.pathname;
        if (url.indexOf("/estudios/posgrado-enero-marzo") >= 0) {
            $(".areas-content").show();
            $(".sh_comunicacion").hide();
            $(".sh_salud").hide();
            $(".sh_veterinaria").hide();
            $(".sh_derecho").hide();
            $(".sh_diseno").hide();
            $(".sh_deporte").hide();
            $(".sh_gastronomia").show();

            url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
            window.history.pushState("object or string", document.title, url + '/area-gastronomia');
        }
        else if (url.indexOf("/estudios") >= 0) {
            url = url.split('/')[0] + '/' + url.split('/')[1];
            window.history.pushState("object or string", document.title, url + '/area-gastronomia');
        }


    });
    $('.i-deporte').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
        var url = window.location.pathname;
        if (url.indexOf("/estudios/posgrado-enero-marzo") >= 0) {
            $(".areas-content").show();
            $(".sh_comunicacion").hide();
            $(".sh_salud").hide();
            $(".sh_veterinaria").hide();
            $(".sh_derecho").hide();
            $(".sh_diseno").hide();
            $(".sh_gastronomia").hide();
            $(".sh_deporte").show();

            url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
            window.history.pushState("object or string", document.title, url + '/area-deporte');
        }
        else if (url.indexOf("/estudios") >= 0) {
            url = url.split('/')[0] + '/' + url.split('/')[1];
            window.history.pushState("object or string", document.title, url + '/area-deporte');
        }


    });

});


// Microcredenciales

$(document).ready(function () {
    $("#contenido_inicial").show();
    $("#contenido_click").hide();
});

$(".bullets").on('click', function (event) {
    $("#contenido_inicial").hide();
    $("#contenido_click").show();
});

// navegar por becas

$(document).ready(function () {
    ocultarcontenido();
    if (window.location.href.indexOf("/grado-becas") > -1 || window.location.href.indexOf("/posgrado-becas") > -1 || window.location.href.indexOf("/internacional-becas") > -1) {
        $('.becas_123').show();
        $(".sh_beca").show();
        $(".sh_seguro").hide();
        $(".sh_financiacion").hide();
        $('html, body').animate({
            scrollTop: $("#menu").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/grado-financiacion") > -1 || window.location.href.indexOf("/posgrado-financiacion") > -1 || window.location.href.indexOf("/internacional-financiacion") > -1) {
        $('.becas_123').hide();
        $(".sh_beca").hide();
        $(".sh_seguro").hide();
        $(".sh_financiacion").show();
        $(".parrafo_financiacion").show();
        $('html, body').animate({
            scrollTop: $("#menu").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/grado-seguros") > -1 || window.location.href.indexOf("/posgrado-seguros") > -1 || window.location.href.indexOf("/internacional-seguros") > -1) {
        $('.becas_123').hide();
        $(".sh_beca").hide();
        $(".sh_seguro").show();
        $(".sh_financiacion").hide();
        $('html, body').animate({
            scrollTop: $("#menu").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-colaboracion") > -1) {
        $(".sh_financiacion").hide();
        $(".becas-colaboracion").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-ceu-merit-program") > -1) {
        $(".sh_financiacion").hide();
        $(".becas-ceu-merit-program").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-fundacion") > -1) {
        $(".sh_financiacion").hide();
        $(".becas-fundacion").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/ayudas-puente") > -1) {
        $(".sh_financiacion").hide();
        $(".ayudas-puente").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-impulso") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".impulso").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-acceso-ceu") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas-acceso-ceu").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-campus-life") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas-campus-life").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-matricula-honor") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas-matricula-honor").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-ministerio") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas-ministerio").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-generalitat") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas-generalitat").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-familia-numerosa") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".familia-numerosa").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-federacion-familias") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".federacion-familias").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/financiacion-caixabank") > -1) {
       
        $(".financiacion-caixabank").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/financiacion-santander") > -1) {
      
        $(".financiacion-santander").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/financiacion-sabadell") > -1) {
      
        $(".financiacion-sabadell").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/seguro-continuidad") > -1) {
        $(".sh_financiacion").hide();
        $(".seguro-continuidad").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/seguro-escolar-28") > -1) {
        $(".sh_financiacion").hide();
        $(".seguro-escolar-28").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/seguro-escolar") > -1) {
        $(".sh_financiacion").hide();
        $(".seguro-escolar").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-empresas") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas-empresas").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-deportistas") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas-deportistas").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-destino-gastronomia") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas-destino-gastronomia").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-veterinarios") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas-veterinarios").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-intraemprende") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas-intraemprende").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-ayuntamientos") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas-ayuntamientos").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-victimas-terrorismo") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas-victimas-terrorismo").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-concapa") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas-concapa").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
        // posgrado
    else if (window.location.href.indexOf("/becas-oficiales-posgrado") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas_posgrado_1").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/descuento-alumni") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas_posgrado_2").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/ayuda-colaboracion-posgrado") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas_posgrado_3").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-ayuntamiento-posgrado") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas_posgrado_4").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-santander-posgrado") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas_posgrado_5").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    // internacionales
    else if (window.location.href.indexOf("/becas-internacionales-colaboracion") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas_internacional_1").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    else if (window.location.href.indexOf("/becas-merit-internacional") > -1) {
        $(".sh_financiacion").hide();
        $(".sh_seguro").hide();
        $(".becas_internacional_2").show();
        $('html, body').animate({
            scrollTop: $("#contenido_becas").offset().top
        }, 1000);
    }
    
});

// Grado
$('.list-careers .i-becas').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".sh_beca").show();
    $(".sh_seguro").hide();
    $(".sh_financiacion").hide();
    $('.becas_123').show();
    window.history.pushState("object or string", document.title, url + '/grado-becas');
});

$('.list-careers .i-seguros').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".sh_beca").hide();
    $(".sh_financiacion").hide();
    $(".sh_seguro").show();
    
    window.history.pushState("object or string", document.title, url + '/grado-seguros');
});

$('.list-careers .i-financiacion').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".sh_financiacion").show();
    $(".parrafo_financiacion").show();
    $(".sh_beca").hide();
    $(".sh_seguro").hide();
    window.history.pushState("object or string", document.title, url + '/grado-financiacion');
});

$('.cl_ceu_merit_program').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas-ceu-merit-program").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-ceu-merit-program');
});

$('.cl_becas_acceso_ceu').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas-acceso-ceu").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-acceso-ceu');
});

$('.cl_becas_impulso').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".impulso").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-impulso');
});

$('.cl_ayudas_puente').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".ayudas-puente").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/ayudas-puente');
});

$('.cl_becas_fundacion').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas-fundacion").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-fundacion');
});

$('.cl_becas_colaboracion').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas-colaboracion").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-colaboracion');
});

$('.cl_becas_campus_life').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas-campus-life").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-campus-life');
});

$('.cl_becas_matricula_honor').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas-matricula-honor").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-matricula-honor');
});

$('.cl_becas_ministerio').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas-ministerio").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-ministerio');
});

$('.cl_becas_generalitat').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas-generalitat").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-generalitat');
});

$('.cl_becas_familia_numerosa').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".familia-numerosa").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-familia-numerosa');
});

$('.cl_becas_federacion_familias').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".federacion-familias").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-federacion-familias');
});

$('.cl_financiacion_caixabank').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".financiacion-caixabank").show();
    $(".parrafo_financiacion").show();
    window.history.pushState("object or string", document.title, url + '/financiacion-caixabank');
});

$('.cl_financiacion_santander').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".financiacion-santander").show();
    $(".parrafo_financiacion").show();
    window.history.pushState("object or string", document.title, url + '/financiacion-santander');
});

$('.cl_financiacion_sabadell').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".financiacion-sabadell").show();
    $(".parrafo_financiacion").show();
    window.history.pushState("object or string", document.title, url + '/financiacion-santander');
});

$('.cl_seguro_continuidad').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".seguro-continuidad").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/seguro-continuidad');
});

$('.cl_seguro_escolar_28').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".seguro-escolar-28").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/seguro-escolar-28');
});

$('.cl_seguro_escolar').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".seguro-escolar").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/seguro-escolar');
});

$('.cl_becas_empresas').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas-empresas").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-empresas');
});
$('.cl_becas_deportistas').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas-deportistas").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-deportistas');
});

$('.cl_becas_destino_gastronomia').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas-destino-gastronomia").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-destino-gastronomia');
});

$('.cl_becas_veterinarios').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas-veterinarios").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-veterinarios');
});

$('.cl_becas_intraemprende').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas-intraemprende").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-intraemprende');
});

$('.cl_becas_ayuntamientos').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas-ayuntamientos").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-ayuntamientos');
});

$('.cl_becas_victimas_terrorismo').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas-victimas-terrorismo").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-victimas-terrorismo');
});

$('.cl_becas_concapa').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas-concapa").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-concapa');
});


// Posgrado
$('.list-careers .i-becas-posgrado').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#becas_posgrado").offset().top
    }, 1000);
    ocultarcontenido();
    $(".sh_beca").show();
    $(".sh_seguro").hide();
    $(".sh_financiacion").hide();

    window.history.pushState("object or string", document.title, url + '/posgrado-becas');
});

$('.list-careers .i-seguros-posgrado').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#becas_posgrado").offset().top
    }, 1000);
    ocultarcontenido();
    $(".sh_beca").hide();
    $(".sh_seguro").show();
    $(".sh_financiacion").hide();
    
    window.history.pushState("object or string", document.title, url + '/posgrado-becas');
});

$('.list-careers .i-financiacion-posgrado').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#becas_posgrado").offset().top
    }, 1000);
    ocultarcontenido();
    $(".sh_beca").hide();
    $(".sh_seguro").hide();
    $(".sh_financiacion").show();
    $(".parrafo_financiacion").show();

    window.history.pushState("object or string", document.title, url + '/posgrado-financiacion');
});

$('.cl_becas_posgrado_1').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas_posgrado_1").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-oficiales-posgrado');
});
$('.cl_becas_posgrado_2').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas_posgrado_2").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/descuento-alumni');
});
$('.cl_becas_posgrado_3').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas_posgrado_3").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/ayuda-colaboracion-posgrado');
});

$('.cl_becas_posgrado_4').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas_posgrado_4").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-ayuntamientos-posgrado');
});

$('.cl_becas_posgrado_5').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas_posgrado_5").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/becas-santander-posgrado');
});

$('.cl_financiacion_posgrado_caixabank').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".financiacion-caixabank").show();
    $(".parrafo_financiacion").show();
   
    window.history.pushState("object or string", document.title, url + '/financiacion-caixabank');
});

$('.cl_financiacion_posgrado_santander').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".financiacion-santander").show();
    $(".parrafo_financiacion").show();
   
    window.history.pushState("object or string", document.title, url + '/financiacion-santander');
});

$('.cl_financiacion_posgrado_sabadell').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".financiacion-sabadell").show();
    $(".parrafo_financiacion").show();
   
    window.history.pushState("object or string", document.title, url + '/financiacion-sabadell');
});

$('.cl_seguro_posgrado_escolar').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".seguro-escolar").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/seguro-escolar');
});
$('.cl_seguro_posgrado_internacional_28').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".seguro-escolar-28").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/seguro-escolar-28');
});
$('.cl_seguro_posgrado_continuidad').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".seguro-continuidad").show();
    $(".sh_financiacion").hide();
    window.history.pushState("object or string", document.title, url + '/seguro-continuidad');
});

// Internacional
$('.list-careers .i-becas-internacional').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#becas_internacional").offset().top
    }, 1000);
    ocultarcontenido();
    $(".sh_beca").show();
    $(".sh_seguro").hide();
    $(".sh_financiacion").hide();
    
    window.history.pushState("object or string", document.title, url + '/internacional-becas');
});

$('.list-careers .i-seguros-internacional').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#becas_internacional").offset().top
    }, 1000);
    ocultarcontenido();
    $(".sh_beca").hide();
    $(".sh_seguro").show();
    $(".sh_financiacion").hide();
   
    window.history.pushState("object or string", document.title, url + '/internacional-seguros');
});


$('.cl_becas_internacional_1').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas_internacional_1").show();
   
    window.history.pushState("object or string", document.title, url + '/becas-internacionales-colaboracion');
});
$('.cl_becas_internacional_2').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas_internacional_2").show();
   
    window.history.pushState("object or string", document.title, url + '/becas-merit-internacional');
});
$('.cl_becas_internacional_3').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".impulso").show();
  
    window.history.pushState("object or string", document.title, url + '/becas-impulso');
});
$('.cl_becas_internacional_4').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".becas-campus-life").show();
   
    window.history.pushState("object or string", document.title, url + '/becas-campus-life');
});

$('.cl_seguro_internacional_escolar').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".seguro-escolar").show();
    window.history.pushState("object or string", document.title, url + '/seguro-escolar');
});
$('.cl_seguro_escolar_internacional_28').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".seguro-escolar-28").show();
    
    window.history.pushState("object or string", document.title, url + '/seguro-escolar-28');
});
$('.cl_seguro_internacional_continuidad').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/becas-universitarias") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#contenido_becas").offset().top
    }, 1000);
    ocultarcontenido();
    $(".seguro-continuidad").show();
    
    window.history.pushState("object or string", document.title, url + '/seguro-continuidad');
});

$('.volver_menu').on('click', function (event) {
   
    $('html, body').animate({
        scrollTop: $("#menu").offset().top
    }, 1000);
    // ocultamos info de becas
    ocultarcontenido();
   
});

$('.mostrar-cajas-internacional').on('click', function (event) {
    // cambiar urls en menús sin recargar la página

    $(".cl_becas_internacional_1").show();
    $(".cl_becas_internacional_2").show();
    $(".cl_becas_internacional_3").show();
    $(".cl_becas_internacional_4").show();
    $(".cl_seguro_internacional_escolar").show();
    $(".cl_seguro_escolar_internacional_28").show();
    $(".cl_seguro_internacional_continuidad").show();
    $(".sh_financiacion").hide();
});

function ocultarcontenido()
{
    $(".parrafo_financiacion").hide();
    $(".becas-ceu-merit-program").hide();
    $(".becas-fundacion").hide();
    $(".ayudas-puente").hide();
    $(".impulso").hide();
    $(".becas-acceso-ceu").hide();
    $(".becas-colaboracion").hide();
    $(".becas-campus-life").hide();
    $(".becas-matricula-honor").hide();
    $(".becas-ministerio").hide();
    $(".becas-generalitat").hide();
    $(".familia-numerosa").hide();
    $(".federacion-familias").hide();
    $(".financiacion-caixabank").hide();
    $(".financiacion-santander").hide();
    $(".financiacion-sabadell").hide();
    $(".seguro-continuidad").hide();
    $(".seguro-escolar-28").hide();
    $(".seguro-escolar").hide();
    $(".becas-empresas").hide();
    $(".becas-deportistas").hide();
    $(".becas-destino-gastronomia").hide();
    $(".becas-veterinarios").hide();
    $(".becas-intraemprende").hide();
    $(".becas-ayuntamientos").hide();
    $(".becas-victimas-terrorismo").hide();
    $(".becas-concapa").hide();
    // posgrado
    $(".becas_posgrado_1").hide();
    $(".becas_posgrado_2").hide();
    $(".becas_posgrado_3").hide();
    $(".becas_posgrado_4").hide();
    $(".becas_posgrado_5").hide();
    // internacional
    $(".becas_internacional_1").hide();
    $(".becas_internacional_2").hide();
}

// navegar por los campus

$('.i-campos-gorriz').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-valencia") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);
    window.history.pushState("object or string", document.title, url + '/edificio-luis-campos-gorriz');
});

$('.i-rectorado').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-valencia") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);
    window.history.pushState("object or string", document.title, url + '/edificio-rectorado');
});

$('.i-clinica-odontologica').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-valencia") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);
    if (!url.indexOf("/conocenos/espacios-avanzados-aprendizaje")) {
        window.history.pushState("object or string", document.title, url + '/clinica-odontologica-universitaria');
    }
});

$('.i-facultad-salud').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-valencia") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);
    window.history.pushState("object or string", document.title, url + '/facultad-ciencias-salud');
});

$('.i-facultad-veterinaria').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-valencia") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);
    window.history.pushState("object or string", document.title, url + '/facultad-veterinaria');
});

$('.i-eset').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-valencia") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);
    window.history.pushState("object or string", document.title, url + '/eset');
});

$('.i-hospital-clinico').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-valencia") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    if (!url.indexOf("/conocenos/espacios-avanzados-aprendizaje")) {
        window.history.pushState("object or string", document.title, url + '/hospital-clinico-veterinario');
    }
    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);
});


$('.i-edificio-biblioteca').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-valencia") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);
    window.history.pushState("object or string", document.title, url + '/biblioteca-crai');
});

$('.i-centro-multimedia').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-valencia") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    if (!url.indexOf("/conocenos/espacios-avanzados-aprendizaje")) {
        window.history.pushState("object or string", document.title, url + '/centro-produccion-multimedia');
    }
    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);
});

$('.i-granja-docente').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-valencia") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    if (!url.indexOf("/conocenos/espacios-avanzados-aprendizaje")) {
        window.history.pushState("object or string", document.title, url + '/granja-docente-investigacion-veterinaria');
    }
    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);
});

$('.i-palacio-colomina').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-valencia") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);
    window.history.pushState("object or string", document.title, url + '/palacio-colomina');
});


$('.i-espacios').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-valencia") >= 0 || url.indexOf("/universidad-castellon") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);
    window.history.pushState("object or string", document.title, url + '/espacios-avanzados-aprendizaje');
});

$('.i-plaza-reyes-catolicos').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-elche") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }
    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);
    window.history.pushState("object or string", document.title, url + '/edificio-plaza-reyes-catolicos');
});


$('.i-carmelitas').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-elche") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }

    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);

    window.history.pushState("object or string", document.title, url + '/edificio-carmelitas');

});

$('.i-castellon').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-castellon") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }

    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);

    window.history.pushState("object or string", document.title, url + '/instalaciones');

});

$('.i-gasma').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-castellon") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }

    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);

    window.history.pushState("object or string", document.title, url + '/campus-gasma');

});

$('.i-sportarea').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-valencia") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }

    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);

    window.history.pushState("object or string", document.title, url + '/sportarea');

});

$('.i-paraninfo').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/universidad-valencia") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1];
    }

    $('html, body').animate({
        scrollTop: $("#mapa").offset().top
    }, 2000);

    window.history.pushState("object or string", document.title, url + '/paraninfo');

});



jQuery(function () {
    jQuery('.tabs-navigation .tab-ctrl').on('click', function () {
        setTimeout(function () {
            window.dispatchEvent(new Event('resize'));
        }, 500)
    })
});

jQuery(function () {
    jQuery('span.btn.open-modal').on('click', function () {
        setTimeout(function () {
            window.dispatchEvent(new Event('resize'));
        }, 500)
    })
});


function getUrl() {
    var url = window.location.href + "?";
    if (url.indexOf("&") >= 0) {
        url = url.split('&')[0] + "&";
    } else if (url.indexOf("?grado=") >= 0 || url.indexOf("?posgrado=") >= 0 || url.indexOf("?capacitacion=") >= 0) {
        url = window.location.href + "&";
    } else if (url.indexOf("?") >= 0) {
        url = url.split('?')[0] + "?";
    }
    return url;
}



/* foco en los campos del formulario */
$('.i-estudiante').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    window.history.pushState("object or string", document.title, getUrl() + 'p=estudiante');
});

$('.i-padre').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    window.history.pushState("object or string", document.title, getUrl() + 'p=padre');
});


$('.i-nombre').on('focus', function (event) {
    // cambiar urls en menús sin recargar la página
    if ($(this).is(':invalid')) {
        window.history.pushState("object or string", document.title, getUrl() + 'p=nombre');
    }
    
});

$('.i-apellidos').on('focus', function (event) {
    // cambiar urls en menús sin recargar la página
    if ($(this).is(':invalid')) {
        window.history.pushState("object or string", document.title, getUrl() + 'p=apellido');
    }
});

$('.i-email').on('focus', function (event) {
    // cambiar urls en menús sin recargar la página
    if ($(this).is(':invalid')) {
        window.history.pushState("object or string", document.title, getUrl() + 'p=email');
    }
});

$('.i-pais').on('change', function (event) {
    // cambiar urls en menús sin recargar la página
    if ($(this).is(':invalid')) {
        window.history.pushState("object or string", document.title, getUrl() + 'p=pais');
    }
});

$('.i-dni').on('focus', function (event) {
    // cambiar urls en menús sin recargar la página
    if ($(this).is(':invalid')) {
        window.history.pushState("object or string", document.title, getUrl() + 'p=dni');
    }
});

$('.i-pasaporte').on('focus', function (event) {
    // cambiar urls en menús sin recargar la página
    if ($(this).is(':invalid')) {
        window.history.pushState("object or string", document.title, getUrl() + 'p=pasaporte');
    }
});

/* foco en los campos del formulario */
$('.i-telefono').on('focus', function (event) {
    // cambiar urls en menús sin recargar la página
    if ($(this).is(':invalid')) {
        window.history.pushState("object or string", document.title, getUrl() + 'p=telefono');
    }
});

$('.i-procedencia').on('change', function (event) {
    // cambiar urls en menús sin recargar la página
    window.history.pushState("object or string", document.title, getUrl() + 'p=procedencia');
});

$('.i-tipo').on('change', function (event) {
    // cambiar urls en menús sin recargar la página
    window.history.pushState("object or string", document.title, getUrl() + 'p=tipo');
});

/* foco en los campos del formulario */
$('.i-area').on('change', function (event) {
    // cambiar urls en menús sin recargar la página
    window.history.pushState("object or string", document.title, getUrl() + 'p=area');
});

/* foco en los campos del formulario */
$('.i-titulacion').on('change', function (event) {
    // cambiar urls en menús sin recargar la página
    window.history.pushState("object or string", document.title, getUrl() + 'p=titulacion');
});

/* foco en los campos del formulario */
$('.i-campus').on('change', function (event) {
    // cambiar urls en menús sin recargar la página
    window.history.pushState("object or string", document.title, getUrl() + 'p=campus');
});

/* foco en los campos del formulario */
$('.i-aviso-legal').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    window.history.pushState("object or string", document.title, getUrl() + 'p=aviso-legal');
});

/* foco en los campos del formulario */
$('.i-siguiente').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    window.history.pushState("object or string", document.title, getUrl() + 'p=paso-2');
});

/*Acordeon*/
	$(document).on('click', '.cover-acordeon-intro .tag',function(event) {
		event.preventDefault();
		$(this).toggleClass('active');
		$(this).next('.acordeon-box').stop().slideToggle(300);
		$(this).closest('.acordeon').siblings('.acordeon').find('.tag').removeClass('active');
		$(this).closest('.acordeon').siblings('.acordeon').find('.acordeon-box').removeClass('active').slideUp(300);
	});
	if($('.cover-acordeon-intro .tag').is('.active')){
		$('.cover-acordeon-intro .tag.active').next('.acordeon-box').slideDown(300);
	}

//SER SOSTENIBLE
$('.i-reto').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/ser-sostenible") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
    }
    window.history.pushState("object or string", document.title, url + '/reto');
});
$('.i-podcast').on('click', function (event) {
    // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("/ser-sostenible") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
    }
    window.history.pushState("object or string", document.title, url + '/podcast');
});
//Urls para investigación
$('.i-docencia').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("investigacion") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
        window.history.pushState("object or string", document.title, url + '/docencia');
    }
});
$('.i-ciencia').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("investigacion") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
        window.history.pushState("object or string", document.title, url + '/ciencia-con-conciencia');
    }
});
$('.i-enfoques').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("investigacion") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
        window.history.pushState("object or string", document.title, url + '/enfoques');
    }
});
$('.i-news').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("investigacion") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
        window.history.pushState("object or string", document.title, url + '/news');
    }
});
$('.i-organizacion').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("investigacion") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
        window.history.pushState("object or string", document.title, url + '/organizacion');
    }
});
$('.i-investigacion').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("investigacion") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
        window.history.pushState("object or string", document.title, url + '/lineas-investigacion');
    }
});
$('.i-convocatorias').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("investigacion") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
        window.history.pushState("object or string", document.title, url + '/convocatorias');
    }
});
$('.i-inicio').on('click', function (event) {
        // cambiar urls en menús sin recargar la página
    var url = window.location.pathname;
    if (url.indexOf("investigacion") >= 0) {
        url = url.split('/')[0] + '/' + url.split('/')[1] + '/' + url.split('/')[2];
        window.history.pushState("object or string", document.title, url);
    }
});




