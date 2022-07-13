import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class GraficoService {

  constructor(private http:HttpClient) {
    }

    getDatos(){
            var json1 = this.http.get('http://localhost:8091/api/sensores');
            /* for */
            for (var clave in json1){
              // Controlando que json realmente tenga esa propiedad
              if (json1.hasOwnProperty(clave)) {
                // Mostrando en pantalla la clave junto a su valor
                console.log(clave);
              }
            }
            return json1;
            /* return this.http.get('http://localhost:8091/api/sensores'); */
    }
}
