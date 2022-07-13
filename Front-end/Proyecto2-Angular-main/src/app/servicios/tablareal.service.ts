import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TablarealService {

  constructor(private http:HttpClient) {
  }

    getTabla(){
      return this.http.get('http://localhost:8091/api/sensores');
    }


}
