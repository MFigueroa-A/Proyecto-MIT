import { Component, OnInit } from '@angular/core';
import { ChartConfiguration, ChartOptions, ChartType } from "chart.js";
import { GraficoService } from '../servicios/grafico.service';

@Component({
  selector: 'app-grafico',
  templateUrl: './grafico.component.html',
  styleUrls: ['./grafico.component.css']
})
export class GraficoComponent {

  //datos = {sensores.MOUSTURE};
  /* datos = [ 59, 80, 81, 56, 55, 40 ]; */
  datos = [62.8, 62.8, 62.8, 62.7, 62.7, 61.8 , 62.8, 62.9, 62.9, 62.9, 62.0, 62.9, 62.8, 61.9 ];
 /*  horas = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July'
  ]; */
  horas =['2022-07-12 08:15:41', '2022-07-12 08:16:12', '2022-07-12 08:16:42', '2022-07-12 08:17:12', '2022-07-12 08:17:42', '2022-07-12 08:18:13' , '2022-07-12 08:18:43', '2022-07-12 08:19:13', '2022-07-12 08:19:43', '2022-07-12 08:20:17', '2022-07-12 08:20:47', '2022-07-12 08:21:17', '2022-07-12 08:21:47', '2022-07-12 08:22:20' ];
  listaDatos:any []=[];
  title = 'ng2-charts-demo';


  public lineChartData: ChartConfiguration<'line'>['data'] = {
    labels: this.horas,
    datasets: [
      {
        data: this.datos,
        label: 'Humedad Suelo',
        fill: true,
        tension: 0.5,
        borderColor: 'black',
        backgroundColor: 'rgba(255,0,0,0.3)'
      }
    ]
  };
  public lineChartOptions: ChartOptions<'line'> = {
    responsive: false
  };
  public lineChartLegend = true;

  constructor(private graficoServicio:GraficoService ) {
    this.graficoServicio.getDatos().subscribe((data:any)=>{
      this.listaDatos=data;
     /*  this.listaDatos=data[datos]; */
     /*  this.listaMeses=data[meses]; */
      console.log(data);
    });

   }
}




