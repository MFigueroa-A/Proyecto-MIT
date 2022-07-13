import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';


// import {Alumno} from '../modelos/alumno.model';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  constructor(private http:HttpClient) {
    console.log("Servicio Profile Listo...");
   }
   getProfile(){
     return this.http.get('http://localhost:8091/alumnos');
   }
}
