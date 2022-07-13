import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EquipoService {

  constructor(private http:HttpClient) { }
  getEquipo(){
    return this.http.get('http://localhost:8091/equipo');
  }
}
