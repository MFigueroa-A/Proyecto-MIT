import { Injectable } from '@angular/core';

@Injectable()
export class BasictableService {
  private tabla:Tabla[]=[
    {
      primer_nombre:"Deshmukh",
      segundo_nombre:"Prohaska",
      usuario:"@Genelia",
      rol:"Administrador"
    },
    {
      primer_nombre:"Deshmukh",
      segundo_nombre:"Gaylord",
      usuario:"	@Ritesh",
      rol:"Miembro"
    },
    {
      primer_nombre:"Sanghani",
      segundo_nombre:"Sanghani",
      usuario:"@Govinda",
      rol:"Desarollador"
    },
    {
      primer_nombre:"Roshan",
      segundo_nombre:"Roshan",
      usuario:"@Hritik",
      rol:"Soporte"
    },
    {
      primer_nombre:"Joshi",
      segundo_nombre:"Hickle",
      usuario:"@Maruti",
      rol:"Miembro"
    },
    {
      primer_nombre:"Nigam",
      segundo_nombre:"Nigam",
      usuario:"@Sonu",
      rol:"Soporte"
    }
  ];
  constructor(){
    console.log("Servicio de tabla basica")
  }
  gettabla():Tabla[]{
    return this.tabla;
  }
}
export interface Tabla{
  primer_nombre:string;
  segundo_nombre:string;
  usuario:string;
  rol:string;
};
