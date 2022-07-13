import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ClientesService {

  constructor(private http:HttpClient) {

  }
  getClientes(){
    return this.http.get('http://localhost:8091/clientes');
  }
  getComentarios(){
    return this.http.get('http://localhost:8091/comentarios');
  }
  getChat(){
    return this.http.get('http://localhost:8091/chat');
  }

}
