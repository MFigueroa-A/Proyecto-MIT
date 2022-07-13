import { Component, OnInit } from '@angular/core';
import { ProfileService } from '../servicios/profile.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  listaPerfile:any []=[];
  constructor(private _profileService:ProfileService) {

    this._profileService.getProfile().subscribe((data:any)=>{
      this.listaPerfile=data;
      console.log(data);
    });
   }

  ngOnInit(): void {
  }

}
