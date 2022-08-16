

function viajes_cambiar(vista,elemento){

    $("#viaje").hide()
    $("#trampas").hide()
    $("#carnadas").hide()
    $(".pointer").removeClass("active")
    $(".pointer").addClass("text-white")

    if(vista=="viaje"){
      $("#viaje").show()
      $("#btn_viaje").addClass("active")
      $("#btn_viaje").removeClass("text-white")
    }
    if(vista=="trampas"){
      $("#trampas").show()
      $("#btn_trampas").addClass("active")
      $("#btn_trampas").removeClass("text-white")
    }
    if(vista=="carnadas"){
        
      $("#carnadas").show()
      $("#btn_carnadas").addClass("active")
      $("#btn_carnadas").removeClass("text-white")
    }
  }



//




var botes=[]

/*
//islas
ipcRenderer.send('all:isla')
ipcRenderer.on('all:isla:response',(e,args)=>{
    const  islas=JSON.parse(args)
    //console.log(islas)
    for (let i = 0; i < islas.length; i++) {
      $('#isla').append('<option data-object="'+_codificar(islas[i])+'" value="'+islas[i].id+'">'+islas[i].codigo+" - "+islas[i].descripcion+'</option>')
    }
})

//especies
ipcRenderer.send('all:especie')
ipcRenderer.on('all:especie:response',(e,args)=>{
    const  especie=JSON.parse(args)
    //console.log(especie)
    for (let i = 0; i < especie.length; i++) {
    $('#especie').append('<option value="'+especie[i].id+'"   '+(especie[i].defecto?"selected=\"\"":"")+'  >'+especie[i].nombre+'</option>')
    }
})

//bycatch
let  bycatch=[]
ipcRenderer.send('all:bycatch')
ipcRenderer.on('all:bycatch:response',(e,args)=>{
    bycatch=JSON.parse(args)
    //console.log(bycatch)
    
})
*/


function viajes_seleccionarSubsistema(bote_id=null){
    id_isla = $("#subsistema").val()

    if(!id_isla){
      return;
    }

    $("#bote").val('')
    $("#bote option[data-subsistema]").hide()
    $("#bote option[data-subsistema="+id_isla+"]").show()

    if(bote_id){

        $("[name=mt_bote_id] option[value="+ bote_id +"]").attr("selected",true);
    }

    if(bote_id==null){
        sectores_agregar_datos()
    }

}




function viajes_cambioFecha(elemento){
    fecha=null
    if($(elemento).val())fecha = _getFecha($(elemento).val())
    if(!fecha)return;

   fecha[1]<10?$("#viaje_temporada").val(fecha[2]-1):$("#viaje_temporada").val(fecha[2])

}

function sectores_agregar_datos(trampa_historico=null){
   

        //console.log(sectores)

        //http://127.0.0.1:8000/api/v1/sector/by/subsistema/3/

        var crf_token = $('#csrfmiddlewaretoken').attr('value');

        id_subsistema = $("#subsistema").val()

        $.ajax({
            type: "POST",
            url: "/api/v1/sector/by/subsistema/"+id_subsistema+"/",
            data: {},
            headers:{"X-CSRFToken": crf_token},
            success: function (sectores) {

                //console.log(sectores)
                $(".sector").children().remove()
                //sector = $(elemento).parent().parent().parent().find(".sector")
         
                
                $(".sector").append('<option value="">Seleccione...</option>')
                $(".sector").append('<option value="otro">Otro Sector</option>')
                for (let i = 0; i < sectores.length; i++) {
                    $(".sector").append('<option value="'+sectores[i].id+'">'+sectores[i].nombre+'</option>')
                }

                

                $(".sector").select2();

                //si existen trampas es por que está editando
                if(trampa_historico){
                    for (let i = 0; i < trampa_historico.length; i++) {
                        const trampa = trampa_historico[i];
                        if(trampa.mt_sector){
                            $($(".trampas")[i]).find('.select2-selection__rendered').text(trampa.mt_sector)//es el texto del del select del sector
                            $($(".trampas")[i]).find("[name=mt_sector_id] option[value="+( trampa.mt_sector?trampa.mt_sector:'')+"]").attr("selected",true);
                        }else{
                            $($(".trampas")[i]).find('.select2-selection__rendered').text("Otro Sector")
                            $($(".trampas")[i]).find("[name=mt_sector_id] option[value=otro]").attr("selected",true);
                            trampas_cambio_sector( $($($(".trampas")[i]).find("[name=mt_sector_id]"))[0] )
                            $($(".trampas")[i]).find("[name=otro_sector]").val(trampa.otro_sector)
                        }

                        $($(".trampas")[i]).find("[name=ventana_escape] option[value="+( trampa.ventana_escape?(trampa.ventana_escape?'si':'no'):'na' )+"]").attr("selected",true);
                        $($(".trampas")[i]).find("[name=num_comercial]").val((trampa.num_comercial?trampa.num_comercial:'na'))
                        $($(".trampas")[i]).find("[name=num_no_comercial]").val((trampa.num_no_comercial?trampa.num_no_comercial:'na'))
                        $($(".trampas")[i]).find("[name=bycatch_id] option[value="+( trampa.bycatch?trampa.bycatch:'na' )+"]").attr("selected",true);
                        $($(".trampas")[i]).find("[name=bycatch_cantidad]").val((trampa.bycatch_cantidad?trampa.bycatch_cantidad:'na'))
                        $($(".trampas")[i]).find("[name=observaciones]").val(trampa.observaciones)


                        
                        opbycatch=$($(".trampas")[i]).find("[name=bycatch_id] option")
                        //console.log(opbycatch[1])
                        //trampas_cambio_bycatch(opbycatch[0])
                    }
                }


            },
            error: function () {
                alert("There was an error")
            }
        });
   

        

   
}
