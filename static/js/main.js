
function _fotmatearFecha(fecha){
    if(!fecha)return "";

    fecha=fecha.split("-")
    hora=""
    if(fecha[2].length>4){
        _fecha=fecha[2].split(" ")
        fecha[2]=_fecha[0]
        if(_fecha.length>1){
            hora=_fecha[1].split(":")
            hora = " a las "+hora[0]+":"+hora[1]+" hrs"
        }
    }

    return fecha[2]+"-"+fecha[1]+"-"+fecha[0]+hora
}

function _codificar(data){
    if(!data)return ""
    data = JSON.stringify(data).replace(/"/gi,'&&cod&&')
    
    return data
}
function _decodificar(data){
    if(!data)return null
    data=JSON.stringify(data.replace(/&&cod&&/gi,'"'))
   

    return JSON.parse(JSON.parse(data))
}

//retorna un arreglo con los datos de la fecha d,m,y
//ej:[18, 3, 2022]
function _getFecha(fecha,ceros=false){
    fecha = fecha.replace(/[/]/g,"-")
    fecha = fecha.split("-")
    if(fecha.length!=3)return null

    if(!ceros)return [fecha[0].toString().trim().length==4? Number.parseInt(fecha[2].substring(0,1)=="0"?fecha[2].replace("0",""):fecha[2]): Number.parseInt(fecha[0].substring(0,1)=="0"?fecha[0].replace("0",""):fecha[0])
                        , Number.parseInt(fecha[1].substring(0,1)=="0"?fecha[1].replace("0",""):fecha[1])
                        ,Number.parseInt(fecha[0].toString().trim().length==4?fecha[0]:fecha[2])]

    return [fecha[0].toString().trim().length==4?fecha[2]:fecha[0],fecha[1],fecha[0].toString().trim().length==4?fecha[0]:fecha[2]]
}

function _empty(valor){

    return !valor || valor.toString().trim().length == 0? true: false;
}

function _getDecodificarOption(selector,data){
    var v = _decodificar($(selector).find(':selected').data(data))
    if(!v || v==null || v == undefined){
        return null
    }
    return v
}