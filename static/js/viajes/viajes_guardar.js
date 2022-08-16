_actualizar=false
function viajes_guardar(event){

    $(".error").remove()


    /*--------------------------------------------------------------- VIEAJE ---------------------------------------------------------------*/

    subsistema_seleccionada=_decodificar($("#subsistema").data("object"))

    

    id_subsistema=null;
    codigo_subsistema=null;
    if(_getDecodificarOption("#subsistema","object")){
        id_subsistema=_getDecodificarOption("#subsistema","object").id;
        codigo_subsistema=_getDecodificarOption("#subsistema","object").codigo;
    }
 

 


    viaje = {}
    if(_actualizar){
        viaje.id=_viaje.id
    }


    viaje.declaracion=$($("[name=declaracion]")[0]).val()
    viaje.mt_subsistema_id=$($("[name=mt_subsistema_id]")[0]).val()
    viaje.mt_bote_id=$($("[name=mt_bote_id]")[0]).val()
    viaje.fecha=$($("[name=fecha]")[0]).val()
    viaje.temporada=$($("[name=temporada]")[0]).val()
    viaje.n_trampas_agua=$($("[name=n_trampas_agua]")[0]).val()
    viaje.n_trampas_visitadas=$($("[name=n_trampas_visitadas]")[0]).val()
    viaje.mt_especie_id=$($("[name=mt_especie_id]")[0]).val()
    viaje.comentario=$($("[name=comentario]")[0]).val()

    

    fecha=_getFecha(viaje.fecha,true)
    if(fecha)viaje.trimpcode=codigo_subsistema+(_getDecodificarOption("#bote","object")?_getDecodificarOption("#bote","object").matricula:'')+fecha[0]+fecha[1]+fecha[2]

  
    //console.log(codigo_subsistema+(_getDecodificarOption("#bote","object")?_getDecodificarOption("#bote","object").numero:'')+fecha[0]+fecha[1]+fecha[2])

    let error="";
    let carnada_error=""
    let trampa_error=""

    if(_empty(viaje.mt_subsistema_id)){
       error="Este campo es obligatorio."
       $($("[name=mt_subsistema_id]")[0]).after(`<span class="error text-danger">${error}</span>`)
    }

    if(_empty(viaje.mt_bote_id)){
        error="Este campo es obligatorio."
        $($("[name=mt_bote_id]")[0]).after(`<span class="error text-danger">${error}</span>`)
    }

    if(_empty(viaje.fecha)){
        error="Este campo es obligatorio."
        $($("[name=fecha]")[0]).after(`<span class="error text-danger">${error}</span>`)
    }
    
    if(_empty(viaje.mt_especie_id)){
        error="Este campo es obligatorio."
        $($("[name=mt_especie_id]")[0]).after(`<span class="error text-danger">${error}</span>`)
    }

    if(!isNaN((viaje.n_trampas_agua).trim())){
        viaje.n_trampas_agua=Number((viaje.n_trampas_agua).trim())
    }else{
        error="El valor ingresado no corresponde a un valor numérico"
        $($("[name=n_trampas_agua]")[0]).after(`<span class="error text-danger">${error}</span>`)
    }

    if(!isNaN((viaje.n_trampas_visitadas).trim())){
        viaje.n_trampas_visitadas=Number((viaje.n_trampas_visitadas).trim())
    }else{
        error="El valor ingresado no corresponde a un valor numérico"
        $($("[name=n_trampas_visitadas]")[0]).after(`<span class="error text-danger">${error}</span>`)
    }

    if(viaje.n_trampas_agua && viaje.n_trampas_agua<0){
        error="El valor ingresado no puede ser menor a 0"
        $($("[name=n_trampas_agua]")[0]).after(`<span class="error text-danger">${error}</span>`)
    }

    if(viaje.n_trampas_visitadas && viaje.n_trampas_visitadas<0){
        error="El valor ingresado no puede ser menor a 0"
        $($("[name=n_trampas_visitadas]")[0]).after(`<span class="error text-danger">${error}</span>`)
    }

    if( ( viaje.n_trampas_agua.toString().length>0 && viaje.n_trampas_visitadas.toString().length>0 ) &&  viaje.n_trampas_agua < viaje.n_trampas_visitadas){
        error="El número de trampas visitadas no puede ser mayor al número de trampas en el agua."
        $($("[name=n_trampas_visitadas]")[0]).after(`<span class="error text-danger">${error}</span>`)
    }

    //console.log(viaje)

    /*--------------------------------------------------------------- FIN VIEAJE ---------------------------------------------------------------*/

    /*--------------------------------------------------------------- TRAMPAS ---------------------------------------------------------------*/
    list_trampas_historicas=[]
    $(".trampas").each(function(){
        trampa_historico= {}
        trampa_historico.viaje_id=viaje.id
        trampa_historico.mt_sector_id=!_empty($($($(this).find("[name=mt_sector_id]"))[0]).val())?$($($(this).find("[name=mt_sector_id]"))[0]).val():null
        trampa_historico.otro_sector=!_empty($($($(this).find("[name=otro_sector]"))[0]).val())?$($($(this).find("[name=otro_sector]"))[0]).val():null
        trampa_historico.ventana_escape=!_empty($($($(this).find("[name=ventana_escape]"))[0]).val())?$($($(this).find("[name=ventana_escape]"))[0]).val():null
        trampa_historico.num_comercial=!_empty($($($(this).find("[name=num_comercial]"))[0]).val())?$($($(this).find("[name=num_comercial]"))[0]).val().trim():null
        trampa_historico.num_no_comercial=!_empty($($($(this).find("[name=num_no_comercial]"))[0]).val())?$($($(this).find("[name=num_no_comercial]"))[0]).val().trim():null
        trampa_historico.bycatch_id=!_empty($($($(this).find("[name=bycatch_id]"))[0]).val())?$($($(this).find("[name=bycatch_id]"))[0]).val().trim():null
        trampa_historico.observaciones=!_empty($($($(this).find("[name=observaciones]"))[0]).val())?$($($(this).find("[name=observaciones]"))[0]).val():null
        trampa_historico.bycatch_cantidad=!_empty($($($(this).find("[name=bycatch_cantidad]"))[0]).val())?$($($(this).find("[name=bycatch_cantidad]"))[0]).val().trim():null
        

        if(_empty(trampa_historico.mt_sector_id)){
            trampa_error="Este campo es obligatorio."
            $($(this).find("[name=mt_sector_id]")[0]).parent().append(`<span class="error text-danger">${trampa_error}</span>`)
        }
        if(trampa_historico.mt_sector_id=="otro"){
            trampa_historico.mt_sector_id=null;
            if(_empty(trampa_historico.otro_sector)){
                trampa_error="Este campo es obligatorio."
                $($(this).find("[name=otro_sector]")[0]).after(`<span class="error text-danger">${trampa_error}</span>`)
            }
            
        }

        if(_empty(trampa_historico.num_comercial)){
            trampa_error="Este campo es obligatorio, si no tiene información escriba: na"
            $($(this).find("[name=num_comercial]")[0]).parent().append(`<span class="error text-danger">${trampa_error}</span>`)
        }else{
            if( (trampa_historico.num_comercial+"").trim().toLocaleLowerCase()=="na"){
                trampa_historico.num_comercial=null;
            }else{
                if(!isNaN((trampa_historico.num_comercial).trim())){
                    trampa_historico.num_comercial=Number((trampa_historico.num_comercial).trim())
                }else{
                    trampa_error="El valor ingresado no corresponde a un valor numérico"
                    $($(this).find("[name=num_comercial]")[0]).parent().append(`<span class="error text-danger">${trampa_error}</span>`)
                }
            }
        }

        if(_empty(trampa_historico.num_no_comercial)){
            trampa_error="Este campo es obligatorio, si no tiene información escriba: na"
            $($(this).find("[name=num_no_comercial]")[0]).parent().append(`<span class="error text-danger">${trampa_error}</span>`)
        }else{
            if( (trampa_historico.num_no_comercial+"").trim().toLocaleLowerCase()=="na"){
                trampa_historico.num_no_comercial=null;
            }else{
                if(!isNaN((trampa_historico.num_no_comercial).trim())){
                    trampa_historico.num_no_comercial=Number((trampa_historico.num_no_comercial).trim())
                }else{
                    trampa_error="El valor ingresado no corresponde a un valor numérico"
                    $($(this).find("[name=num_no_comercial]")[0]).parent().append(`<span class="error text-danger">${trampa_error}</span>`)
                }
            }
        }

        if(!_empty(trampa_historico.ventana_escape)){
            if(trampa_historico.ventana_escape=="na"){
                trampa_historico.ventana_escape=null;
            }else{
                trampa_historico.ventana_escape=trampa_historico.ventana_escape=="si"?true:false
            }
        }else{

            trampa_error="Este campo es obligatorio."
            $($(this).find("[name=ventana_escape]")[0]).after(`<span class="error text-danger">${trampa_error}</span>`)
        }

        if(!_empty(trampa_historico.bycatch_id)){
            if(trampa_historico.bycatch_id=="na"){
                trampa_historico.bycatch_id=null;
            }
        }else{

            trampa_error="Este campo es obligatorio."
            $($(this).find("[name=bycatch_id]")[0]).after(`<span class="error text-danger">${trampa_error}</span>`)
        }

        if(trampa_historico.bycatch_id){

            if(_empty(trampa_historico.bycatch_cantidad)){
                trampa_error="Este campo es obligatorio, si no tiene información escriba: na"
                $($(this).find("[name=bycatch_cantidad]")[0]).parent().append(`<span class="error text-danger">${trampa_error}</span>`)
            }else{
                if( (trampa_historico.bycatch_cantidad+"").trim().toLocaleLowerCase()=="na"){
                    trampa_historico.bycatch_cantidad=null;
                }else{
                    if(!isNaN((trampa_historico.bycatch_cantidad).trim())){
                        trampa_historico.bycatch_cantidad=Number((trampa_historico.bycatch_cantidad).trim())
                    }else{
                        trampa_error="El valor ingresado no corresponde a un valor numérico"
                        $($(this).find("[name=bycatch_cantidad]")[0]).parent().append(`<span class="error text-danger">${trampa_error}</span>`)
                    }
                }
            }


        }else{
            trampa_historico.bycatch_cantidad=null;
        }

        list_trampas_historicas.push(trampa_historico)
        
    });
    /*--------------------------------------------------------------- FIN TRAMPAS ---------------------------------------------------------------*/

    /*--------------------------------------------------------------- REGISTRO DE CARNADAS ---------------------------------------------------------------*/
    list_carnadas=[]
    $(".carnadas_padre").each(function(){

        carnada_registro = {}

        carnada = _decodificar(($($($(this).find("[name=carnada_mt_especie_id]"))[0]).val()))
        if(!carnada){
            carnada_error="Este campo es obligatorio."
            $($($(this).find("[name=carnada_mt_especie_id]"))[0]).parent().append(`<span class="error text-danger">${carnada_error}</span>`);
        }

        unidad_id = _decodificar(($($($(this).find("[name=mt_unidad_id]"))[0]).val()))
        volumen=$($($(this).find("[name=volumen]"))[0]).val()

        carnada_registro.viaje_id=viaje.id
        carnada_registro.mt_especie_id=carnada?carnada.id:null
        carnada_registro.mt_unidad_id=!_empty(unidad_id)?unidad_id:null;
        carnada_registro.volumen=!_empty(volumen)?volumen:null
        list_carnadas.push(carnada_registro)
        
    });
    //console.log(list_carnadas)

    /* FIN REGISTRO DE CARNADAS ---------------------------------------------------------------*/
    

    if(carnada_error.length>0)viajes_cambiar('carnadas');
    if(carnada_error.length==0 && trampa_error.length>0 )viajes_cambiar('trampas');
    

    if( error.length>0 || carnada_error.length>0 || trampa_error.length>0 )event.preventDefault();;

    viaje.list_carnadas=list_carnadas
    viaje.list_trampas_historicas=list_trampas_historicas

    

    $("#viaje_send").val(JSON.stringify(viaje))
   
    

}


