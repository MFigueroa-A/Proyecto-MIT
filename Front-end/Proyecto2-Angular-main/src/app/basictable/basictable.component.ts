import { Component, OnInit } from '@angular/core';
import { BasictableService, Tabla } from '../servicios/basictable.service';
import {EquipoService} from '../servicios/equipo.service';


@Component({
  selector: 'app-basictable',
  templateUrl: './basictable.component.html',
  styleUrls: ['./basictable.component.css']
})
export class BasictableComponent implements OnInit {
  tabla:Tabla[]=[];
  listaEquipo:any[]=[];

  constructor(private _equipoService:EquipoService) {
    // this.tabla=_basictableService.gettabla();
    this._equipoService.getEquipo().subscribe((data:any)=>{
      this.listaEquipo=data;
      console.log(data);
    });

   }

  ngOnInit(): void {
  }

}
