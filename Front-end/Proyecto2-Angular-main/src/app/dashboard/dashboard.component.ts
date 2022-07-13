import { Component, OnInit } from '@angular/core';
import { DashboardService, Venta, Comentario,Chats } from '../servicios/dashboard.service';
import { ClientesService } from '../servicios/clientes.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
   ventas:Venta[]=[];
   comentarios:Comentario[]=[];
   chat:Chats[]=[];
   listaClientes:any []=[];
   listaComentarios:any[]=[];
   listaChat:any[]=[];


  constructor(private _clientesService:ClientesService) {
    //console.log("Creando El Componente dashboard..")
    // console.log(_dashboardService.getComentario());
    // this.ventas=_dashboardService.getVentas();
    // this.comentarios=_dashboardService.getComentario();
    // this.chat=_dashboardService.getChat();
    this._clientesService.getClientes().subscribe((data:any)=>{
      this.listaClientes=data;
      console.log(data);
    });
    this._clientesService.getComentarios().subscribe((data:any)=>{
      this.listaComentarios=data;
      console.log(data);
    });
    this._clientesService.getChat().subscribe((data:any)=>{
      this.listaChat=data;
      console.log(data);
    });
   }
  ngOnInit(): void {
  }

}
