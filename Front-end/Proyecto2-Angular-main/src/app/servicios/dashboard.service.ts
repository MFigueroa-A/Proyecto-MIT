import { Injectable } from '@angular/core';

@Injectable()

export class DashboardService {
  private ventas:Venta[]=[
    {
      nombre: "Elite Admin",
      estado: "Vendido",
      fecha: "April 18,2021",
      precio:24,
      colorprecio:"text-success"
    },
    {
      nombre:"Real Homes WP Theme",
      estado:"Extendido",
      fecha:"April 19,2021",
      precio:1250,
      colorprecio:"text-info"
    },
    {
      nombre:"Ample Admin",
      estado:"Extendido",
      fecha:"April 19, 2021",
      precio:1250,
      colorprecio:"text-info"
    },
    {
      nombre:"Medical Pro WP Theme",
      estado:"Impuesto",
      fecha:"April 20, 2021",
      precio:-24,
      colorprecio:"text-danger"
    },
    {
      nombre:"Hosting press html",
      estado:"Vendido",
      fecha:"April 21, 2021",
      precio:24,
      colorprecio:"text-success"
    },
    {
      nombre:"Digital Agency PSD",
      estado:"Vendido",
      fecha:"April 23, 2021",
      precio:-14,
      colorprecio:"text-danger"
    },
    {
      nombre:"Helping Hands WP Theme",
      estado:"Vendido",
      fecha:"April 22, 2021",
      precio:64,
      colorprecio:"text-success"
    }

  ];

  private comentarios: Comentario[]=[
    {
      nombres: "James Anderson",
      comentario:"Lorem Ipsum es simplemente un texto ficticio de la industria de la impresión y la composición tipográfica. Ha sobrevivido no solo cinco siglos.",
      estados: "Pendiente",
      fecha:"April 14, 2021",
      imagen:'../../assets/plugins/images/users/varun.jpg',
      colorestado:"bg-primary"
    },
    {
      nombres: "Michael Jorden",
      comentario:"Lorem Ipsum es simplemente un texto ficticio de la industria de la impresión y la composición tipográfica. Ha sobrevivido no solo cinco siglos.",
      estados: "Aprobado",
      fecha:"April 15, 2021",
      imagen:'../../assets/plugins/images/users/genu.jpg',
      colorestado:"bg-success"
    },
    {
      nombres: "Johnathan Doeting",
      comentario:"Lorem Ipsum es simplemente un texto ficticio de la industria de la impresión y la composición tipográfica. Ha sobrevivido no solo cinco siglos.",
      estados: "Denegado",
      fecha:"April 16, 2021",
      imagen:'../../assets/plugins/images/users/ritesh.jpg',
      colorestado:"bg-danger"
    }

  ];
  private chat:Chats[]=[
    {
      nombres: "Varun Dhavan",
      estados: "online",
      colorchat:"text-success",
      photoperfil:'../../assets/plugins/images/users/varun.jpg'
    },
    {
      nombres: "Genelia Deshmukh",
      estados: "Ausente",
      colorchat:"text-warning",
      photoperfil:'../../assets/plugins/images/users/genu.jpg'
    },
    {
      nombres: "Ritesh Deshmukh",
      estados: "Ocupado",
      colorchat:"text-danger",
      photoperfil:'../../assets/plugins/images/users/ritesh.jpg'
    },
    {
      nombres: "Arijit Sing",
      estados: "Desconectado",
      colorchat:"text-muted",
      photoperfil:'../../assets/plugins/images/users/arijit.jpg'
    },
    {
      nombres: "Govinda Star",
      estados: "En Linea",
      colorchat:"text-success",
      photoperfil:'../../assets/plugins/images/users/govinda.jpg'
    },
    {
      nombres: "John Abraham",
      estados: "En Linea",
      colorchat:"text-success",
      photoperfil:'../../assets/plugins/images/users/hritik.jpg'
    },
  ];


  constructor(){
    console.log("Servicio Dashboard Listo para Usarse...")
  }

  getVentas():Venta[]{
    return this.ventas;
  }
  getComentario():Comentario[]{
    return this.comentarios;
  }
  getChat():Chats[]{
    return this.chat;
  }


}
export interface Venta{
  nombre: string;
  estado: string;
  fecha: string;
  precio: number;
  colorprecio:string;
};
export interface Comentario{
  nombres: string;
  comentario: string;
  estados: string;
  fecha: string;
  imagen:string;
  colorestado:string;
};
export interface Chats{
  nombres: string;
  estados: string;
  colorchat: string;
  photoperfil:string;
};