$(document).ready(function(){
    modificar()
})

function modificar(){

    if(!_viaje)return
    _actualizar=true
    $(".viaje_titulo").text("EDITAR VIAJE #"+_viaje.id)


   

    $($("[name=declaracion]")[0]).val(_viaje.declaracion)

    $("[name=mt_subsistema_id] option[value="+ _viaje.mt_subsistema +"]").attr("selected",true);
    viajes_seleccionarSubsistema(_viaje.mt_bote)
    
    $($("[name=fecha]")[0]).val(_viaje.fecha)
    $($("[name=temporada]")[0]).val(_viaje.temporada)
    $($("[name=n_trampas_agua]")[0]).val(_viaje.n_trampas_agua)
    $($("[name=n_trampas_visitadas]")[0]).val(_viaje.n_trampas_visitadas)

    //console.log(_viaje.trampa_historico)
    trampas_ntrampas(_viaje.trampa_historico)
    
    //$($("[name=mt_especie_id]")[0]).val("")

    $("[name=mt_especie_id] option:selected").removeAttr('selected');
    $("[name=mt_especie_id] option[value="+_viaje.mt_especie+"]").attr("selected",true);

    $($("[name=comentario]")[0]).val(_viaje.comentario)

    $(".carnadas_padre").remove();
    if(_viaje.carnada_registro){
        for (let c = 0; c < _viaje.carnada_registro.length; c++) {
            const carnada = _viaje.carnada_registro[c];
            carnadas_add(carnada)
            
        }
    }   
            
            
  
  
}

